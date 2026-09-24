---
name: sources-cited
description: >
  Track, organize, and export research sources into a professional .docx bibliography document. Use this skill whenever you are collecting data from multiple sources and need to maintain a citation trail — for case analyses, research projects, literature reviews, competitive intelligence, or any task where source attribution matters. Trigger when the user mentions "sources," "citations," "bibliography," "works cited," "references list," "source tracking," "cite your sources," or when another skill (like 411-case) invokes source tracking during a research phase. Also trigger when the user asks to "make a sources document," "list where you got that," or "show me your sources." This skill produces a .docx file as its final output.
---

# Sources-Cited Skill

This skill maintains a running log of data sources during any research task and produces a formatted .docx bibliography at the end.

## How It Works

### 1. Initialize the Source Log

When invoked, create an in-memory source log (a structured list). Each entry contains:

| Field | Description |
|---|---|
| **id** | Sequential number (1, 2, 3...) |
| **data_point** | The specific fact, number, or claim sourced |
| **source_name** | Name of the source (publication, website, report title) |
| **source_url** | Direct URL — link as close to the highlighted information as possible |
| **date_accessed** | Date the source was accessed |
| **assumption** | Which assumption or analysis this data supports (if applicable) |
| **reliability** | `Verified` or `Estimate` — with one-sentence justification |
| **notes** | Any caveats about data quality, methodology, or reliability |

### 2. Add Sources During Research

As data is collected (by you or by a parent skill like 411-case), add each source to the log immediately. Guidelines:

- **One entry per distinct data point.** If a single source provides 3 different numbers, create 3 entries pointing to the same source.
- **Deep-link when possible.** Don't just link to the homepage — link to the specific page, section, or paragraph. If the source is a PDF, note the page number.
- **Flag quality.** In the notes field, mark sources as: `primary` (original data), `secondary` (reporting on someone else's data), or `estimate` (calculated/inferred).
- **Label data reliability.** For each data point, assign one of two labels:
  - **Verified** — sourced directly from a primary/authoritative source (SEC filing, government report, company 10-K, peer-reviewed study, official statistics)
  - **Estimate** — derived, projected, calculated, or from a secondary source (analyst report, news article citing unnamed sources, industry estimates, proxy data)
- **Justify the label.** Add one sentence explaining why this classification applies: "Verified: directly from Netflix 2023 10-K filing" or "Estimate: analyst projection based on partial-year data."
- **Record access date.** Web sources change; the access date establishes what was available when you looked.

### 3. Present Sources for Review

Before generating the final document, present the full source log to the user in a readable table format. Ask them to:

- Verify source credibility
- Flag any sources they want replaced
- Confirm the data points are accurately captured
- Add any sources they found independently

### 4. Generate the .docx

Once the user approves, invoke the `docx` skill to produce a formatted Word document.

**Document structure:**

```
SOURCES CITED
[Project/Case Name]
Generated [Date]

─────────────────────────────────

SECTION: [Assumption or Analysis Category]

1. [Data Point]
   Source: [Source Name]
   URL: [hyperlinked URL]
   Accessed: [Date]
   Quality: [Primary / Secondary / Estimate]
   Reliability: [Verified / Estimate] — [one-sentence justification]
   Notes: [Any caveats]

2. [Data Point]
   ...

─────────────────────────────────

SECTION: [Next Assumption or Category]

3. [Data Point]
   ...

─────────────────────────────────

SUMMARY
Total sources: [N]
Primary sources: [N]
Secondary sources: [N]
Estimates: [N]
```

**Formatting requirements:**
- Use heading styles for section headers
- Hyperlink all URLs (clickable in Word)
- Use a professional, clean font (Calibri or similar)
- Include a table of contents if more than 10 sources
- Group sources by assumption/category, then order by ID within each group

### 5. Save and Share

Save the .docx to the workspace folder and provide a computer:// link to the user.

---

## Standalone Usage

This skill can be used independently (not just from 411-case). If the user asks to track sources for any research task:

1. Ask what they're researching and how they want sources organized (by topic, by date, alphabetically)
2. Initialize the log
3. As you research, add entries
4. Present for review
5. Generate the .docx

## Integration with Other Skills

When another skill invokes sources-cited:
- The parent skill passes the organizing structure (e.g., assumptions from 411-case)
- Sources-cited maintains the log and produces the document
- The parent skill continues its workflow after the document is generated
