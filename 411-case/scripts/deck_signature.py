#!/usr/bin/env python3
"""
deck_signature.py — Sign and verify the handoff contract between /411-case and /411-deck.

Hashes the *argument-bearing* fields of a deck-spec.md (argument_flow, per-slide
leadlines and callout items, and the recommendation statement + reasons + risks +
next steps). Technical/editable fields (chart type, data tables, axis labels,
footnotes, source lines, formatting notes) are intentionally excluded so that
post-signature typo-fixes don't invalidate the signature.

Usage:
  deck_signature.py --sign   <path-to-deck-spec.md>
  deck_signature.py --verify <path-to-deck-spec.md>

Exit codes (verify mode):
  0 — signature present and hash matches
  1 — signature missing entirely (no validation block)
  2 — signature present but hash mismatches (prints diff on stdout)
  3 — spec is malformed (missing frontmatter, missing required fields, etc.)

Pure stdlib (hashlib, json, re, sys, datetime, pathlib). No YAML parser
dependency — uses a minimal hand-rolled parser scoped to the deck-spec shape.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


SKILL_VERSION = "411-case@1.0.0"


def read_spec(path: Path) -> tuple[dict, str, str]:
    """Split the file into frontmatter (dict), body (string), and raw text.

    Returns (frontmatter_dict, body_text, raw_text).
    Raises ValueError if the file has no frontmatter.
    """
    raw = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, flags=re.DOTALL)
    if not m:
        raise ValueError("No YAML frontmatter found (expected file to start with ---).")
    fm_text, body = m.group(1), m.group(2)
    return parse_yaml_like(fm_text), body, raw


def parse_yaml_like(text: str) -> dict:
    """Minimal YAML parser scoped to the deck-spec frontmatter shape.

    Supports: top-level scalars (quoted or unquoted), nested 2-space-indented
    blocks one level deep, and list syntax `[a, b, c]` OR `- item` lines.
    Not a general YAML parser — do not use elsewhere.
    """
    result: dict = {}
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue
        if line.startswith("  "):
            i += 1
            continue
        m = re.match(r"^([a-zA-Z_][a-zA-Z0-9_]*):\s*(.*)$", line)
        if not m:
            i += 1
            continue
        key, val = m.group(1), m.group(2).rstrip()
        if val == "":
            block, i = collect_block(lines, i + 1)
            result[key] = block
        elif val.startswith("["):
            result[key] = parse_inline_list(val)
            i += 1
        else:
            result[key] = strip_quotes(val)
            i += 1
    return result


def collect_block(lines: list[str], start: int) -> tuple[object, int]:
    """Collect a nested block starting at `start`. Returns (value, next_index)."""
    block_lines: list[str] = []
    i = start
    while i < len(lines):
        line = lines[i]
        if line.strip() == "":
            i += 1
            continue
        if not line.startswith("  "):
            break
        block_lines.append(line[2:])
        i += 1
    if not block_lines:
        return {}, i
    if all(bl.lstrip().startswith("- ") for bl in block_lines if bl.strip()):
        items = [strip_quotes(bl.lstrip()[2:].rstrip()) for bl in block_lines if bl.strip()]
        return items, i
    sub: dict = {}
    for bl in block_lines:
        m = re.match(r"^([a-zA-Z_][a-zA-Z0-9_]*):\s*(.*)$", bl)
        if m:
            sub[m.group(1)] = strip_quotes(m.group(2))
    return sub, i


def parse_inline_list(val: str) -> list:
    inner = val.strip().lstrip("[").rstrip("]")
    if not inner.strip():
        return []
    parts = [p.strip() for p in inner.split(",")]
    out: list = []
    for p in parts:
        if re.fullmatch(r"-?\d+", p):
            out.append(int(p))
        else:
            out.append(strip_quotes(p))
    return out


def strip_quotes(s: str) -> str:
    s = s.strip()
    if len(s) >= 2 and ((s[0] == '"' and s[-1] == '"') or (s[0] == "'" and s[-1] == "'")):
        return s[1:-1]
    return s


SLIDE_HEADER_RE = re.compile(r"^###\s+Slide\s+([^:\n]+):\s*(.*)$", re.MULTILINE)


def parse_slides(body: str) -> list[dict]:
    """Split body into per-slide sections and extract argument fields.

    Each slide dict has: id (str), leadline (str), callout_items (list[str]).
    Non-argument fields (chart type, data, axes, footnotes, source) are intentionally
    NOT extracted — they are excluded from the signature.
    """
    positions = [(m.start(), m.group(1).strip(), m.group(2).strip()) for m in SLIDE_HEADER_RE.finditer(body)]
    if not positions:
        return []
    slides: list[dict] = []
    for idx, (start, slide_id, _title) in enumerate(positions):
        end = positions[idx + 1][0] if idx + 1 < len(positions) else len(body)
        section = body[start:end]
        slides.append({
            "id": slide_id,
            "leadline": extract_field(section, "Leadline"),
            "callout_items": extract_callout_items(section),
            "recommendation": extract_recommendation(section) if slide_id.upper() == "R" else None,
        })
    return slides


def extract_field(section: str, field: str) -> str:
    m = re.search(rf"^\*\*{re.escape(field)}:\*\*\s*(.*)$", section, re.MULTILINE)
    return m.group(1).strip() if m else ""


def extract_callout_items(section: str) -> list[str]:
    m = re.search(r"^\*\*Callout items:\*\*\s*\n((?:-.*\n?)+)", section, re.MULTILINE)
    if not m:
        return []
    block = m.group(1)
    return [ln.lstrip("- ").strip() for ln in block.strip().split("\n") if ln.strip().startswith("-")]


def extract_list_field(section: str, field: str) -> list[str]:
    m = re.search(rf"^\*\*{re.escape(field)}:\*\*\s*\n((?:(?:-|\d+\.).*\n?)+)", section, re.MULTILINE)
    if not m:
        single = extract_field(section, field)
        return [single] if single else []
    block = m.group(1)
    items = []
    for ln in block.strip().split("\n"):
        s = ln.strip()
        s = re.sub(r"^(-|\d+\.)\s*", "", s)
        if s:
            items.append(s)
    return items


def extract_recommendation(section: str) -> dict:
    return {
        "recommendation": extract_field(section, "Recommendation"),
        "supporting_reasons": extract_list_field(section, "Supporting reasons"),
        "key_risks": extract_list_field(section, "Key risks"),
        "next_steps": extract_list_field(section, "Next steps"),
    }


def canonical_hash_input(fm: dict, slides: list[dict]) -> str:
    """Produce the canonical string that gets sha256'd.

    Format — one field per line, with explicit markers so a diff is meaningful:
        ARGUMENT_FLOW[0]: ...
        ARGUMENT_FLOW[1]: ...
        SLIDE[1].LEADLINE: ...
        SLIDE[1].CALLOUT[0]: ...
        SLIDE[1].CALLOUT[1]: ...
        ...
        REC.STATEMENT: ...
        REC.REASON[0]: ...
        REC.RISK[0]: ...
        REC.NEXT[0]: ...
    """
    lines: list[str] = []
    for i, item in enumerate(fm.get("argument_flow", []) or []):
        lines.append(f"ARGUMENT_FLOW[{i}]: {item}")
    for s in slides:
        sid = s["id"]
        if sid.upper() == "R":
            rec = s.get("recommendation") or {}
            lines.append(f"REC.STATEMENT: {rec.get('recommendation', '')}")
            for i, r in enumerate(rec.get("supporting_reasons", [])):
                lines.append(f"REC.REASON[{i}]: {r}")
            for i, r in enumerate(rec.get("key_risks", [])):
                lines.append(f"REC.RISK[{i}]: {r}")
            for i, n in enumerate(rec.get("next_steps", [])):
                lines.append(f"REC.NEXT[{i}]: {n}")
        else:
            lines.append(f"SLIDE[{sid}].LEADLINE: {s.get('leadline', '')}")
            for i, c in enumerate(s.get("callout_items", [])):
                lines.append(f"SLIDE[{sid}].CALLOUT[{i}]: {c}")
    return "\n".join(lines) + "\n"


def compute_hash(fm: dict, slides: list[dict]) -> tuple[str, str]:
    canonical = canonical_hash_input(fm, slides)
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    return f"sha256:{digest}", canonical


def sign(path: Path) -> int:
    fm, body, raw = read_spec(path)
    slides = parse_slides(body)
    digest, _canonical = compute_hash(fm, slides)
    validation_block = "\n".join([
        "validation:",
        "  validated: true",
        f'  validated_at: "{datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}"',
        f'  validated_by: "{SKILL_VERSION}"',
        f'  content_hash: "{digest}"',
        "  hashed_fields: [argument_flow, leadlines, callout_items, recommendation]",
    ])
    m = re.match(r"^(---\n)(.*?)(\n---\n)(.*)$", raw, flags=re.DOTALL)
    if not m:
        print("ERROR: frontmatter not found", file=sys.stderr)
        return 3
    existing_fm = m.group(2)
    existing_fm = re.sub(r"^validation:\n(?:  .*\n)*", "", existing_fm, flags=re.MULTILINE)
    new_fm = existing_fm.rstrip() + "\n" + validation_block
    new_text = m.group(1) + new_fm + m.group(3) + m.group(4)
    path.write_text(new_text, encoding="utf-8")
    print(json.dumps({"status": "signed", "hash": digest, "path": str(path)}, indent=2))
    return 0


def verify(path: Path) -> int:
    try:
        fm, body, _raw = read_spec(path)
    except ValueError as e:
        print(json.dumps({"status": "malformed", "reason": str(e)}, indent=2))
        return 3
    validation = fm.get("validation")
    if not validation or not isinstance(validation, dict):
        print(json.dumps({"status": "missing", "reason": "no validation block in frontmatter"}, indent=2))
        return 1
    stored_hash = validation.get("content_hash", "")
    if not stored_hash:
        print(json.dumps({"status": "missing", "reason": "validation block present but no content_hash"}, indent=2))
        return 1
    slides = parse_slides(body)
    current_hash, current_canonical = compute_hash(fm, slides)
    if current_hash == stored_hash:
        print(json.dumps({
            "status": "ok",
            "hash": current_hash,
            "validated_at": validation.get("validated_at", ""),
            "validated_by": validation.get("validated_by", ""),
        }, indent=2))
        return 0
    print(json.dumps({
        "status": "mismatch",
        "stored_hash": stored_hash,
        "current_hash": current_hash,
        "current_canonical_preview": current_canonical[:2000],
        "reason": "content has been edited since signing — compare stored_hash vs current_hash, and inspect current_canonical_preview to see what the skill is hashing now",
    }, indent=2))
    return 2


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--sign", metavar="PATH", help="Compute hash and write signature block into frontmatter")
    g.add_argument("--verify", metavar="PATH", help="Verify the signature block matches current content")
    args = ap.parse_args()
    if args.sign:
        return sign(Path(args.sign).expanduser())
    return verify(Path(args.verify).expanduser())


if __name__ == "__main__":
    sys.exit(main())
