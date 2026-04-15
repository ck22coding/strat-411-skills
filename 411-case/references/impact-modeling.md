# Impact Modeling Template

## Table of Contents
1. Model Structure Overview
2. Assumptions Sheet
3. Revenue Model
4. Cost Model
5. Profitability Analysis
6. Scenario Comparison

---

## 1. Model Structure Overview

A 3-scenario financial impact model with 5 interconnected sheets:
- **Assumptions** → drives all calculations
- **Revenue Model** → customers × price across 5 years
- **Cost Model** → fixed + variable costs across 5 years
- **Profitability Analysis** → P&L for each scenario
- **Scenario Comparison** → side-by-side comparison

Each sheet computes for three scenarios: **Base Case**, **Optimistic Case**, **Pessimistic Case**.

---

## 2. Assumptions Sheet

All model inputs are centralized here. This makes it easy to adjust a single assumption and see the cascading impact.

### Customer Assumptions
| Assumption | Base | Optimistic | Pessimistic |
|---|---|---|---|
| Initial New Customers | 100,000 | 120,000 | 100,000 |
| Initial Existing Customers | 50,000 | 60,000 | 40,000 |
| New Customer Growth Rate | 10% | 15% | 5% |
| Existing Customer Growth Rate | 5% | 8% | 2% |

### Pricing Assumptions
| Assumption | Base | Optimistic | Pessimistic |
|---|---|---|---|
| Initial Average Price | $700 | $700 | $700 |
| Price Growth Rate | 2% | 3% | 0% |

### Variable Cost Assumptions (per unit)
| Assumption | Base | Optimistic | Pessimistic |
|---|---|---|---|
| Manufacturing | $250 | $230 | $280 |
| Marketing | $50 | $40 | $60 |
| Logistics | $20 | $18 | $25 |

### Fixed Cost Assumptions
| Assumption | Base | Optimistic | Pessimistic |
|---|---|---|---|
| Initial R&D | $5M | $6M | $4M |
| R&D Growth Rate | 5% | 8% | 0% |
| Initial Salaries | $2M | $2.5M | $1.5M |
| Salaries Growth Rate | 5% | 10% | 2% |
| Initial Facilities | $1M | $1.2M | $0.8M |
| Facilities Growth Rate | 2% | 5% | 0% |

### Other
| Assumption | Base | Optimistic | Pessimistic |
|---|---|---|---|
| Tax Rate | 25% | 25% | 25% |

*Note: Model assumes one unit purchased per customer during the period modeled.*

---

## 3. Revenue Model

For each scenario and each year (1-5):

```
New Customers[year] = New Customers[year-1] × (1 + New Customer Growth Rate)
Existing Customers[year] = Existing Customers[year-1] × (1 + Existing Customer Growth Rate)
Total Customers = New Customers + Existing Customers
Average Price[year] = Average Price[year-1] × (1 + Price Growth Rate)
Revenue = Total Customers × Average Price
```

---

## 4. Cost Model

### Fixed Costs
Each fixed cost category grows at its own rate:
```
R&D[year] = R&D[year-1] × (1 + R&D Growth Rate)
Salaries[year] = Salaries[year-1] × (1 + Salaries Growth Rate)
Facilities[year] = Facilities[year-1] × (1 + Facilities Growth Rate)
Total Fixed = R&D + Salaries + Facilities
```

### Variable Costs
Scale with total customers (volume):
```
Manufacturing = Total Customers × Manufacturing Cost per Unit
Marketing = Total Customers × Marketing Cost per Unit
Logistics = Total Customers × Logistics Cost per Unit
Total Variable = Manufacturing + Marketing + Logistics
```

---

## 5. Profitability Analysis

For each scenario:
```
Revenue (from Revenue Model)
- Variable Costs (from Cost Model)
= Gross Profit
  Gross Margin = Gross Profit / Revenue

Gross Profit
- Fixed Costs (from Cost Model)
= Operating Profit
  Operating Margin = Operating Profit / Revenue

Net Profit = Operating Profit × (1 - Tax Rate)
```

---

## 6. Scenario Comparison

Side-by-side view across all 5 years:
- Revenue: Base vs. Optimistic vs. Pessimistic
- Operating Profit: Base vs. Optimistic vs. Pessimistic
- Operating Margin: Base vs. Optimistic vs. Pessimistic
- Net Profit: Base vs. Optimistic vs. Pessimistic

### How to Use This Template
1. Start with the Assumptions sheet — customize for your case
2. The Revenue, Cost, and Profitability sheets auto-calculate
3. Use Scenario Comparison to identify the range of outcomes
4. Present the range with a recommendation based on the most likely scenario
5. Highlight which assumptions most sensitively affect the outcome (sensitivity analysis)
