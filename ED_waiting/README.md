# Emergency Department Wait Time Dashboard
## README — Project Documentation

**Project:** ED Patient Wait Time Analysis
**Period:** November 1, 2025 – January 28, 2026 (3 months)

---

## 1. Background and Problem Statement

Patients visiting the Emergency Department (ED) have submitted complaints about excessively long waiting times before being seen by a clinician. This project analyses 3 months of de-identified ED visit records to:

1. Quantify how frequently the department is missing its triage-based wait time targets.
2. Identify which patient severity groups and operational shifts are underperforming.
3. Present findings to two different audiences — executive leadership and the quality development team — in formats appropriate to each audience's decision-making needs.

---

## 2. Dataset Description

| Field | Description |
|---|---|
| `Patient_ID` | De-identified unique patient identifier *(from dataset)* |
| `Visit_Date` | Date of ED visit (DD/MM/YYYY) *(from dataset)* |
| `Shift` | Operational shift: Morning / Afternoon / Night *(from dataset)* |
| `Emergency Severity Index (ESI)` | Triage level assigned at arrival (1 = most severe, 5 = least severe) *(from dataset)* |
| `Waiting_Time_Minutes` | Minutes from arrival to first clinician contact *(from dataset)* |
| `within_target` | Boolean: TRUE if wait time ≤ ESI target, FALSE otherwise *(derived field — created by author)* |
| `target` | Target wait time in minutes based on ESI level *(derived field — created by author)* |

**Total records:** 6,530 visits
**No missing values** in any field.

---

## 3. ESI Triage Levels and Target Wait Times

The Emergency Severity Index (ESI) is a 5-level triage system used to prioritise patients by clinical urgency. Each level carries a benchmark wait time target:

| Level | Category | Target Time | Clinical Description |
|---|---|---|---|
| ESI 1 | Resuscitation | ≤ 1 minute | Immediate life-threatening intervention required (e.g., cardiac arrest, major trauma) |
| ESI 2 | Emergent | ≤ 10 minutes | High-risk situation, severe pain or distress (e.g., stroke, chest pain) |
| ESI 3 | Urgent | ≤ 30 minutes | Stable vitals but requires multiple resources (labs, imaging) |
| ESI 4 | Less Urgent | ≤ 60 minutes | Stable, requires one simple resource (e.g., suture) |
| ESI 5 | Non-Urgent | ≤ 120 minutes | Stable, no diagnostic resources needed (e.g., prescription refill) |

---

## 4. Descriptive Statistics

### 4.1 Overall Summary

| Metric | Value |
|---|---|
| Total visits | 6,530 |
| Visits within target | 4,153 (63.6%) |
| Visits exceeding target | 2,377 (36.4%) |
| Average wait time (all patients) | 55.5 minutes |
| Average target time (all patients) | 46.0 minutes |
| Observation period | 89 days (Nov 1, 2025 – Jan 28, 2026) |
| Average daily visits | ~73 patients/day (84 of 89 days have recorded visits) |

### 4.2 Compliance by ESI Level

| ESI | Category | n | Within Target | Compliance | Avg Wait | Median Wait | Target |
|---|---|---|---|---|---|---|---|
| 1 | Resuscitation | 420 | 420 | **100.0%** | 0.5 min | 0 min | 1 min |
| 2 | Emergent | 1,022 | 1,022 | **100.0%** | 2.0 min | 2 min | 10 min |
| 3 | Urgent | 2,546 | 2,107 | **82.8%** | 31.1 min | 15 min | 30 min |
| 4 | Less Urgent | 1,526 | 184 | **12.1%** | 95.4 min | 89 min | 60 min |
| 5 | Non-Urgent | 1,016 | 420 | **41.3%** | 133.2 min | 128 min | 120 min |

> **Key finding:** ESI 1 and 2 (life-threatening cases, n = 1,442) are 100% compliant — the critical safety pathway is intact. ESI 4 is the most severely underperforming group, with 88% of patients waiting beyond their 60-minute target. When ESI 3 patients breach their target, they wait a median of 80+ extra minutes beyond the 30-minute threshold.

### 4.3 Compliance by Shift

| Shift | n | Within Target | Compliance |
|---|---|---|---|
| Morning | 2,112 | 1,413 | 66.9% |
| Afternoon | 2,817 | 1,649 | 58.5% |
| Night | 1,601 | 1,091 | 68.1% |

> **Key finding:** Afternoon is the highest-volume shift and the worst-performing. It handles 43% of all visits but achieves the lowest compliance rate.

### 4.4 Compliance by ESI × Shift (Breach Rate)

| | Morning | Afternoon | Night |
|---|---|---|---|
| **ESI 1** | 0% | 0% | 0% |
| **ESI 2** | 0% | 0% | 0% |
| **ESI 3** | 18.3% | 16.0% | 18.3% |
| **ESI 4** | 75.0% | **98.8%** | 86.1% |
| **ESI 5** | 46.6% | 72.7% | 49.8% |

> **Critical cell:** ESI 4 × Afternoon has a 98.8% breach rate — effectively, every ESI 4 patient arriving in the afternoon exceeds the 60-minute target.

### 4.5 Day-of-Week Pattern

| Day | Compliance |
|---|---|
| Mon | 65.9% |
| Tue | 62.9% |
| Wed | 64.7% |
| Thu | 62.9% |
| Fri | 65.6% |
| **Sat** | **61.8%** |
| **Sun** | **61.7%** |

> Weekends show slightly lower compliance, suggesting weekend staffing may need review.

### 4.6 Trend Over Time

Weekly compliance rates ranged from 60.7% to 67.5% across 14 weeks with no sustained improvement. The trend is flat, indicating that the problem is structural and has not self-corrected.

---

## 5. Dashboard 1 — Executive Team

**Audience:** Hospital director, medical director, COO/CMO
**Purpose:** Strategic awareness, accountability, risk identification
**Design principle:** One screen, five to six elements, clear narrative flow

### Chart Rationale

#### 5.1 KPI Cards (4 tiles)
**Charts used:** Headline number tiles with colour-coded top borders

**Why:** Executives scan numbers before charts. Four tiles deliver the four most decision-relevant facts at a glance — overall compliance rate (strategic health), total visits (volume context), ESI 1–2 safety status (patient safety assurance), and ESI 4 compliance (critical problem severity). Colour-coding (green/amber/red) communicates pass/fail without requiring the reader to interpret a scale.

#### 5.2 Weekly Compliance Trend (Line Chart)
**Charts used:** Line chart with area fill and reference line at 80%

**Why:** A line chart is the standard form for showing change over time. It answers the most important strategic question — "Is this getting better or worse?" — without ambiguity. The reference line at 80% gives a clear goal. An area fill adds visual weight to the current performance level without adding data. A bar chart would be noisier and harder to read for 14 weeks of data.

#### 5.3 Compliance by ESI Level (Horizontal Bar Chart)
**Charts used:** Horizontal bar chart with colour-coded bars and patient count labels

**Why:** A horizontal bar chart is ideal for comparing a single metric across a small set of named categories where the category labels need room. ESI levels (1–5) are ordered and named, making position on a shared axis immediately readable. The colour coding (green for compliant, amber for borderline, red for failing) adds a second encoding channel so the story reads even before the numbers. A pie or donut chart would make proportional comparison impossible and hide the actual compliance values.

#### 5.4 Volume and Compliance by Shift (Grouped Bar Chart)
**Charts used:** Stacked appearance — faded full bar (total volume) with solid inner bar (within-target volume), compliance % labelled inside

**Why:** The key insight here is not just compliance rate but the combination of volume and compliance. Afternoon has the worst compliance AND the highest volume — a double burden that a simple compliance bar would understate. Showing total volume as a faded bar behind the within-target portion lets the reader see both dimensions in one chart without a dual-axis (which is always misleading). The compliance % is labelled inside the solid bar to avoid collision with any element above.

#### 5.5 Key Findings Box (Structured Text Panel)
**Charts used:** Three-column text panel with colour-coded section headers

**Why:** Charts communicate patterns; text communicates meaning. After four data charts, the executive needs a concise narrative that explicitly names what is safe, what needs attention, and what is a critical priority. This panel removes the burden of interpretation and provides the language the executive needs to brief their board or take action. It is not a replacement for the charts — it is a synthesis layer above them.

---

## 6. Dashboard 2 — Quality Development Team

**Audience:** Charge nurses, QI officers, ER operations managers
**Purpose:** Root-cause analysis, operational diagnosis, intervention design
**Design principle:** Dense but navigable; reveals not just where but how much and why

### Chart Rationale

#### 6.1 ESI × Shift Breach Rate Heatmap
**Charts used:** Grid table with colour-interpolated cells (red = high breach, green = low breach)

**Why:** The heatmap is the single most operationally useful chart in this dashboard. It simultaneously shows all 15 combinations of ESI level and shift, with colour encoding breach rate across a continuous scale. The QD team can immediately identify the worst-performing cell (ESI 4 × Afternoon, 98.8%) and see the surrounding pattern — does the problem exist across all shifts for ESI 4, or only in Afternoon? A bar chart would require 15 separate bars and lose the two-dimensional structure. A heatmap is the correct form when the insight lives at the intersection of two categorical variables.

#### 6.2 Wait Time Distribution by ESI (Box Plot)
**Charts used:** Box plot for ESI 3, 4, and 5 — with IQR box, 10th–90th percentile whiskers, and target line overlay

**Why:** Compliance rate tells you how many patients missed the target but not by how much or with what spread. A box plot shows the median, the spread of the middle 50% of patients (IQR), and the extent of outliers — all in one mark. For ESI 4, the entire IQR (72–107 minutes) sits above the 60-minute target, meaning the breach is systemic rather than driven by outliers. A bar chart of average wait would obscure this. ESI 1 and 2 are excluded because they are 100% compliant; including them would compress the scale and hide the detail in ESI 3–5.

#### 6.3 Monthly Compliance Trend by ESI (Multi-Series Line Chart)
**Charts used:** Line chart with one line per ESI level (3, 4, 5)

**Why:** A multi-series line chart tracks whether compliance is improving, stable, or deteriorating over time for each ESI level independently. If ESI 4 were improving while ESI 3 worsened, the chart would reveal that immediately. In our data, all three ESI levels are essentially flat across three months — a finding that rules out seasonal or random variation and points to a structural cause. A faceted bar chart would make this comparison harder. ESI 1 and 2 are excluded because they are 100% compliant at all times and would compress the y-axis scale, obscuring the variation in ESI 3–5.

#### 6.4 Compliance by Day of Week (Bar Chart)
**Charts used:** Vertical bar chart with weekend bars highlighted in a distinct colour

**Why:** A bar chart is the correct form for comparing a single metric across an ordered categorical axis (Monday through Sunday). The ordered x-axis preserves the weekly rhythm, so patterns like weekend drops are immediately visible. Weekends (Saturday and Sunday) are highlighted in a distinct colour to make the staffing implication salient without requiring text annotation. A line chart would imply continuity between days, which is misleading for categorical weekday data.

#### 6.5 Average Excess Minutes by ESI + Shift (Horizontal Bar Chart)
**Charts used:** Horizontal bar chart sorted by descending excess minutes, colour-coded by ESI level

**Why:** Compliance rate answers "did they miss the target?" but not "by how much?" A patient who waits 31 minutes for an ESI 3 (1 minute over) is a very different problem from one who waits 120 minutes (90 minutes over). This chart shows the average number of minutes over target for breaching patients in each ESI × shift group. Sorting by descending excess makes it a prioritisation tool — the longest bars represent the combinations that would benefit most from intervention. ESI 3 breaches appear at the top of the chart despite lower breach rates, because when ESI 3 patients do breach, they tend to wait extremely long (median excess 99 minutes).

---

## 7. Files

| File | Description |
|---|---|
| `ed_visits.csv` | Source data (de-identified, 6,530 rows) |
| `ED_Executive_Dashboard.html` | Standalone executive dashboard — open in any browser |
| `ED_QualityDev_Dashboard.html` | Standalone QD dashboard — open in any browser |
| `ED_Executive_Dashboard.pdf` | Single-page PDF export of executive dashboard |
| `ED_QualityDev_Dashboard.pdf` | Single-page PDF export of QD dashboard |
| `README.md` | This document |

---

## 8. Technical Notes

- All charts are built with vanilla HTML5 Canvas and CSS — no external libraries required. The HTML files are fully self-contained and work offline.
- PDF exports were generated using Playwright with Chromium, rendered at 1400px viewport width to preserve layout fidelity.
- The `within_target` and `target` fields were derived by the author: `within_target` compares `Waiting_Time_Minutes` against the ESI-specific `target` threshold; they are not present in the original source data.
- ESI 1 and ESI 2 patients are excluded from box plots and monthly trend charts because 100% compliance collapses the useful scale range for the other levels.

---

