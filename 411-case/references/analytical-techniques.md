# Analytical Techniques and Templates

## 1. Standard Hypothesis Types — Routing Table

Use this table first. Match the hypothesis type → jump to the numbered section.

| Hypothesis Type | Template | Jump To |
|---|---|---|
| **Comparison** | "If A were like B, performance would improve by __%" | § 2 |
| **Categorization** | "__% of the effect is concentrated in __% of the input" | § 3 |
| **Change** | "If the current trend continues, then..." | § 4 |
| **Correlation** | "Factor A is associated with (or causes) Factor B" | § 5 |
| **Description** | "An examination of this issue reveals..." | § 6 |
| **Impact** | "The financial effect of this decision is $__ under [scenario]" | § 8 |

### Reverse Lookup — What Data Do You Have?

Use this table when you have data in hand and want to know what analyses it can support.

| Data you have | Analyses available |
|---|---|
| One metric across multiple entities, no time dimension | Comparison (§ 2), Categorization (§ 3) |
| One metric for one or more entities over time | Change (§ 4) |
| Two metrics per entity, paired observations | Correlation (§ 5) |
| Individual-level records (per customer, SKU, deal) | Categorization — Pareto (§ 3) |
| Qualitative ratings, text, or feature presence/absence | Description (§ 6) |
| Volume + price + cost assumptions | Output-Based Modeling (§ 8) |
| Firm positions on strategic dimensions | Strategic Group Mapping (§ 10), Strategy Canvas (§ 11) |
| Many correlated attributes per entity (10+) | Factor Analysis Positioning (§ 12) |
| One metric, two groups, before/after an event | Segmented Regression or ANOVA (§ 9) |

---

## 2. Comparison Analysis

**What it analyzes:** Relative magnitudes and differences between entities, groups, or time periods.

**Triggers — use when:**
- You want to show what performance would look like if one entity matched another
- You have two or more groups, companies, or departments to contrast
- The key question is "how much better/worse," not "what caused it"

**Data inputs required:**
- The same metric measured consistently across all entities
- Defined units (revenue per employee, cost per unit, etc.)
- A baseline entity to benchmark against

### Benchmarking Bar Chart
Horizontal bars sorted descending. Gap to target line = opportunity size.

```
Performance (units/employee)

Comp A  |████████████████| 8.0
Comp B  |████████████| 6.0  ← benchmark line
Comp C  |████████| 4.0
Comp D  |█████| 2.5
         0    2    4    6    8
```
Gap between each bar and the benchmark = the quantifiable improvement opportunity.

### Stacked 100% Columns (Relative Mix)
Each bar totals 100%; segments show proportional composition. Absolute size is hidden.

```
           Seg A    Seg B    Seg C
Yr 1  [███████████░░░░░░░▒▒▒▒▒▒]  100%
Yr 2  [█████████░░░░░░░░░▒▒▒▒▒▒▒]  100%
Yr 3  [███████░░░░░░░░░░░░▒▒▒▒▒▒▒▒]  100%
        ~50%       ~30%      ~20%
```
Shift in segment widths over time shows mix change, independent of volume.

### Absolute Stacked Columns (Total + Composition)
Bar height = actual total; segments reveal what drives growth or decline.

```
Revenue ($M)
120 │       ┌────┐  ┌────┐
 90 │  ┌────┤ C  ├──┤ C  │
 60 │  │ B  ├────┤  ├────┤
 30 │  ├────┤ A  ├──┤ A  │
  0 └──┴────┴────┴──┴────┴──
       Yr1        Yr2    Yr3
```
Taller bars show absolute growth; widening/shrinking segments show which part is driving it.

### Difference Chart (Net Delta)
Plots (Series A − Series B) directly. Above zero = A leads; below = B leads.

```
Margin gap (A minus B, pp)

+10 │       ╭──╮
 +5 │   ╭───╯  ╰──╮
  0 ├───╯          ╰───
 -5 │                  ╰──╮
-10 │                      ╰─
     Yr1   Yr2   Yr3   Yr4   Yr5
```
When and by how much the gap opened, closed, or flipped — not the absolute levels.

### Waterfall Chart (Bridge)
Used in Comparison to show how you get from Entity A's total to Entity B's total, or from baseline to target. Each bar = one contributing factor.

```
Cost per unit ($)

 80 │ ┌──┐
 70 │ │  │  ┌──┐
 60 │ │  │  │//│  ┌──┐  ┌──┐
 50 │ │  │  │//│  │  │  │  │ ← Target
 40 │ │  │  │//│  │  │  │  │
    └─┴──┴──┴──┴──┴──┴──┴──┴─
     Co A  -Labor -Waste +Matl  Co B
           (hatched = cost add; solid = savings)
```
How much each factor accounts for the gap between two entities. *Also appears in § 3 as a categorization tool when building up a total from parts.*

---

## 3. Categorization Analysis

**What it analyzes:** Concentration — which inputs, customers, or factors account for most of the output.

**Triggers — use when:**
- You suspect outcomes are unequally distributed (80/20 hypothesis)
- You want to show "where to focus" rather than "how much total"
- You need to justify resource reallocation

**Data inputs required:**
- Individual-level data (per customer, per SKU, per store, etc.)
- A single output metric to rank by (revenue, cost, complaints, etc.)
- Ideally 20+ observations for the pattern to be visible

### Pareto Bar Chart (Ranked)
Bars sorted highest to lowest. X-axis = rank (ordinal), not a natural numeric scale.

```
Revenue ($K)

500 │ ██
400 │ ████
300 │ ██████
200 │ ████████
100 │ █████████████
    └────────────────────────
     Customers sorted by revenue →
```
Steep left-to-right drop-off reveals concentration in the top items.

### Pareto Analysis: Step-by-Step Procedure
1. Gather the output metric data for each individual entity (per customer, per SKU, etc.)
2. Sort from greatest to least
3. Compute the cumulative sum of both the count (number of entities) and the output metric
4. Convert sums to percentages if desired
5. Plot the cumulative sums as an X-Y chart

**When to use counts vs percentages on x-axis:** Use counts when they are more meaningful or when the total population size is unknown. Use percentages when the "80/20" framing is the key message.

**When to use columns vs lines:** Use a line chart when entity count is large (50+). Use columns when categories are few (<15) and each bar label matters.

### Cumulative Sum Line Overlay
Plotted on a secondary 0–100% axis. Rises steeply then flattens as low-value items are added.

```
Cumulative % of total revenue

100% │                     ╭────
 80% │              ╭──────╯
 60% │        ╭─────╯
 40% │   ╭────╯
 20% │───╯
  0% └──────────────────────────
      10%  30%  50%  70%  100%
      % of customers (ranked)
```
The "knee of the curve" marks where incremental customers add diminishing returns.

### Waterfall Chart (Building to a Total)
Starts at a base; each bar adds or subtracts en route to the final total.

```
Operating Profit ($M)

 50 │            ┌──┐
 40 │      ┌──┐  │//│
 30 │      │  │  │//│  ┌──┐
 20 │      │  │  │//│  │  │
 10 │ ┌──┐ │  │  │//│  │  │  ← Net
  0 └─┴──┴─┴──┴──┴──┴──┴──┴─
    Base  +A   -B   +C   Net
         (hatched = negative / cost)
```
Which categories add vs. subtract value en route to the final number.

### Reverse Waterfall ("Peel the Onion")
Waterfalls can work in reverse — starting from a total and breaking it down into constituent parts. Use when the audience cares about what's INSIDE a total, not what builds up to it.

Example: "Entire Market $1.1B → Fortune 1000 $792M (72%) → Top 4 verticals $271M (34% of Fortune 1000)"

---

## 4. Change Analysis

**What it analyzes:** How a variable moves over an ordered sequence — usually time, but sometimes tenure, deal count, or another proxy.

**Triggers — use when:**
- The hypothesis involves a trend continuing, reversing, or accelerating
- You want to show rate of change, not just level
- The x-axis has a meaningful order

**Data inputs required:**
- At least 6–8 data points to establish a reliable trend
- Consistent measurement intervals (monthly, quarterly, annually)
- A single outcome variable per chart

### Time Series Line Chart
Single line connecting observations in chronological order.

```
Revenue ($M)
120 │                 ╭──●
100 │           ╭──●──╯
 80 │      ╭──●─╯
 60 │ ●────╯
 40 │
    └────────────────────────
     Yr1    Yr2    Yr3    Yr4
```
Direction, velocity, and inflection points — the fundamental trend story.

### Trend Line with Derivative (Rate of Change)
Two panels: top = absolute level; bottom = period-over-period change.

```
Revenue ($M)                           (level)
120 │              ╭─────────●
 80 │    ╭─────────╯
 40 │●───╯
    Yr1    Yr2    Yr3    Yr4

Change vs. prior period ($M)      (derivative)
+40 │ ██
+30 │ ██  ██
+20 │ ██  ██  ██
+10 │ ██  ██  ██  ██
  0 └────────────────
    Yr1  Yr2  Yr3  Yr4
```
Whether growth is accelerating, steady, or slowing — even as totals keep rising.

### Non-Obvious Time Variable
X-axis is a proxy for time (e.g., sales rep tenure, customer age) rather than calendar date.

```
Avg deal size ($K)

200 │                          ●────●
150 │               ●────●────╯
100 │    ●────●────╯
 50 │●───╯
    └──────────────────────────────────
     Yr1   Yr2   Yr3   Yr4   Yr5   Yr6
              Rep tenure (years)
```
Maturation — not a calendar trend — drives the outcome. Reveals what to expect as the team ages.

---

## 5. Correlation Analysis

**What it analyzes:** The relationship (direction, strength, linearity) between two continuous variables.

**Triggers — use when:**
- You want to show that X is associated with Y
- You need to imply a threshold, demand curve, or optimal level
- You are diagnosing whether an input driver is producing the expected output

**Data inputs required:**
- Paired observations of both variables for each entity (n ≥ 15 preferred)
- Both variables measured on a consistent scale
- Enough variation in both axes for a pattern to be visible

### Scatter Plot (Linear Scale)
Each dot = one observation. Add a trend line when n ≥ 15.

```
Profit margin (%)

30 │                    ●    ●
20 │            ●   ●
10 │       ●●       ●
 0 │  ●  ●
   └──────────────────────────
    $1M    $5M   $10M   $20M
                Revenue
```
Direction (slope) and tightness (scatter around the line) of the relationship.

### Scatter Plot (Log Scale)
Both axes rescaled so equal distances = equal multipliers (10×, 100×). Use when range spans orders of magnitude.

```
Market cap (log $)

 $1B │                       ●  ●
$100M│           ●   ●   ●
 $10M│   ●  ●
     └──────────────────────────
       $1M     $10M    $100M
               Revenue (log $)
```
Whether the relationship holds across wide-range data — linear on a log scale = power law.

### Annotated Scatter (Labeled Data Points)
Individual dots labeled with entity names for identification of outliers.

```
R&D spend / revenue (%)

15 │  Comp A●
10 │              Comp B●    ●Comp C
 5 │  Comp D●  ●Comp E
 0 └──────────────────────────────
   Low          Med          High
              R&D productivity
```
Which specific entities are outliers and where each one sits relative to peers.

### Quadrant Overlay Technique
Overlay labeled quadrants on a scatter plot to create actionable decision zones. Each quadrant gets a specific action label (e.g., "Target for In-depth Analysis," "Lower Priority," "Review policy"). Use when the scatter data implies different actions at different positions.

---

## 6. Description Analysis

**What it analyzes:** Qualitative, mixed, or too-complex-to-chart information — fills gaps where hard numbers don't exist or would mislead.

**Triggers — use when:**
- Data is categorical or verbal (interview themes, feature presence/absence)
- A numeric chart would be too dense or falsely precise
- You are summarizing a landscape, not proving a causal relationship

**Data inputs required:**
- Structured qualitative data (interview notes, expert ratings, feature lists)
- A consistent set of criteria applied to all entities being compared
- Clear audience — description must be reader-appropriate, not raw

### Summary Table
Rows = entities; columns = attributes. Use when ≤ 8 columns and ≤ 12 rows.

```
┌─────────────┬──────────┬──────────┬──────────┬──────────┐
│             │  Attr 1  │  Attr 2  │  Attr 3  │  Attr 4  │
├─────────────┼──────────┼──────────┼──────────┼──────────┤
│ Company A   │   $12M   │   18%    │   High   │   Yes    │
│ Company B   │    $8M   │   22%    │   Low    │   No     │
│ Company C   │   $15M   │   14%    │   Med    │   Yes    │
└─────────────┴──────────┴──────────┴──────────┴──────────┘
```
Cross-entity comparison when too many metrics to represent in a single chart.

### Harvey Balls (Qualitative Scoring Grid)
● = full  ◕ = most  ◑ = half  ◔ = little  ○ = none

```
               Speed    Cost   Quality  Flexibility
Option A          ●       ◔       ●         ◑
Option B          ◑       ●       ◑         ●
Option C          ◔       ◑       ●         ◔
```
Trade-offs at a glance without false numeric precision.

### Benefits / Costs Matrix
Rows = options; columns = benefit or cost dimension. Cells = concise qualitative description.

```
┌─────────────┬──────────────────────┬──────────────────────┐
│             │ Benefits             │ Costs / Risks        │
├─────────────┼──────────────────────┼──────────────────────┤
│ Option A    │ Fast to market       │ High capex, low flex │
│ Option B    │ Low cost, scalable   │ 18-mo. build time    │
│ Option C    │ Flexibility, brand   │ Channel conflict     │
└─────────────┴──────────────────────┴──────────────────────┘
```
Structured comparison of trade-offs that can't be collapsed to a single number.

### Interview Data Summary (Representative Comments)
Themes extracted from interviews. n = respondents citing that theme.

```
Theme                            n    Representative Comment
────────────────────────────────────────────────────────────────
Pricing too high                  8   "We'd switch if cost dropped 20%"
Poor customer support             6   "Takes days to get a response"
Product missing key feature       5   "We need [X] to justify the price"
Satisfied, no plans to change     3   "It does what we need"
```
Which pain points dominate — without misrepresenting individual voices.

### Strategic Group Map (2-Axis Positioning)
Qualitative axes (e.g., price vs. scope). Circles = firms; size ≈ market share.

```
      High │  ●Comp A           ○Comp D
     Price │
           │          ●Comp B
      Low  │  ○Comp C       ○Comp E
           └─────────────────────────
            Narrow              Broad
                       Scope
```
Which strategic positions are crowded vs. vacant (white space = opportunity).

*See also: Factor Analysis Positioning (§ 12) — produces the same type of 2-axis positioning map from quantitative data rather than qualitative judgment.*

### Illustrative Charts
When real data is unavailable, draw the chart as it would look if the data existed. Label it clearly **ILLUSTRATIVE** so the audience knows it is directional, not measured.

```
Revenue vs. Market Share (ILLUSTRATIVE)

High │        ●
     │   ●        ●
     │        ●
Low  │  ●
     └──────────────────
      Low           High
           Market Share
```
Use ILLUSTRATIVE charts to make an argument visible before data collection — and to show what data would be needed to confirm it.

---

## 7. Essential Techniques

### Divide by Units

**What it analyzes:** Absolute totals that can't be compared across entities of different scale.

**Triggers — use when:**
- Comparing costs or revenues across organizations of different size
- Building a cost curve from individual data points
- "Bigger entity spends more" is true but uninformative

**Data inputs required:**
- The absolute metric (total cost, total revenue)
- A meaningful denominator (employees, units produced, customers, sq ft)

```
Before (raw totals)           After (per employee)
──────────────────────        ──────────────────────────
Division A: $10M cost         Division A: $100K/employee  ← efficient
Division B:  $3M cost         Division B: $150K/employee  ← expensive
(A looks worse on raw $)      (B revealed as the real cost problem)
```

### Normalize

**What it analyzes:** Variables with different baselines or unknown absolute values that need a common scale.

**Triggers — use when:**
- Base values differ across entities (different starting points hide relative change)
- You only know percentage changes, not absolute levels
- Building BCG-style matrices (share relative to leading competitor)

**Data inputs required:**
- Raw values for each entity across time or conditions
- A chosen reference point: mean, maximum, or baseline year

```
Before (raw)                    After (normalized to Yr1 = 1.00)
──────────────────────────      ──────────────────────────────────
Co A:  500 → 550 → 620          Co A: 1.00 → 1.10 → 1.24
Co B:   20 →  24 →  30          Co B: 1.00 → 1.20 → 1.50  ← faster growth
(scale gap hides Co B's pace)   (relative growth now directly comparable)
```

### Cross-Technique Note
Some analyses span categories. A cost curve built from quarterly observations is both "divide by units" (cost per unit) and "change" (progression over time). The experience/learning curve — where costs fall by a predictable percentage with every doubling of volume — is a classic cross-technique analysis.

### When to Use Tables vs Charts
Tables are better when:
- A chart would be too busy for ease of interpretation
- You need to show many metrics across a few entities (>5 columns of data)
- Precise values matter more than visual patterns

Charts are better when:
- You want to show trends, comparisons, or distributions
- The visual pattern IS the insight
- One or two metrics are the focus

---

## 8. Output-Based Modeling

**What it analyzes:** Expected financial outcomes under different assumption sets — bridges analysis to dollar-denominated recommendations.

**Triggers — use when:**
- A recommendation requires a quantified impact estimate
- Multiple scenarios (optimistic / base / pessimistic) should be shown side by side
- Assumptions need to be explicit and challengeable by the client

**Data inputs required:**
- Volume drivers (customers, units, deals) with growth rates
- Pricing with growth rates
- Variable costs per unit (COGS, marketing, logistics)
- Fixed costs (R&D, salaries, facilities) with growth rates
- Tax rate

### 3-Scenario Impact Model (Low / Base / High)

```
                       Low        Base       High
───────────────────────────────────────────────────
Customers (Yr 3)        800       1,200      1,800
Avg Revenue / Cust       $80        $100       $110
───────────────────────────────────────────────────
Gross Revenue           $64K       $120K      $198K
Variable Costs          $32K        $54K       $89K
Gross Profit            $32K        $66K      $109K
Fixed Costs             $40K        $40K       $40K
Operating Profit        -$8K        $26K       $69K
───────────────────────────────────────────────────
```
Range of outcomes and which assumptions drive the spread between Low and High.

### Acquisition / Valuation Modeling
Same 3-scenario structure applied to an acquisition target. Add: purchase price, synergies, integration costs, payback period.

See `references/impact-modeling.md` for the full template and formula structure.

### Three Ways Acquisitions Pay
Only three mechanisms create value in an acquisition:
1. **Multiple arbitrage** — buying at a lower valuation multiple than the acquirer trades at
2. **Cost synergy** — eliminating redundant costs by combining operations
3. **Cross-sell** — selling the acquirer's products to the target's customers (or vice versa)

If none of these three mechanisms apply with quantifiable evidence, the acquisition does not have a defensible value creation thesis.

---

## 9. Advanced Methods (Brief Reference)

Specialized and infrequent. No full ASCII charts — use references below to decide whether to engage.

### Factor Analysis
**What it analyzes:** Reduces many correlated attributes to a small number of underlying dimensions.
**Triggers:** Positioning or differentiation analysis; revealing hidden structure in analyst ratings or survey data.
**Data inputs:** Matrix of ratings (entities × attributes); typically 10+ attributes and 20+ entities.
*See § 12 for the full Factor Analysis Positioning methodology with worked examples and implementation guidance.*

### Bertrand Pricing Analysis
**What it analyzes:** Optimal pricing under competitive response assumptions.
**Triggers:** Pricing decision where competitor cost structures are known or estimable.
**Data inputs:** Own cost structure, competitor cost estimates, demand elasticity, market share data.
**Practical procedure:** Derive competitor reaction functions from win-loss survey data. Survey customers who evaluated both products, then derive demand functions and use Bertrand pricing theory to compute optimal pricing response.

### Discriminant Analysis
**What it analyzes:** Which factors best separate two or more pre-defined groups (e.g., won vs. lost deals).
**Triggers:** Adaptive pricing, targeting, or classifying entities into categories.
**Data inputs:** Labeled group membership + multiple predictor variables per observation.
**Three-Step Adaptive Pricing Procedure:**
1. Identify key customer and competitive characteristics; record for every sales opportunity; note wins and losses
2. Establish a desirable win percentage threshold that maximizes revenue (or profit)
3. Given characteristics of a new deal, adjust price to hit the win percentage threshold

Key predictors: product, price, partner type, competitor, deal size, vertical, region, deal type.

### Segmented Regression
**What it analyzes:** Trend lines or demand curves that have a structural break at an intervention point.
**Triggers:** Before/after a policy change, price intervention, or natural experiment.
**Data inputs:** Time series with a known breakpoint date; sufficient observations on both sides.
**Elasticity Calculation:** If a price increase of X% produces a volume decline of Y% (measured from the pre-intervention trajectory), then elasticity = Y/X. The pre-intervention trajectory is the regression line fitted to data before the price change, extended forward.

### Analysis of Variance (ANOVA)
**What it analyzes:** Whether group means differ more than expected by chance — tests factor importance.
**Triggers:** Determining whether a treatment, segment, or intervention explains outcome differences.
**Data inputs:** Outcome variable + categorical group labels; at least 3 groups recommended.
**Interpretation Rule:** When the confidence interval includes zero, no statistically significant effect was present. Shade or flag results where the interval excludes zero — these are the factors that matter.

---

> This framework covers approximately 20% of analysis types that address 70–80% of hypothesis tests in strategic analysis. Strive for creativity beyond these templates when the situation calls for it.

---

## 10. Strategic Group Mapping

**What it analyzes:** Competitive terrain by plotting firms on two differentiating strategic dimensions.

**Triggers — use when:**
- Many competitors and the student needs to see the big picture
- Asking "who are our real competitors?" (group membership answers this)
- Entry strategy — where to enter and how to move between positions
- Understanding why certain firms face more intense competition

**Data inputs required:**
- Key strategic dimensions that differentiate firms in the industry
- Firm positions on those dimensions
- Revenue or market share data for circle sizing

### Definition

A strategic group is a set of firms within an industry that follow similar strategies along key strategic dimensions. Strategic group maps visualize the competitive terrain by plotting firms on two differentiating axes.

### Methodology (3 Steps)

1. **Identify differentiating factors** — determine which strategic dimensions most sharply separate firms in the industry (e.g., price vs. geographic scope, breadth of product line vs. degree of vertical integration, technology level vs. channel strategy)
2. **Plot firms on two axes** — choose the two most differentiating dimensions as axes. Position each firm according to its strategy on those dimensions.
3. **Size circles by revenue or profit** — each firm or group is represented by a circle whose area reflects revenue, market share, or profitability. Add annotations for growth rates, strategic direction, or other relevant metadata.

### Key Insight: Intra-Group Rivalry

Rivalry within a strategic group can be more intense than rivalry across groups. Variance in profitability within a group often exceeds variance across groups. Firms competing in the same strategic space fight hardest against each other because they target the same buyers with similar value propositions.

### Mobility Barriers and Steppingstones

Strategic groups persist because mobility barriers make it costly to move from one group to another. These barriers arise from entrenched differentiation (high K): switching groups requires changing many interdependent strategic choices simultaneously.

However, groups can serve as steppingstones — a firm may enter one group to build capabilities and then move toward a more attractive group over time. The map reveals which transitions are plausible (adjacent groups with lower barriers) versus impractical (distant groups requiring radical reconfiguration).

### Worked Examples

- **Retail Jewelry:** groups separated by price point and channel (e.g., luxury boutique vs. mall chain vs. online discount). Mobility barriers between luxury and discount segments are high due to brand positioning, supplier relationships, and customer expectations.
- **Systems Management Software:** groups separated by breadth of platform support and depth of management features. Shows clustering in mid-market with open space in specialized niches.
- **MX Open Finance:** groups separated by integration depth and customer segment focus. Reveals positioning relative to competitors in the open finance ecosystem.

### Source Citations

- Thompson, A. & Strickland, A. J. *Strategic Management*.

**Offer prompt:** "Should we map where competitors cluster and where open space exists?"

---

## 11. Strategy Canvas Analysis

**What it analyzes:** How an industry competes and invests across the factors that matter to buyers, revealing over-investment and white space.

**Triggers — use when:**
- Comparing specific value propositions side by side
- Trying to find over-investment areas or unmet buyer needs
- A visual showing all competitors' value curves would clarify the discussion
- Working on a specific recommendation and needs to show how it changes the value curve

**Data inputs required:**
- All buyer-relevant features and competing factors in the industry
- Competitor performance ratings on each factor (low to high)

### Definition

The strategy canvas is a one-page visual that captures the current competitive landscape and the firm's relative value proposition. It shows how an industry competes and invests across the factors that matter to buyers.

### Methodology (4 Steps)

1. **Identify all buyer-relevant features** — list every factor buyers consider when choosing between offerings (price, speed, reliability, brand prestige, convenience, features, service quality, etc.)
2. **Array factors on the horizontal axis** — spread them across the x-axis
3. **Plot competitor performance** — for each competitor, mark performance level (low to high) on each factor, then connect the dots to form a value curve
4. **Sort to highlight strengths and weaknesses** — reorder factors so that patterns become visible: where competitors cluster, where they diverge, where one firm dominates

### Benefits

- Makes implicit competitive dynamics explicit and visual
- Reveals over-investment (factors where all firms compete intensely but buyers don't value proportionally)
- Identifies divergence opportunities (where a firm could break away)
- Shows competitive convergence (industries where everyone looks the same — a red ocean signal)

### Worked Examples

- **Southwest Airlines:** value curve diverges sharply from traditional carriers. Low on meals, lounges, seating choice, connections. High on price (low), frequency, speed, friendly service. Reveals that Southwest competes on a fundamentally different set of factors.
- **BYU Dining Options:** comparing on-campus dining venues across factors like price, speed, variety, ambiance, healthiness, convenience. Shows clustering among fast-casual options and open space in certain attribute combinations.
- **Systems Management Software:** comparing enterprise vendors across platform breadth, automation depth, ease of deployment, price, integration capabilities. Highlights where market leaders over-invest and where challengers differentiate.

### Source Citations

- Kim, W. C. & Mauborgne, R. (2002). "Charting Your Company's Future." *Harvard Business Review*.
- Kim, W. C. & Mauborgne, R. *Blue Ocean Strategy*.

**Offer prompt:** "Would you like to draw a strategy canvas to see where competitors cluster and where the value curve could diverge?"

---

## 12. Factor Analysis Positioning

**What it analyzes:** Many competitive attributes collapsed into 2-3 underlying dimensions via statistical dimensionality reduction, revealing positioning patterns invisible to inspection.

**Triggers — use when:**
- Too many attributes for a simple two-axis map
- Quantitative rigor needed to support positioning claims
- Competitive landscape is complex with many players and dimensions
- Need to identify underlying dimensions that truly differentiate competitors

**Data inputs required:**
- Matrix of ratings (entities x attributes); typically 10+ attributes and 20+ entities
- Consistent scoring scale across all attributes

### Definition

Factor analysis positioning is the quantitative version of strategic group maps. It uses statistical dimensionality reduction to collapse many competitive attributes into 2-3 underlying factors, then plots firms in that reduced space to reveal positioning patterns invisible to the naked eye.

### Methodology (5 Steps)

1. **Score firms on attributes** — rate each competitor on every relevant competitive attribute (e.g., 1-10 scale). Collect enough attributes to capture the full competitive picture.
2. **Compute correlation matrix** — identify which attributes move together (correlated attributes likely reflect the same underlying strategic dimension).
3. **Extract factors via PCA / varimax rotation** — Principal Component Analysis extracts the underlying dimensions. Varimax rotation makes factors more interpretable by maximizing the loading of each attribute on one factor.
4. **Interpret and name factors** — examine which attributes load heavily on each factor. Name the factor based on what those attributes have in common (e.g., "Premium Experience" if brand prestige, service quality, and price all load together).
5. **Compute factor scores and plot positions** — calculate each firm's score on each factor, then plot firms on a 2D (or 3D) positioning map.

### Interpretation Rules

- **Loadings > |0.75|** define each factor's meaning — these attributes are strongly associated with that dimension
- **Proximity** on the map = similar positioning (firms competing head-to-head)
- **Distance** on the map = differentiation (firms with distinct strategic profiles)
- **Quadrant** = type of advantage (each quadrant represents a different combination of the underlying factors)

### Python and R Approaches

**Python:** Use `sklearn.decomposition.PCA` or `factor_analyzer` library. Steps: standardize data -> fit PCA -> extract loadings -> rotate (varimax) -> compute scores -> plot with matplotlib/seaborn.

**R:** Use `factanal()` or `psych::fa()`. Steps: standardize data -> run factor analysis with varimax rotation -> examine loadings -> compute scores -> plot with ggplot2.

Both approaches yield the same strategic insights — choice depends on team familiarity.

### Worked Examples

- **Smartphone Positioning (2011):** Factor analysis of smartphone competitors across attributes like screen size, app ecosystem, price, camera quality, enterprise features, ease of use. Reveals underlying dimensions (e.g., "Consumer Experience" vs. "Enterprise Capability") and shows how Apple, BlackBerry, Samsung, HTC, and Nokia occupied distinct positions. BlackBerry's position in the enterprise quadrant became vulnerable as consumer-oriented competitors added enterprise features.
- **Enterprise Client Management:** Positioning of CRM and client management vendors across integration depth, customization, price, scalability, ease of use. Factor analysis reveals two underlying dimensions separating enterprise-grade platforms from SMB-focused tools.
- **Enterprise Mobile Management:** Positioning of MDM/EMM vendors. Factor analysis collapses security features, device support breadth, deployment complexity, and cost into interpretable dimensions showing competitive clusters and white space.

### Source Citations

- Forrester Research (methodology reference for technology positioning maps).

**Offer prompt:** "There are a lot of attributes in play. Would a positioning analysis help simplify the competitive picture?"
