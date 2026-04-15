# Deck Spec Handoff Template

> Template asset — used in Phase 6 Step 4 to generate the handoff file for `/411-deck`.

## Format

```markdown
---
case_name: "Company X Strategic Response"
recommendation_format: "single"  # or "multiple-options"
scqa:
  situation: "..."
  complication: "..."
  question: "..."
  answer: "..."
key_line: "..."
structure: "inductive"  # or "deductive"
plural_noun: "three reasons"
argument_flow:
  - "Leadline 1 summary"
  - "Leadline 2 summary"
  - "Leadline 3 summary"
sensitivity_slides: [4, 7]
---

# Deck Spec: Company X Strategic Response

## Argument Summary
[Reading just the leadlines tells this story — numbered list]

---

### Slide 1: [Short title]

**Position:** [Where in argument flow]
**Leadline:** [Analytical statement]
**Chart type:** [Bar/line/scatter/waterfall/table/etc.]
**Chart title:** [Descriptive label]
**Data:**
| Col1 | Col2 | Col3 |
|------|------|------|
| ...  | ...  | ...  |
**X-axis:** [Label]
**Y-axis:** [Label]
**Data labels:** [Instruction]
**Callout title:** Key Implications
**Callout items:**
- [Strategic conclusion 1]
- [Strategic conclusion 2]
**Footnotes:** [Numbered footnotes]
**Source:** [Specific source, year]
**Formatting notes:** [Any special instructions]

---

### Slide R: Recommendation

**Position:** Final slide
**Leadline:** [Recommendation statement]
**Format:** [single / multiple-options]
**Recommendation:** [Clear statement]
**Supporting reasons:** [Numbered list]
**Key risks:** [Bulleted list]
**Next steps:** [Numbered list]
```

## Platform Case Additions

For platform portfolio cases, add to frontmatter:

```yaml
platform_case: true
theme: "..."
quadrant_map:
  q1: [...]
  q2: [...]
  q3: [...]
  q4: [...]
governance:
  own: [...]
  partner: [...]
  affiliate: [...]
sequence: [ordered list]
deep_dive: "first investment name"
```
