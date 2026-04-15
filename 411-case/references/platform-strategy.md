# Platform Strategy (Internal Reference)

> **Preamble:** This file informs Claude's reasoning during case analysis of platform businesses. Never name these theories, models, or frameworks to students. Use them to shape questions, frame analysis, and recognize strategic patterns. Translate insights into plain strategic language or Socratic questions.

> **Connection to Other Theory Files:** The competitive positioning frameworks analyze how to win WITHIN a single market. Platform strategy analyzes which markets (interactions) a platform should HOST and how to sequence them. Use this file when the firm's core problem is about scope (what portfolio of interactions to offer) rather than positioning (how to compete in one interaction). The other theory files still apply to the deep-dive analysis of individual interactions.

> **When to Activate:** The firm is a platform business (multi-sided marketplace connecting distinct participant groups) AND the case question is about growth, expansion, diversification, or what to do when the core interaction matures. Signals: slowing growth in the core, competitors expanding faster through broader portfolios, investor pressure for "what's next."

---

## 1. Core Definitions

### Sides, Interactions, Engagement

Three building blocks of any platform, arranged in a hierarchy:

| Building Block | Definition | Example (Uber) | Example (Airbnb) |
|---------------|-----------|-----------------|-------------------|
| **Sides** | Distinct participant groups with different reasons for being on the platform (WHO) | Riders, Drivers | Guests, Hosts |
| **Interactions** | Types of exchanges between sides (WHAT) | Ride-hailing, Food delivery, Package delivery | Short-term rental booking, Experiences |
| **Engagement** | Intensity of existing interactions (HOW MUCH) | Rides per user, Driver hours | Nights per user, Repeat booking rate |

**Hierarchy:** Sides -> Interactions -> Engagement (players -> games -> rounds played)

**Strategic insight:** Most platform teams default to engagement optimization (marketing, retention, onboarding) with almost no process for evaluating new interactions or sides. That is like a restaurant only optimizing table turnover when it could add catering or delivery.

---

## 2. The Growth Matrix (2x2)

Four growth quadrants defined by two dimensions: existing vs. new sides, and existing vs. new interactions.

```
                        INTERACTIONS
                 Existing              New
            +-------------------+---------------------+
   Existing |  Q1: DEEPEN        |  Q2: ADD NEW         |
            |   ENGAGEMENT       |   INTERACTIONS       |
 S          |  Features, virality |  Complement or       |
 I          |  lower friction,    |  substitute offers   |
 D          |  referral mechanics |  for existing users   |
 E          +-------------------+---------------------+
 S     New  |  Q3: ADD NEW        |  Q4: NEW SIDES       |
            |   SIDES            |   + INTERACTIONS     |
            |  New user groups    |  Highest growth,     |
            |  or provider types  |  highest complexity  |
            +-------------------+---------------------+
```

### Quadrant Playbooks

**Q1: Deepen Engagement (Existing Sides, Existing Interactions)**
- Release engagement features early -- do not wait for scale
- Build virality through chain interactions and referral mechanics
- Reduce transaction costs to boost usage frequency
- Engagement features deepen network effects AND reduce switching costs
- *Case: Venmo delayed instant transfer and QR codes for 8 years. Cash App launched 4 years later but shipped instant deposit early and captured ~45% of P2P transactions.*

**Q2: Add New Interactions (Existing Sides, New Interactions)**
Two types:
- **Complements** -- enhance another interaction's value (WeChat Pay complements shopping; Airbnb Experiences complements lodging)
- **Substitutes** -- alternative way to get a job done on-platform (Uber rentals substitute for ride-hailing; Facebook Dating substitutes for Match.com)
Both deepen engagement without requiring new user types.

**Q3: Add New Sides (New Sides, Existing Interactions)**
- **New Producers:** SDKs, APIs, and app stores lower entry barriers. Financial incentives or equity stakes for high-value partners. Identify off-platform producers that existing users already interact with.
  - *Amazon: publishers -> added authors. Airbnb: homeowners -> added boutique hotels.*
- **New Consumers:** Target sides with overlapping needs to stimulate cross-side interaction. Subsidies, discounts, referral bonuses to motivate adoption.
  - *LinkedIn: professionals -> added companies. Uber: adults -> added teen accounts (13-17) with parental controls.*

**Q4: New Sides + New Interactions (Highest Growth, Highest Complexity)**
- Adding both simultaneously accelerates growth but requires deliberate mode selection (see Own/Partner/Affiliate below)
- Cross-platform synergy: new sides also participate in existing interactions; new interactions also serve existing sides
- *This is where super-apps live (Meituan, WeChat) -- but only when unified by a coherent theme*

### How Claude Uses the Growth Matrix

1. **Phase 1 (Problem Framing):** Map the firm's current sides, interactions, and engagement levers. Identify where past growth moves concentrated (usually Q1).
2. **Phase 2 (Solution Development):** Walk through each quadrant systematically to generate growth options. The matrix is a MAP of possibilities, not alternatives to choose between.
3. **Historical mapping:** Before proposing new moves, map every past growth move into the matrix WITH DATES. This reveals concentration patterns and underexplored quadrants.

---

## 3. Unifying Theme

A platform's growth ceiling depends on how broadly it defines its theme early on. Without a coherent theme, expansion becomes random bundling.

### Theme = the filter for what belongs in the portfolio

| Platform | Theme | What It Justified | Outcome |
|----------|-------|-------------------|---------|
| Meituan | "Local goods and services on-demand" | Food delivery, pharmacy, local travel, entertainment, health & beauty | 100x faster growth than Groupon |
| Groupon | "Group buying" | Constrained to daily deals | Theme too narrow, limited expansion |
| Uber | "On-demand mobility/transportation" | Food delivery, package delivery, rental cars, 2-wheel vehicles | 180% 5-yr revenue growth ($13B -> $37B) |
| Lyft | "Ride-hailing" | Core rides only | 20% 5-yr growth ($3.6B -> $4.4B) |
| Cash App | "Financial ecosystem for everyday Americans" | Debit card ('17), Bitcoin ('18), tax filing ('20), stocks ('21), loans ('23), savings ('24) | 57M users, $16.25B revenue |

### Theme Evaluation Criteria

Ask: Is the theme...
- **Broad enough** to permit multi-quadrant expansion?
- **Narrow enough** to create coherence (not "we do everything")?
- **Authentic** to what the platform already does well?
- **Reinforcing** -- do new interactions under this theme strengthen existing ones?

### When to Offer

In Phase 2, BEFORE generating growth options. The theme must be established first because it determines which Q2-Q4 moves make sense and which do not.

**Offer prompt:** "Before we brainstorm growth moves -- what vision or theme should guide expansion? This determines what belongs in the portfolio and what doesn't."

---

## 4. Own, Partner, or Affiliate (Value Curve)

Not all interactions need to be owned. Map interactions along a power-law value curve:

```
  Value |
        |  ### OWN: Highest-value interactions, full control
        |     #### PARTNER: Shared governance, equity stakes
        |        ##### AFFILIATE: Open platform, 3rd-party experiments
        +------------------------------------------------->
              Interactions ranked by value (head -> tail)
```

| Mode | When to Use | Example |
|------|-------------|---------|
| **Own** (head) | Highest-value, most strategic interactions. Full control required. | WeChat Messaging, WeChat Pay |
| **Partner** (middle) | Shared governance, 15-20% equity stakes. Co-development. | Tencent -> JD.com, DiDi, Meituan |
| **Affiliate** (tail) | Open platform. Let 3rd parties experiment. Low investment, high option value. | Mini Programs, long-tail developers |

**The curve is dynamic.** Pinduoduo and Meituan started as tail affiliates on Tencent's platform and graduated to equity partners as they proved value. This is a low-risk options strategy: let the tail experiment, promote winners.

### When to Offer

In Phase 2, AFTER the growth matrix is mapped. For each proposed interaction, ask which governance mode fits.

**Offer prompt:** "For each of these growth moves -- should the platform build it in-house, partner with someone, or open it up for third parties to build?"

---

## 5. Sequencing Logic

Growth moves should be ordered, not pursued simultaneously. Dependencies between quadrants create a natural sequence:

### Default Sequence

1. **Q1 first** -- strengthen the core before expanding. A weak core undermines everything built on top of it.
2. **Q2 next** -- new interactions for existing users are lower risk (no new user acquisition needed).
3. **Q3 then** -- new sides require new acquisition channels but can participate in existing interactions.
4. **Q4 last** -- new sides AND new interactions require the most investment and coordination.

### Sequencing Criteria

Within each quadrant, order moves by:
1. **Leverage of existing assets** -- does this reuse existing sides, trust infrastructure, or data?
2. **Cross-side synergy with core** -- does this make the core interaction more valuable?
3. **Investment required** -- lower investment moves de-risk the portfolio before bigger bets

### When to Offer

In Phase 2, AFTER governance modes are assigned. Present the proposed sequence and ask if the ordering makes sense.

**Offer prompt:** "Here's a proposed sequence for these growth moves. Does this ordering make sense given the dependencies?"

---

## 6. Platform-Specific Assumption Categories

These supplement (do not replace) the standard 8 categories in `references/assumption-categories.md`. Use when stress-testing platform growth moves in Phase 3.

### 9. Network Effect Assumptions

Questions to ask: Will this move strengthen or dilute existing network effects? Does cross-side synergy exist? Will existing users benefit?

**Example assumptions:**
- "Adding [new side/interaction] will strengthen existing network effects rather than dilute them"
- "Cross-side synergy exists: existing users will want [new interaction] from [existing/new side]"
- "The new interaction creates data/trust/relationship spillovers that make the core more valuable"
- "Network effects in the new interaction are strong enough to create a defensible position"

### 10. Platform Governance Assumptions

Questions to ask: Is the governance mode right? Can the platform attract quality providers? Does existing trust infrastructure extend?

**Example assumptions:**
- "The right governance mode for [interaction] is [own/partner/affiliate] because [rationale]"
- "The platform can attract quality [new side] providers at scale"
- "The platform's trust and review infrastructure extends naturally to [new interaction]"
- "Revenue sharing / incentive structure is attractive enough for [partners/affiliates]"

### 11. Portfolio Coherence Assumptions

Questions to ask: Does this fit the theme? Will users see it as natural? Does it cannibalize or complement?

**Example assumptions:**
- "This interaction fits the unifying theme of [theme]"
- "This interaction does not cannibalize [existing interaction] -- it complements it"
- "Users will perceive this as a natural extension, not brand confusion or distraction"
- "The platform's brand can credibly extend to host [new interaction]"

---

## 7. Platform Slide Templates

Use these ASCII templates when building mock slides in Phase 4 for platform cases.

### Historical Growth Matrix (Past Moves with Dates)

```
LEADLINE: [Analytical statement about where past growth concentrated]

                        INTERACTIONS
                 Existing              New
            +-------------------+---------------------+
   Existing |  [Move] (YYYY)     |  [Move] (YYYY)       |
            |  [Move] (YYYY)     |  [Move] (YYYY)       |
 S          |  [Move] (YYYY)     |                      |
 I          |  [Move] (YYYY)     |                      |
 D          +-------------------+---------------------+
 E     New  |  [Move] (YYYY)     |  [Move] (YYYY)       |
 S          |                    |                      |
            +-------------------+---------------------+

Key Implications:
- [Where has effort concentrated?]
- [Which quadrants are underexplored?]
- [What does this reveal about strategic bias?]

Source: Case document pp. X-Y
```

### Proposed Growth Matrix (New Opportunities)

```
LEADLINE: [Analytical statement about where untapped growth lies]

                        INTERACTIONS
                 Existing              New
            +-------------------+---------------------+
   Existing |  [Existing moves    |  [Proposed move]     |
            |   in grey]         |  [Proposed move]     |
 S          |  + [New Q1 move]    |  [Proposed move]     |
 I          +-------------------+---------------------+
 D     New  |  [Proposed move]    |  [Proposed move]     |
 E          |  [Proposed move]    |  [Proposed move]     |
 S          +-------------------+---------------------+

Key Implications:
- [Which moves are highest priority?]
- [What theme unifies these choices?]

Source: Analysis based on [framework reference]
```

### Value Curve (Own / Partner / Affiliate)

```
LEADLINE: [Statement about governance mode distribution]

  Value |
        |  ## OWN: [Interaction 1], [Interaction 2]
        |     ### PARTNER: [Interaction 3], [Interaction 4]
        |        #### AFFILIATE: [Interaction 5], [Interaction 6]
        +------------------------------------------------->
              Interactions ranked by strategic value

Key Implications:
- [Why own the head?]
- [What partnerships unlock?]
- [How affiliates graduate over time?]

Source: [Value curve framework, Bryce et al.]
```

### Sequencing Timeline

```
LEADLINE: [Statement about sequencing rationale]

  Year 1          Year 2          Year 3          Year 4+
  |               |               |               |
  [Q1 move]  -->  [Q2 move]  -->  [Q3 move]  -->  [Q4 move]
  [Q1 move]       [Q2 move]       [Q3 move]

  STRENGTHEN      EXPAND          ADD NEW         FULL
  THE CORE        INTERACTIONS    SIDES           PORTFOLIO

Key Implications:
- [Why this order?]
- [What dependencies exist?]
- [What milestones trigger the next phase?]

Source: Analysis
```

---

## 8. Case Comparisons

Use these contrasts to illustrate platform strategy concepts without naming the framework:

| Comparison | What It Shows |
|-----------|---------------|
| Uber vs. Lyft | Q1-Q4 expansion (180% growth) vs. Q1-only (20% growth) |
| Meituan vs. Groupon | Broad theme (100x value) vs. narrow theme |
| Cash App vs. Venmo | Early engagement features vs. delayed features |
| Tencent value curve | Dynamic graduation from affiliate -> partner -> owned |
| WeChat vs. single-purpose apps | Theme-based super-app vs. siloed interactions |

---

## Internal Questions Claude Should Ask

Use these to determine when and how to apply platform strategy concepts:

### When to Activate Platform Strategy
- Is the firm a multi-sided platform connecting distinct participant groups?
- Is the case question about growth, expansion, or "what's next" rather than competitive positioning within one market?
- Is the core interaction maturing (slowing growth, market saturation, competitive pressure)?
- Are competitors growing faster through broader portfolios of interactions?

### During Problem Framing (Phase 1)
- What are the firm's current sides? Are there sides that interact off-platform?
- What are the firm's current interactions? How many revenue streams exist?
- Where has engagement growth come from? Is it decelerating?
- What is the competitor portfolio scope? Who offers more interactions?

### During Solution Development (Phase 2)
- Has the firm over-indexed on Q1 (engagement) at the expense of Q2-Q4?
- Is the firm's implicit theme broad enough to permit multi-quadrant expansion?
- For each proposed interaction: complement or substitute? Own, partner, or affiliate?
- What is the natural sequence? What depends on what?

### During Assumption Mapping (Phase 3)
- For each growth move: will it strengthen or dilute existing network effects?
- Does the platform's trust infrastructure extend to the new interaction?
- Will users perceive this as coherent with the platform's identity?
- Is the governance mode assumption realistic? Can the platform attract quality providers?

### Pattern Recognition
- Student describes a platform with strong financials but stagnant stock -> core interaction ceiling, needs Q2-Q4
- Student proposes many unrelated growth moves -> missing a unifying theme, random bundling risk
- Student says "build everything in-house" -> challenge with own/partner/affiliate value curve
- Student proposes adding new interactions without considering sequence -> ask about dependencies and risk ordering
- Student focuses exclusively on engagement metrics -> ask about interaction and side diversity

---

## Sources

- Bryce, D. J., Dyer, J. H., & Van Alstyne, M. W. (2025). "Are You Missing Growth Opportunities for Your Platform?" *Harvard Business Review*, May-June 2025.
- Platform Growth 2026 lecture slides, STRAT 411, BYU Marriott School of Business.
