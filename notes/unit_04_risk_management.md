# Unit 04: Risk Management

> **Hours:** 4 Hrs. | **Source:** `Chapter_4_Risk Management.pdf`

---

## Table of Contents

- [1. Introduction to Risk Management](#1-introduction-to-risk-management)
  - [Characteristics of Risk](#characteristics-of-risk)
- [2. Types of Risk](#2-types-of-risk)
- [3. Risk Appetite, Tolerance, and Threshold](#3-risk-appetite-tolerance-and-threshold)
- [4. Plan Risk Management](#4-plan-risk-management)
  - [Elements of Plan Risk Management](#elements-of-plan-risk-management)
- [5. Risk Identification](#5-risk-identification)
  - [Risk Identification Techniques](#risk-identification-techniques)
  - [Common Software Project Risks](#common-software-project-risks)
- [6. Risk Register](#6-risk-register)
  - [Contents of Risk Register](#contents-of-risk-register)
- [7. Risk Analysis](#7-risk-analysis)
  - [Steps in Risk Analysis](#steps-in-risk-analysis)
  - [Risk Table](#risk-table)
  - [Probability and Impact Matrix](#probability-and-impact-matrix)
- [8. Qualitative Risk Analysis](#8-qualitative-risk-analysis)
  - [Three Functions of Qualitative Risk Analysis](#three-functions-of-qualitative-risk-analysis)
- [9. Quantitative Risk Analysis](#9-quantitative-risk-analysis)
- [10. Risk Response (Avoidance & Mitigation)](#10-risk-response-avoidance-mitigation)
  - [Risk Avoidance](#risk-avoidance)
  - [Risk Mitigation](#risk-mitigation)
- [11. Risk Monitoring and Control](#11-risk-monitoring-and-control)
  - [Risk Monitoring](#risk-monitoring)
  - [Risk Control](#risk-control)
- [12. Risk Management Process](#12-risk-management-process)
  - [Six Processes of Risk Management](#six-processes-of-risk-management)
- [13. PERT Numerical Example](#13-pert-numerical-example)
  - [Step 1: Project Variance and Standard Deviation](#step-1-project-variance-and-standard-deviation)
  - [Step 2: Compute Project Variance and Standard Deviation](#step-2-compute-project-variance-and-standard-deviation)
  - [Step 3: Probability of Completing 5 Days Early](#step-3-probability-of-completing-5-days-early)
  - [Step 4: Project Duration for 95% Confidence Level](#step-4-project-duration-for-95-confidence-level)
- [14. Quick Revision Summary](#14-quick-revision-summary)
  - [Key Formulas](#key-formulas)
  - [Decision Rules](#decision-rules)
  - [PERT Example Quick Reference](#pert-example-quick-reference)

---

## 1. Introduction to Risk Management

> **Definition — Risk:** An uncertain event that, if it occurs, affects project objectives (scope, schedule, cost, quality). — *PMI*

**Key Characteristics:**

- **Uncertainty:** The event may or may not happen
- **Impact:** If it occurs, it affects project objectives
- **Probability:** Can be expressed as a likelihood (0-100%)

> **⚠️ Important:** Risks are **not** the same as *issues*. Issues are things you know you'll have to deal with, and may even have an idea of when they'll occur, like a team member's scheduled vacation, or a big spike in product demand around the holidays. Risks are events that *might* happen, and you may not be able to tell *when*.

> **Definition — Issue:** A problem that has already happened or is certain to happen — unlike risks, issues are certain and must be addressed immediately.

**Risk vs Issue:**

| Aspect | Risk | Issue |
|--------|------|-------|
| Timing | Future event | Present or certain future |
| Certainty | Uncertain (may or may not happen) | Certain (will definitely happen) |
| Action | Plan and prepare (proactive) | Address and resolve (reactive) |

### Characteristics of Risk

Risk is an uncertainty which is associated with a future and may or may not occur and a corresponding potential for loss. Two main characteristics of risk are:

1. **Uncertainty:** The risk may or may not happen — there are no 100% risks.
2. **Loss:** If risks become a reality, then losses occur.

---

## 2. Types of Risk

| Risk Type | Description |
|---|---|
| **Cost Risk** | Escalation of project costs due to poor cost estimating accuracy and scope creep. |
| **Schedule Risk** | The risk that activities will take longer than expected. Slippages in schedule typically increase costs and delay the receipt of project benefits, with a possible loss of competitive advantage. |
| **Performance Risk** | The risk that the project will fail to produce results consistent with project specifications. |
| **Governance Risk** | Relates to board and management performance with regard to ethics, community stewardship, and company reputation. |
| **Strategic Risks** | Result from errors in strategy, such as choosing a technology that can't be made to work. |
| **Operational Risk** | Includes risks from poor implementation and process problems such as procurement, production, and distribution. |
| **Market Risks** | Include competition, foreign exchange, commodity markets, and interest rate risk, as well as liquidity and credit risks. |
| **Legal Risks** | Arise from legal and regulatory obligations, including contract risks and litigation brought against the organization. |
| **External Hazards** | Include storms, floods, and earthquakes; vandalism, sabotage, and terrorism; labor strikes; and civil unrest. |

---

## 3. Risk Appetite, Tolerance, and Threshold

Organizations perceive risk as the effect of uncertainty on projects and organizational objectives. Organizations and stakeholders are willing to accept varying degrees of risk depending on their risk attitude.

The risk attitudes may be influenced by a number of factors, which are broadly classified into three themes:

| Concept | Definition | Example |
|---------|------------|---------|
| **Risk Appetite** | How much risk an organization is willing to take on to achieve its goals (strategic level) | "We're willing to accept up to 30% cost overrun for innovation" |
| **Risk Tolerance** | How much variation an organization can withstand for a specific objective (project level) | "We can tolerate schedule delays of up to 2 weeks" |
| **Risk Threshold** | The exact point at which a risk becomes unacceptable; triggers action | "If cost exceeds Rs. 50,000, we must escalate" |

---

## 4. Plan Risk Management

> **Definition:** **Plan Risk Management** is the process of defining how risk management activities will be conducted — establishing methodology, roles, budget, timing, and risk categories.

The risk management plan is vital to communicate with and obtain agreement and support from all stakeholders to ensure the risk management process is supported and performed effectively over the project life cycle. Careful and explicit planning enhances the probability of success for other risk management processes. It is important to provide sufficient resources and time for risk management activities and to establish an agreed upon basis for evaluating risk.

### Elements of Plan Risk Management

| Element | Description |
|---|---|
| **Methodology** | Defines the approaches, tools, and data sources that will be used to perform risk management on the project. |
| **Roles and Responsibilities** | Defines the lead, support, and risk management team members for each type of activity in the risk management plan, and clarifies their responsibilities. |
| **Budgeting** | Estimates funds needed, based on assigned resources, for inclusion in the cost baseline and establishes protocols for application of contingency and management reserves. |
| **Timing** | Defines when and how often the risk management processes will be performed throughout the project life cycle and establishes risk management activities for inclusion in the project schedule. |
| **Risk Categories** | Provide a means for grouping potential causes of risk. A **Risk Breakdown Structure (RBS)** helps the project team to look at many sources from which project risk may arise in a risk identification exercise. |
| **Definitions of Risk Probability and Impact** | The quality and credibility of the risk analysis requires that different levels of risk probability and impact be defined that are specific to the project context. |

![Risk Breakdown Structure (RBS)](assets/ch04/ch04_img_098.jpeg)

---

## 5. Risk Identification

> **Definition:** **Risk Identification** is the process of determining which risks could affect the project and documenting their characteristics — an iterative process that continues throughout the project.

**Key Benefit:** Documentation of existing risks and the knowledge and ability it provides to the project team to anticipate events.

> **⚠️ Important:** It is an **iterative process** — risk cannot be foreseen at once.

### Risk Identification Techniques

| Technique | Description |
|---|---|
| **SWOT Analysis** (Strengths-Weakness-Opportunities-Threat Analysis) | A helpful technique within the greater organization to identify risk. Basically used to formulate strategies for identifying risks and to find out weaknesses and threats. |
| **Brainstorming** | The goal is to obtain a comprehensive list of project risks. |
| **Delphi Technique** | A way to reach a consensus of experts. |
| **Interviewing** | Interviewing experienced project participants, stakeholders, and subject matter experts helps to identify risks. |
| **Root Cause Analysis** | A specific technique used to identify a problem, discover the underlying causes that lead to it, and develop preventive action. |
| **Cause and Effect Diagrams** (Fishbone Diagrams) | Useful for identifying causes of risks. |
| **System or Process Flow Charts** | Show how various elements of a system interrelate and the mechanism of causation. |
| **Influence Diagrams** | Graphical representations of situations showing causal influences, time ordering of events, and other relationships among variables and outcomes. |

![Risk Identification](assets/ch04/ch04_img_092.jpeg)

### Common Software Project Risks

- Personnel shortfalls
- Unrealistic schedules and budgets
- Developing the wrong software functions
- Developing the wrong user interface
- Gold plating
- Continuing stream of requirements changes
- Shortfalls in externally performed tasks
- Shortfalls in externally furnished components
- Real-time performance shortfalls
- Straining computer science capabilities

---

## 6. Risk Register

> **Definition:** A **Risk Register** is the document where identified risks, their analysis results, and planned responses are recorded and tracked throughout the project.

The risk register is a document in which the results of risk analysis and risk response planning are recorded.

### Contents of Risk Register

- **List of Identified Risks**
- **List of Potential Responses**

---

## 7. Risk Analysis

> **Definition:** **Risk Analysis** is the process of identifying the factors that could affect project success, assessing their probability and impact, and calculating risk exposure to prioritize them.

This process includes risk identification, analysis of risks, and management of risks. It is a **pro-active process** which helps to control possible future events that may harm the overall project.

### Steps in Risk Analysis

| Step | Description |
|---|---|
| **Step 1** | Identifying the problems causing risk in project. |
| **Step 2** | Identifying the probability of occurrence of problems. |
| **Step 3** | Identifying the impact of problem. |
| **Step 4** | Assign value to Step 2 and Step 3 in range of 1–100: |
| | (0–10) **Very Low**, (10–25) **Low**, (25–50) **Moderate**, (50–75) **High**, (75–100) **Very High** |

> **⚡ Quick Formula:**
> $$
> \text{RE} = \text{Potential Damage} \times \text{Probability of Occurrence}
> $$

> Where,
> - **Potential Damage** can be a money value (e.g., flood caused damage of ₹15 crores)
> - **Probability of Occurrence** ranges from 0.00 to 1.00 (e.g., 0.1 = ten times in hundred)

**Probability Formats:**

| Format | Range | Example |
|---------|-------|---------|
| Percentage | 0% – 100% | 25% chance |
| Decimal | 0.00 – 1.00 | 0.25 probability |

> **Note:** For the formula, convert percentage to decimal (e.g., 25% = 0.25).

| Step | Description |
|---|---|
| **Step 5** | Calculate **Risk Exposure Factor** using the formula above. |
| **Step 6** | Prepare table consisting of all of these values and order risk on the basis of Risk Exposure Factor (RE). |

### Risk Table

![Risk Table with Impact and Probability of Occurrence](assets/ch04/ch04_img_093.jpeg)

![Risk Table](assets/ch04/ch04_img_094.jpeg)

![Risk Table](assets/ch04/ch04_img_095.jpeg)

### Probability and Impact Matrix

![Probability and Impact Matrix](assets/ch04/ch04_img_096.jpeg)

---

## 8. Qualitative Risk Analysis

> **Definition:** **Qualitative Risk Analysis** is the process of prioritizing risks by assessing and combining their probability of occurrence and impact — using subjective scales (High/Medium/Low) when numerical data is limited.

It assesses the priority of identified risks using their relative probability or likelihood of occurrence and the corresponding impact on project objectives. It enables project managers to reduce the level of uncertainty and to focus on high-priority risks.

### Three Functions of Qualitative Risk Analysis

1. **Prioritize** risks according to probability and impact
2. **Identify** the main areas of risk exposure
3. **Improve** understanding of project risks

---

### Qualitative vs Quantitative Risk Analysis

| Aspect | Qualitative Risk Analysis | Quantitative Risk Analysis |
|--------|--------------------------|----------------------------|
| Nature | Subjective | Objective |
| Input | Probability and Impact scales | Numeric data (cost, time) |
| Output | Priority list of risks (High/Medium/Low) | Numeric probability (e.g., 75% chance of completion) |
| When to Use | Early in project when data is limited | Later when more data is available |
| Key Question | "Which risks need the most attention?" | "What is the probability of meeting the deadline?" |

---

## 9. Quantitative Risk Analysis

> **Definition:** **Quantitative Risk Analysis** is the process of numerically analyzing the effect of identified risks on project objectives — using data to quantify probability (e.g., "75% chance of completing on time").

It produces quantitative risk information to support decision making in order to reduce project uncertainty. It is performed on prioritized risks obtained after qualitative risk analysis.

---

## 10. Risk Response (Avoidance & Mitigation)

### Risk Avoidance

> **Definition:** **Risk Avoidance** is a strategy that **completely eliminates a risk** by changing the project plan to remove the root cause — used for high-impact, high-probability risks.

- Focuses on **removing the root cause** of risk
- Often involves **changing scope, approach, or requirements**
- Used for **high-impact and high-probability risks**
- It is a **deliberate and planned action**, not ignoring the risk

> **⚠️ Important:** Risk avoidance is **not** ignoring a risk — it is **actively eliminating it**.

#### Examples

- Avoid using a **new, untested technology** and use a stable one instead
- Reduce project scope by **removing non-essential features**
- Extend deadlines to avoid **schedule risk**

### Risk Mitigation

> **Definition:** **Risk Mitigation** is a strategy that **reduces the probability or impact** of a risk without eliminating it completely — the risk still exists but its effect is minimized.

- Risk still exists, but its **effect is minimized**
- Focuses on **prevention and control**
- Used when risks **cannot be avoided completely**

> **⚠️ Important:** Types of risks include cyberattacks, natural disasters, legal issues, strategic or management errors, and accidents.

#### Examples

- Train backup team members to reduce **dependency risk**
- Perform regular testing to reduce **system failure risk**
- Use data backups to reduce **data loss impact**

---

### Key Difference

| Risk Avoidance | Risk Mitigation |
|---|---|
| Eliminates risk completely | Reduces risk impact/probability |
| Requires major changes | Improves existing plan |
| No chance of occurrence | Risk still exists |
| Used for severe risks | Used for manageable risks |

> **⭐ Exam Line:** *"Risk avoidance eliminates the risk, while risk mitigation reduces its likelihood or impact."*

---

## 11. Risk Monitoring and Control

### Risk Monitoring

> **Definition:** **Risk Monitoring** is the ongoing process of tracking identified risks, monitoring residual risks, and staying aware of the organization's current risk exposure.

It is a key component of determining individual risk appetites — in other words, the decision of how much risk can be tolerated.

#### Benefits of Risk Monitoring

- **Minimizes** Risk
- **Mitigates** the effects of Risk
- **Provides** a clear picture of the Risk Landscape
- **Promotes** Accountability
- **Creates** Transparency
- **Utilizes** Historical Events
- **Allows** for Improvement

### Risk Control

> **Definition:** **Risk Control** is the process of implementing risk response plans, tracking risks, identifying new threats, and continuously evaluating and improving the risk management approach.

**Improves efficiency** of the risk approach throughout the project life cycle to continuously optimize risk responses.

---

## 12. Risk Management Process

> **Definition:** **Risk Management Process** is the systematic application of planning, identification, analysis, response planning, and control to manage project risks effectively.

**Objectives:** To increase the likelihood and impact of positive events, and decrease the likelihood and impact of negative events in the project.

![Risk Management Process](assets/ch04/ch04_img_097.jpeg)

### Six Processes of Risk Management

| # | Process | Description |
|---|---|---|
| 1 | **Plan Risk Management** | The process of defining how to conduct risk management activities for a project. |
| 2 | **Identify Risks** | The process of determining which risks may affect the project and documenting their characteristics. |
| 3 | **Perform Qualitative Risk Analysis** | The process of prioritizing risks for further analysis or action by assessing and combining their probability of occurrence and impact. |
| 4 | **Perform Quantitative Risk Analysis** | The process of numerically analyzing the effect of identified risks on overall project objectives. |
| 5 | **Plan Risk Responses** | The process of developing options and actions to enhance opportunities and to reduce threats to project objectives. |
| 6 | **Control Risks** | The process of implementing risk response plans, tracking identified risks, monitoring residual risks, identifying new risks, and evaluating risk process effectiveness throughout the project. |

> **⭐ Key Takeaway:** Project risk is an uncertain event or condition that, if it occurs, has a positive or negative effect on one or more project objectives such as scope, schedule, cost, and quality.

> **Note:** Risk Management is not a one-time activity. The process is cyclical:
>
> ```
> Plan → Identify → Analyze → Respond → Monitor → (Loop back to Identify)
> ```
>
> Risk Monitoring should happen continuously throughout the project lifecycle.

---

## 13. PERT Numerical Example

> **Why PERT is in Risk Management:**
>
> PERT is a risk management tool because:
> - It accounts for uncertainty in activity durations using three time estimates
> - It calculates the probability of meeting project deadlines
> - It identifies critical activities that pose schedule risk
> - It provides a quantitative measure of schedule risk (standard deviation)
>
> This aligns with **Quantitative Risk Analysis** — numerically analyzing the effect of risks on project objectives.

> **💡 Example:** Using the same PERT network from Unit 3 (Activity Planning), the critical path is **1 → 3 → 5 → 6** with expected project duration = **25 days**. The PERT formulas and network diagram are covered in Unit 3 — here we focus on the risk/probability aspect.

### Step 1: Project Variance and Standard Deviation

From Unit 3, the variance of each activity on the critical path is already computed:

| Activity | $t_e$ | $\sigma^2$ |
|---|---|---|
| 1–3 | 6 | 1 |
| 3–5 | 14 | 16 |
| 5–6 | 5 | 1 |

> **⚡ Quick Formula:**
> $$
> \sigma_{\text{project}}^2 = \sum \sigma_{\text{critical path}}^2
> $$

### Step 2: Compute Project Variance and Standard Deviation

$$
\sigma^2 = 1 + 16 + 1 = 18
$$

$$
\sigma = \sqrt{18} = 4.24 \text{ days}
$$

> **⚡ Quick Formula:**
> $$
> z = \frac{T_s - T_e}{\sigma}
> $$
> Where:
> - $T_s$ = Schedule time (target)
> - $T_e$ = Project length (expected duration)
> - $\sigma$ = Standard deviation of project

### Step 3: Probability of Completing 5 Days Early

> **Given:** Critical path duration = 25 days. 5 days earlier = $25 - 5 = 20$ days.

$$
z = \frac{20 - 25}{4.24} = \frac{-5}{4.24} = -1.18
$$

$$
P(z \leq -1.18) = 0.1190 = 11.90\%
$$

> **Answer:** The probability that the project will be completed in **20 days** is **11.90%**.
>
> *(Value from standard normal distribution table for $z = -1.18$)*

> **⚡ Quick Formula:**
> $$
> T_s = T_e + z \cdot \sigma
> $$

### Step 4: Project Duration for 95% Confidence Level

> **Given:** 95% confidence. From the $z$-value table, the value for 0.95 is $z = 1.65$.

$$
1.65 = \frac{T_s - 25}{4.24}
$$

$$
T_s = 25 + 1.65 \times 4.24 = 25 + 6.97 = 31.97 \text{ days}
$$

> **Answer:** Project duration for **95% level of confidence** is **31.97 days**.
>
> *(Value from standard normal distribution table where 0.95053 is in row 1.6 and column 0.05, so $z = 1.65$)*

---

## 14. Quick Revision Summary

### Key Formulas

| Formula | Description |
|---|---|
| $t_e = \dfrac{t_o + 4t_m + t_p}{6}$ | Expected duration of an activity (PERT) |
| $\sigma^2 = \left(\dfrac{t_p - t_o}{6}\right)^2$ | Variance of an activity |
| $\sigma_{\text{project}} = \sqrt{\sum \sigma_{\text{critical path}}^2}$ | Standard deviation of project |
| $\text{RE} = \text{Potential Damage} \times \text{Probability of Occurrence}$ | Risk Exposure Factor |
| $z = \dfrac{T_s - T_e}{\sigma}$ | Z-value for probability calculation |

### Decision Rules

| Concept | Rule |
|---|---|
| **Risk vs Issue** | Risks *might* happen (uncertain); Issues *will* happen (certain) |
| **Risk Appetite** | Degree of uncertainty willing to take on for reward |
| **Risk Tolerance** | Amount of risk an organization will withstand |
| **Risk Threshold** | Level above which risk is not tolerated |
| **Qualitative Analysis** | Prioritize risks by probability & impact (subjective) |
| **Quantitative Analysis** | Numerically analyze effect on project objectives (objective) |
| **Risk Avoidance** | Eliminate the risk altogether |
| **Risk Mitigation** | Reduce the impact of risk |
| **Critical Path** | The path with the **longest** duration in the network |
| **Project Duration** | Sum of expected durations on the critical path |

### PERT Example Quick Reference

| Item | Value |
|---|---|
| Critical Path | 1 → 3 → 5 → 6 |
| Expected Duration | 25 days |
| Project Variance | 18 |
| Standard Deviation | 4.24 days |
| $P(\text{complete in 20 days})$ | 11.90% ($z = -1.18$) |
| Duration for 95% Confidence | 31.97 days ($z = 1.65$) |

## Past Exam Questions

**2082 Q9.** Define risk. Explain how risks are handled in a project.

**Answer:** **Risk** is an uncertain event or condition that, if it occurs, has a positive or negative effect on project objectives — defined by Risk Exposure (RE) = Probability × Impact. Risks are handled through: (1) **Risk Identification** — recognizing potential risks using checklists, brainstorming, and expert interviews; (2) **Risk Analysis** — assessing probability and impact of each risk; (3) **Risk Prioritization** — ranking risks by Risk Exposure; (4) **Risk Planning** — developing strategies: Avoidance (eliminate the cause), Reduction (reduce probability/impact), Transfer (shift to third party e.g., insurance), Acceptance (acknowledge and budget contingency); (5) **Risk Monitoring** — tracking identified risks and identifying new ones throughout the project.

**2081 Q11.** What is risk analysis? Explain the steps involved in risk analysis process.

**Answer:** **Risk analysis** is the systematic process of identifying, assessing, and prioritizing risks to understand their potential impact on a project. The steps in the risk analysis process are: (1) **Risk Identification** — brainstorming, checklists, and interviews to list possible risks; (2) **Evaluate probability and impact** for each identified risk; (3) **Calculate Risk Exposure** = P × I; (4) **Prioritize risks** by sorting them in descending order of Risk Exposure; (5) **Determine risk threshold** — the maximum acceptable risk before contingency action is triggered; (6) **Develop risk response plans** — strategies to handle high-priority risks; (7) **Monitor and review** — track risks throughout the project lifecycle.

**2080 Q11.** What are the practical implications of Risk Exposure?

**Answer:** **Risk Exposure (RE)** = Probability × Impact helps prioritize which risks need active management. Practical implications: (1) **High RE risks** demand immediate contingency planning — they threaten project success; (2) **Low RE risks** may be accepted or monitored passively; (3) RE provides a **quantitative basis** for comparing risks that differ in probability and impact (e.g., a low-probability/high-impact risk may have same RE as a high-probability/low-impact risk); (4) RE helps **allocate contingency budget** proportionally; (5) The **risk threshold** (maximum acceptable RE) determines when a risk must trigger a contingency plan. However, RE is a product of two subjective estimates, so it should be treated as an approximation, not an exact measure.

**2079 Q12b.** Write short note on Risk Exposure.

**Answer:** **Risk Exposure (RE)** is a quantitative measure of the potential loss from a risk, calculated as RE = Probability × Impact. Probability is the likelihood of the risk occurring (0 to 1), and Impact is the cost or schedule effect if it occurs (in rupees, days, or other units). RE allows risks to be ranked objectively — a risk with Probability 0.5 and Impact NRs. 1,00,000 has RE = 50,000. Projects typically set a **risk threshold** — if RE exceeds this threshold, a contingency plan must be triggered. The Risk Exposure matrix (Probability vs Impact grid) helps visualize and prioritize risks.

**2078 Q3.** Identify any four risks in a software project, rank them by Risk Exposure, and suggest a contingency plan for the two highest-ranked risks.

**Answer:** Four common software project risks: (1) **Staff turnover** — loss of key personnel; (2) **Requirement changes** — scope creep during development; (3) **Technology failure** — chosen technology fails to meet requirements; (4) **Unrealistic schedule** — schedule is too aggressive. **Ranking**: Assume probabilities and impacts: (1) Staff turnover RE = 0.7 × 50000 = 35,000; (2) Requirement changes RE = 0.6 × 30000 = 18,000; (3) Technology failure RE = 0.3 × 80000 = 24,000; (4) Unrealistic schedule RE = 0.5 × 40000 = 20,000. **Contingency plans**: For staff turnover (highest RE) — cross-train team members, document knowledge, maintain a skills inventory; For technology failure (second highest) — build a prototype early, have a fallback technology identified, and allocate time for technology evaluation.

## Glossary

| Term | Definition |
|------|-----------|
| **Risk** | An uncertain event that, if it occurs, has a positive or negative effect on project objectives |
| **Issue** | A known event that will definitely occur (unlike risk, which is uncertain) |
| **Risk Appetite** | Degree of uncertainty an entity is willing to take on in anticipation of reward |
| **Risk Tolerance** | Amount of risk an organization or individual will withstand |
| **Risk Threshold** | Level of impact above which a stakeholder will not tolerate the risk |
| **Risk Register** | Document recording identified risks, their analysis, and planned responses |
| **Risk Exposure (RE)** | Potential damage × Probability of occurrence |
| **Qualitative Analysis** | Prioritizing risks by assessing probability and impact subjectively |
| **Quantitative Analysis** | Numerically analyzing the effect of risks on project objectives |
| **Risk Avoidance** | Eliminating the risk altogether by changing the project plan |
| **Risk Mitigation** | Reducing the probability or impact of a risk |
| **SWOT Analysis** | Strengths-Weaknesses-Opportunities-Threats analysis for risk identification |
| **Delphi Technique** | Consensus-building technique using anonymous expert feedback |
| **RBS** | Risk Breakdown Structure — hierarchical grouping of potential risk sources |
