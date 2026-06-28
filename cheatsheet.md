# Software Project Management — Last Minute Revision

> **Course:** CSC415 | **Textbook:** Hughes & Cotterell | **Exam:** 60 marks theory

---

## Unit 1: Introduction to SPM

### Key Definitions
| Term | Definition |
|------|-----------|
| **Project (PMI)** | Temporary endeavor to create a unique product/service |
| **Software Project** | Complete SW dev process from req gathering → maintenance within time & budget |
| **SPM** | Application of knowledge, skills, tools & techniques to meet project requirements |
| **PM Life Cycle** | 4 phases: Initiation → Planning → Execution → Closure |
| **SPM Framework** | 3 parts: Project Lifecycle + Project Control Cycle + Tools & Templates |

### SP vs Other Projects — 4 Unique Characteristics (ICCF)
| Char | Description |
|------|-------------|
| **I**nvisibility | Progress not physically visible (unlike construction) |
| **C**omplexity | Higher complexity per $ than other engineered artifacts |
| **C**onformity | Must conform to inconsistent human client requirements |
| **F**lexibility | Highly subject to change; easy to restructure parts |

### SMART Goals
| Letter | Meaning |
|--------|---------|
| **S**pecific | Clear goal (Who? What? When? Where? Why?) |
| **M**easurable | Quantifiable target |
| **A**chievable | Realistic with available resources |
| **R**elevant | Aligns with business goals |
| **T**ime Bounded | Has a deadline |

### Classification of Projects (Memory Aid: SCIO)
| Factor | Types |
|--------|-------|
| **S**ource of Capital | Public / Private / Mixed |
| **C**ontent | Construction / IT / Business / Service |
| **I**nvolvement | Departmental / Internal / Matrix / External |
| **O**bjective | Production / Social / Educational / Community / Research |

### Categorizing Software Projects
- **Information System** (interface with org) vs **Embedded System** (interface with machine)
- **Outsourced Projects**
- **Compulsory** vs **Voluntary Users**
- **Objective-driven** Development

### Activities Covered by SPM (3 Processes)
1. **Feasibility Study** — Technical / Economical / Legal / Operational / Time
2. **Planning** — Outline plan + detailed plan for first stage
3. **Execution** — Design + Implementation

### Project Manager Skills
| Category | Skills |
|----------|--------|
| **Technical** | Scheduling, Cost Control, Risk Mgmt, Task Mgmt, Quality Mgmt |
| **Soft** | Leadership, Negotiation, Critical Thinking, Communication |
| **Management** | Planning, Organizing, Motivating, Budgeting, Risk Analysis, Documentation |

### 4 Types of Project Plan
Project Plan / Quality Plan / Configuration Mgmt Plan / Communication Plan

### Project Lifecycle vs Product Lifecycle
| Aspect | Project Lifecycle | Product Lifecycle |
|--------|------------------|-------------------|
| Scope | Start to finish | Concept to retirement |
| Duration | Temporary (ends when closed) | Long-term (5+ years) |
| Focus | Delivering project outputs | Managing product through entire life |

### SPM Tools
| Tool | Usage |
|------|-------|
| **Gantt Chart** | Schedule visualization (bars against time) |
| **PERT Chart** | Network diagram for task sequencing |
| **WBS** | Task-oriented hierarchical decomposition |

### Scope Triangle
**5 constraints:** Scope, Quality, Cost, Time, Resources — all interdependent

---

## Unit 2: Project Analysis

### Strategic Assessment
Evaluates project alignment with organizational long-term goals.
| Type | Focus |
|------|-------|
| **Programme Management** | Projects for **internal** use — coordination across related projects (Ferns: "group of related projects managed in coordinated way") |
| **Portfolio Management** | Products for **external** clients — evaluates value to both client & SW company |

**Issues in Programme Management:** Objectives, IS Plan, Org Structure, MIS, Personnel, Good Will

### Technical Assessment
- Evaluates if functionality can be implemented with available HW/SW
- **Technical Reviews** — periodic evaluations (design/code/test reviews)
- **Technical Indicators** — quantitative measures: KPPs (critical success parameters), TPMs (actual vs planned performance)

### Economic Analysis Methods
| Method | Formula | Decision Rule |
|--------|---------|---------------|
| **Present Worth (PW)** | $PW = \sum \frac{F_t}{(1+i)^t}$ | Revenue: **max** PW (>0 viable); Cost: **min** PW |
| **Future Worth (FW)** | Rev: $FW = -P(1+i)^n + A\frac{(1+i)^n-1}{i} + S$ / Cost: $FW = P(1+i)^n + C\frac{(1+i)^n-1}{i} - S$ | Revenue: **max** FW; Cost: **min** FW |
| **Annual Worth (AW)** | $AW = PW \times \frac{i(1+i)^n}{(1+i)^n-1}$ | Revenue: AW > 0, select highest; Cost: min AW |
| **IRR** | $\sum \frac{F_t}{(1+IRR)^t} = 0$ | Accept if **IRR ≥ MARR** |
| **BCR** | $BCR = \frac{PV(Benefits)}{PV(Costs)}$ | Accept if **BCR > 1** |

### Revenue-Dominated vs Cost-Dominated Cash Flow
| Aspect | Revenue-Dominated | Cost-Dominated |
|--------|------------------|----------------|
| **Inflows** | Positive sign (+) | Negative sign (−) |
| **Outflows** | Negative sign (−) | Positive sign (+) |
| **Select** | Max PW/FW/AW | Min PW/FW/AW |

### Uniform Gradient Cash Flow
$PW = A_1(P/A, i, n) + G(P/G, i, n)$ where G = constant increase/decrease per period

### Comparison of Alternatives
| Aspect | Mutually Exclusive | Independent |
|--------|-------------------|-------------|
| **Selection** | Only one can be selected | Multiple can be selected |
| **Basis** | Compare against each other | Compare against MARR threshold |
| **PW Criteria** | Select **highest** PW | Accept all with **PW ≥ 0** |

### Standard Interest Factors
| Factor | Formula | Purpose |
|--------|---------|---------|
| (P/F, i, n) | $1/(1+i)^n$ | Future → Present |
| (F/P, i, n) | $(1+i)^n$ | Present → Future |
| (P/A, i, n) | $\frac{(1+i)^n-1}{i(1+i)^n}$ | Uniform series → Present |
| (A/P, i, n) | $\frac{i(1+i)^n}{(1+i)^n-1}$ | Present → Uniform series |
| (F/A, i, n) | $\frac{(1+i)^n-1}{i}$ | Uniform series → Future |
| (A/F, i, n) | $\frac{i}{(1+i)^n-1}$ | Future → Uniform series |

### Discounted Payback Period
$PP = \text{Year before positive} + \frac{|\text{Cumulative Discount at that Year}|}{\text{Discounted CF of recovery year}}$
- Default discount rate if not given: **10%**
- Shorter payback → more desirable

### Return on Investment (ROI)
$ROI = \frac{\text{Profit}}{\text{Total Investment}} \times 100\%$

---

## Unit 3: Activity Planning & Scheduling

### Objectives of Activity Planning
1. **Feasibility Assessment** — Is project possible within timescales & resources?
2. **Resource Allocation** — What resources needed, when?
3. **Detailed Costing** — How much will it cost, when?
4. **Motivation** — Targets & monitoring drive staff performance
5. **Co-ordination** — When do different depts need to be available?

### Approaches to Identify Activities
| Approach | Focus | Method |
|----------|-------|--------|
| **Activity-Based** | Lists all activities directly | Brainstorming, past project analysis |
| **Product-Based** | PBS + PFD → derive activities | SSADM methodology |
| **Hybrid** | Combination of both | Deliverable-based WBS (most practical) |

### Work Breakdown Structure (WBS)
- Hierarchical decomposition of total scope
- **100% Rule**: Child elements sum to parent
- **IBM 5 Levels**: Project → Deliverables → Components → Work-packages → Tasks

### Gantt Chart (Bar Chart)
- Horizontal bars show task duration (developed by Henry L. Gantt, 1917)
- Shows: start/end dates, **does not** show dependencies

### Network Planning Models
| Method | Type | Key Feature |
|--------|------|-------------|
| **CPM** | Deterministic (fixed durations) | Critical path, cost-time tradeoff |
| **PERT** | Probabilistic (3 time estimates) | Z-values for probability |
| **PDM** | Deterministic | 4 dependency types (FS, FF, SS, SF) |

### ADM vs PDM
| Aspect | ADM (AOA) | PDM (AON) |
|--------|-----------|-----------|
| Activities | Arrows | Boxes (nodes) |
| Dependencies | FS only | FS, FF, SS, SF |
| Popularity | Less popular | Most popular (SW tools) |

### CPM Formulas (Forward & Backward Pass)
```
┌──────┬──────┬──────┐
│  ES  │  Dur │  EF  │
├──────┼──────┼──────┤
│  LS  │Float │  LF  │
└──────┴──────┴──────┘
```
- **ES** = Max(EF of all predecessors)
- **EF** = ES + Duration
- **LF** = Min(LS of all successors)
- **LS** = LF − Duration
- **Float** = LS − ES = LF − EF
- **Critical Path**: path with **Float = 0** (longest path = min project duration)

### PDM — 4 Dependency Types
| Type | Notation | Meaning |
|------|----------|---------|
| Finish-to-Start | **FS** | Predecessor must finish before successor starts |
| Finish-to-Finish | **FF** | Predecessor must finish before successor finishes |
| Start-to-Start | **SS** | Predecessor must start before successor starts |
| Start-to-Finish | **SF** | Predecessor must start before successor finishes (rare) |

### PERT Formulas
$t_e = \frac{a + 4m + b}{6}$
$\sigma^2 = \left(\frac{b - a}{6}\right)^2$
Where: $a$ = optimistic, $m$ = most likely, $b$ = pessimistic

### Shortening Project Duration
1. Identify critical path → 2. Reduce critical activity durations (add resources) → 3. Check for new critical paths → 4. Parkinson's Law: "Work expands to fill time available"

### Probability Interpretation (Z-value)
| Z | Probability | Meaning |
|---|-------------|---------|
| Z = 0 | 50% | Equal chance |
| Z > 0 | > 50% | Likely to meet deadline |
| Z < 0 | < 50% | Unlikely to meet deadline |

---

## Unit 4: Risk Management

### Risk vs Issue
| Aspect | Risk | Issue |
|--------|------|-------|
| Timing | Future event | Present or certain future |
| Certainty | Uncertain (may/may not happen) | Certain (will definitely happen) |
| Action | Plan & prepare (proactive) | Address & resolve (reactive) |

### Risk Categories
| Type | Examples |
|------|----------|
| **Cost** | Budget overruns, scope creep |
| **Schedule** | Activities take longer than expected |
| **Performance** | Fails to meet specifications |
| **Strategic** | Wrong technology choice |
| **Operational** | Poor implementation, process problems |
| **Market** | Competition, FX, interest rate |
| **Legal** | Regulatory obligations, contract litigation |
| **External** | Storms, sabotage, labor strikes |

### Risk Appetite, Tolerance, Threshold
| Concept | Level | Meaning |
|---------|-------|---------|
| **Risk Appetite** | Strategic | How much risk org is willing to take on |
| **Risk Tolerance** | Project | How much variation org can withstand |
| **Risk Threshold** | Trigger | Exact point above which risk is unacceptable |

### Risk Management — 6 Processes
1. **Plan Risk Management** — define methodology, roles, budget
2. **Identify Risks** — determine which risks may affect project
3. **Perform Qualitative Risk Analysis** — prioritize by P×I (subjective)
4. **Perform Quantitative Risk Analysis** — numerically analyze effect (objective)
5. **Plan Risk Responses** — develop options to enhance opportunities, reduce threats
6. **Control Risks** — implement plans, track, identify new risks

### Risk Identification Techniques
Brainstorming / Delphi Technique / Interviewing / SWOT Analysis / Root Cause Analysis / Cause & Effect Diagrams / Flow Charts / Influence Diagrams

### Risk Analysis
**Risk Exposure (RE)** = Potential Damage × Probability of Occurrence
- Probability format: 0%–100% or 0.00–1.00
- **Risk Register** documents identified risks, analysis results, planned responses

### Qualitative vs Quantitative Risk Analysis
| Aspect | Qualitative | Quantitative |
|--------|-------------|--------------|
| Nature | Subjective (High/Medium/Low) | Objective (numeric) |
| Output | Priority list | Numeric probability (e.g., 75%) |
| When | Early, limited data | Later, more data available |

### Risk Response Strategies
| Strategy | Action |
|----------|--------|
| **Avoid** | Eliminate risk completely (change scope/approach) |
| **Transfer** | Shift to third party (insurance, outsourcing) |
| **Mitigate** | Reduce probability or impact |
| **Accept** | Acknowledge and prepare contingency |

### PERT for Risk (Z-value)
$Z = \frac{T_S - T_E}{\sigma_{path}}$, $\sigma_{path} = \sqrt{\sum \sigma^2_{critical\ path}}$
$T_S$ = target, $T_E$ = expected project length

---

## Unit 5: Resource Allocation

### Resource Types (5 Categories)
| Type | Examples |
|------|----------|
| **Financial** | Capital, funds, budgets |
| **Physical** | Equipment, raw materials, facilities |
| **Human** | Staff, labor, management |
| **Technological** | Software, hardware, IT infrastructure |
| **Intangible** | Licensing rights, patents, org knowledge |

### Resource Allocation Process
1. Identify resource requirements per activity
2. Estimate resource availability
3. Assign resources to activities
4. Resolve conflicts (resource leveling)

### Factors Influencing Allocation
Availability / Criticality (experienced → critical tasks) / Risk (experienced → high risk) / Training / Team Building

### Resulting Schedules
| Schedule | Description |
|----------|-------------|
| **Activity Schedule** | Start & completion dates for each activity |
| **Resource Schedule** | Dates & levels for resource needs |
| **Cost Schedule** | Cumulative expenditures |

### Steps to Determine Resource Requirements
1. Establish Scope → 2. Make WBS → 3. Estimate Duration → 4. Identify Requirements → 5. Create Resource Schedule → 6. Assign Resources → 7. Track

### Resource Leveling vs Resource Smoothing
| Aspect | Leveling | Smoothing |
|--------|----------|-----------|
| **Impact on Critical Path** | ⚠️ **May delay** project | ✅ **Does not impact** |
| **Order** | Performed **first** | Performed **after** leveling |
| **Float Usage** | May not use float | Uses total & free floats |
| **Key Question** | "When can we finish with given resources?" | "How to distribute resources evenly?" |

### Multiple Projects — Priority Rules
When constrained resource is needed by multiple projects:
1. Consider penalty for delay
2. Consider project importance
3. Assign resource to highest-priority project first

---

## Unit 6: Monitoring & Control

### Monitoring vs Controlling
| Aspect | Monitoring | Controlling |
|--------|-----------|-------------|
| **Focus** | Observing & tracking | Taking corrective action |
| **Purpose** | Ensure project is on track | Ensure goals are met |
| **Nature** | Observation & evaluation | Action & correction |

### 5W Questions of Monitoring
| W | Answer |
|---|--------|
| **Why** | Detect & react to deviations |
| **What** | Men, Machines, Time, Materials, Tasks, Money, Quality |
| **When** | Continuously, at milestones, at task completion |
| **Where** | Head office / Site office / Depends |
| **How** | Meetings, CPA/PERT/Gantt updates, EVA, Milestones |

### Data Collection
- **Partial Completion Report** — weekly timesheets showing work done & time spent
- **Risk Report** — traffic-light method: 🟢 Green (on target) / 🟡 Amber (recoverable) / 🔴 Red (difficult)

### Checkpoints
- **Time-based** (weekly/monthly/quarterly)
- **Event-based** (end of activity, middle of critical activity)
- Set before plan publication; everyone must know when/what

### Visualizing Progress (3 Techniques)
| Technique | What It Shows |
|-----------|---------------|
| **Gantt Chart** | Planned vs actual bars; today cursor |
| **Slip Chart** | Slip line showing ahead/behind; bending = rescheduling needed |
| **Ball Chart** | Circles contain original & revised start/completion dates |

### Cost Monitoring
- **Cumulative Expenditure Chart** — compares actual vs planned spending
- Reveals if being on time is due to cost overruns

### Earned Value Analysis (EVA)
| Metric | Formula | Meaning |
|--------|---------|---------|
| **BCWS (PV)** | — | Budgeted cost of work **scheduled** |
| **BCWP (EV)** | — | Budgeted cost of work **performed** |
| **ACWP (AC)** | — | **Actual** cost of work performed |
| **SV** | EV − PV | Positive = ahead; Negative = behind |
| **CV** | EV − AC | Positive = under budget; Negative = over budget |
| **SPI** | EV / PV | > 1 = ahead; =1 = on schedule; < 1 = behind |
| **CPI** | EV / AC | > 1 = under budget; =1 = on budget; < 1 = over |
| **EAC** | BAC / CPI | Revised total cost estimate |
| **ETC** | EAC − AC | Remaining cost |
| **VAC** | BAC − EAC | Expected over/under |

**Memory Aid:** EV is always on top (numerator)
- CV = EV − AC (like profit = revenue − cost)
- SV = EV − PV
- CPI = EV / AC
- SPI = EV / PV

---

## Unit 7: Managing Contracts & People

### Contract Types
| Type | Buyer Risk | Seller Risk | Best When |
|------|-----------|-------------|-----------|
| **FP (Fixed Price)** | Low | High | Well-defined, stable requirements |
| **CR (Cost Reimbursable)** | High | Low | R&D, uncertain requirements |
| **T&M (Time & Material)** | Medium | Medium | Scope may change; not-to-exceed limit |
| **SDS (Subscription)** | Low | Low | Ongoing software usage & support |

### FP Variants: FFP / FPIF (incentive) / FP-EPA (economic adjustment)
### CR Variants: CPFF / CPIF / CPAF / Cost + Percentage of Cost

### Contract Management Lifecycle (6 Stages)
| Stage | Phase |
|-------|-------|
| **1. Contract Creation** | Pre-Signature |
| **2. Negotiation & Collaboration** | Pre-Signature |
| **3. Review & Approval** | Pre-Signature |
| **4. Administration & Execution** | Post-Signature |
| **5. Ongoing Management & Renewal** | Post-Signature |
| **6. Reporting & Tracking** | Post-Signature |

### Contract Terms
| Category | Breach Remedy |
|----------|---------------|
| **Condition** (fundamental) | Terminate contract + claim damages |
| **Warranty** (secondary) | Claim damages only (cannot terminate) |
| **Innominate** (neither) | Depends on severity |

**Expressed** = specifically mentioned; **Implied** = default rules (can override expressed)

### Key Clauses
Confidentiality / Termination / Force Majeure (greater force — natural disasters) / Dispute / Damages

### Contract Placement
| Aspect | Permanent | Contract |
|--------|-----------|----------|
| Duration | Long-term, full-time | Short-term, project-based |
| Advantage | Reliable, known personnel | Cost-effective, quick onboarding |
| Disadvantage | Costly to recruit | Not for long-term positions |

### Acceptance
Customer tests completed work against agreed criteria → payment depends on successful acceptance. Time limit may apply.

### Managing People — 3 Concerns
1. **Staff Selection** 2. **Staff Development** 3. **Staff Motivation**

### Selecting the Right Person
**Eligible** (has qualifications) vs **Suitable** (can actually do the job)
⚠️ Danger: Eligible but not suitable; ✅ Best: Suitable but not eligible (cheaper, stays longer)

**Process:** Job Spec → Job Holder Profile → Obtain Applicants → Examine CVs → Interview → Other Procedures (references, medical)

### Motivation — Herzberg's Two-Factor Theory
| Factor | Effect | Examples |
|--------|--------|----------|
| **Hygiene** | Prevent dissatisfaction | Salary, job security, work environment, supervision |
| **Motivators** | Create satisfaction | Achievement, recognition, responsibility, growth |

### Tuckman's 5 Stages of Team Development
| Stage | Key Characteristic |
|-------|-------------------|
| **Forming** | Orientation, high uncertainty, look for leadership |
| **Storming** | Conflict, competition, subgroups form |
| **Norming** | Unity emerges, consensus on roles, performance increases |
| **Performing** | Mature, organized, focused on goals |
| **Adjourning** | Wrapping up, lessons learned, formal recognition |

### Structured vs Unstructured Decisions
| Aspect | Structured | Unstructured |
|--------|-----------|-------------|
| Goals | Defined | Uncertain |
| Nature | Repetitive, routine, programmable | Unique, no predefined procedure |
| Example | Payroll | Personal development decisions |

### Leadership — 7 Types of Power
| Type | Category |
|------|----------|
| **Coercive** | Position (threaten punishment) |
| **Connection** | Position (access to powerful people) |
| **Legitimate** | Position (title/status) |
| **Reward** | Position (can give rewards) |
| **Expert** | Personal (specialized skill) |
| **Information** | Personal (exclusive access to info) |
| **Referent** | Personal (personal attractiveness) |

### Leadership Styles (2×2 Grid)
| | Autocratic | Democratic |
|--|-----------|------------|
| **Directive** | Decides alone, close supervision | Decides participatively, close supervision |
| **Permissive** | Decides alone, autonomy in implementation | Decides participatively, autonomy in implementation |

### Organizational Structures
| Structure | PM Authority | Key Feature |
|-----------|-------------|-------------|
| **Functional** | Low/None | Employees grouped by specialization (Finance, IT, Sales) |
| **Matrix** | Moderate-High | Dual reporting: functional mgr + project mgr (Weak/Balanced/Strong) |
| **Projectized** | High/Total | Full-time PM, team co-located |

---

## Unit 8: SQA & Testing

### Testing Principles (Memory Aid: P-E-E-D-P-T-A)
1. **P**resence of defects (cannot prove absence)
2. **E**xhaustive testing impossible (26¹⁰ combos → 4.5M years)
3. **E**arly testing (shift left — early detection saves cost)
4. **D**efect clustering (Pareto: 80% defects in 20% modules)
5. **P**esticide paradox (repeat tests find fewer bugs; update test cases)
6. **T**esting is context-dependent
7. **A**bsence-of-errors fallacy (no bugs ≠ useful if wrong requirements)

### Testing vs Verification vs Validation vs Debugging
| Term | Definition |
|------|-----------|
| **Testing** | Execute program to find faults |
| **Verification** | "Are we building the product **right**?" (reviews, inspections) |
| **Validation** | "Are we building the **right** product?" (user testing) |
| **Debugging** | Diagnosing & correcting errors |

### Manual vs Automation Testing
| Aspect | Manual | Automation |
|--------|--------|------------|
| Approach | Human tester | Scripts & tools |
| Speed | Slower | Faster |
| Best For | Exploratory, usability | Regression, repeated execution |

### 4 Levels of Testing
| Level | Who | Focus |
|-------|-----|-------|
| **Unit** | Developer | Single component/module |
| **Integration** | Tester | Module interactions & interfaces |
| **System** | Tester | Complete system (load, reliability, performance, security) |
| **Acceptance** | User/QA | End-user requirements, deployment readiness |

### Test Strategies
| Strategy | Description |
|----------|-------------|
| **Static** | Evaluate without running (reviews, walkthroughs) |
| **Structural** | Run on real devices, find data flow errors |
| **Behavioral** | Focus on system behavior, workflows, user journey |

### V-Model
```
Requirements ──────► Acceptance Testing
Design ─────────────► System Testing
Architecture ───────► Integration Testing
Module Design ──────► Unit Testing
```

### QA vs QC
| Aspect | QA | QC |
|--------|----|----|
| Focus | Process-oriented (prevent defects) | Product-oriented (detect defects) |
| When | During development (proactive) | After development (reactive) |
| Slogan | "Prevent defects" | "Find & fix defects" |

### Software Quality — ISO 9126 (6 Factors)
**Functionality** / **Reliability** / **Usability** / **Efficiency** / **Maintainability** / **Portability**

### SEI-CMM 5 Levels (Mnemonic: **I** **R**eally **D**o **M**ake **O**ptimizations)
| Level | Name | Key Feature |
|-------|------|-------------|
| 1 | **I**nitial | Ad-hoc, heroics, unpredictable |
| 2 | **R**epeatable | Basic project management, repeatable successes |
| 3 | **D**efined | Standardized processes organization-wide |
| 4 | **M**anaged | Quantitative metrics, predictable quality |
| 5 | **O**ptimizing | Continuous process improvement |

### CMM — 5 Aspects
Maturity Levels / Key Process Areas / Goals / Common Features / Key Practices

### SQA Activities
Quality Planning → Technical Reviews → Testing → Defect Tracking → Process Improvement → Configuration Management → SQA Audits

### SQA Plan Contents
Management Section / Documentation Section / Standards, Practices & Conventions / Reviews & Audits / Problem Reporting & Corrective Action / Test Section / Others (tools, change control, training, risk)

### Mission of SEI
Research → Collaboration → Development & Demonstration → Transition

---

## Unit 9: Software Configuration Management

### First Law of System Engineering
> "No matter where you are in system life cycle, the system will change, and the desire to change will persist throughout."

### 4 Aspects of Software Evolution (Memory Aid: CAP-P)
| Type | Description | Example |
|------|-------------|---------|
| **C**orrective | Fix faults/bugs | Fix login bug |
| **A**daptive | Accommodate environment changes | Upgrade DB, new OS |
| **P**erfective | Refactoring for maintainability | Split 500-line function |
| **P**reventive | Prevent future degradation | Input validation, DB replication |

### Why SCM?
- Prevents conflicting changes
- Supports multiple versions
- Enables rollback to last known safe state
- Increases accountability & confidence

### Basic CM Steps (7 Steps)
1. **Identify Configuration Items (CIs)** — code, docs, requirements, tests
2. **Define Repository Structure** — folder hierarchy
3. **Choose a VCS** — e.g., Git
4. **Establish a Baseline** — starting point for development
5. **Create Change Management Process** — procedures for changes
6. **Set up Build & Release Management** — packaging & distribution
7. **Define Access Control & Security** — roles, permissions, passwords

### Configuration Item (CI)
Any work product under SCM control (source code, docs, design specs, test cases) — each with unique identifier.

### Baseline
> Formally reviewed & agreed-upon version of a CI — changeable only through formal change control.

**Common Baselines:** Functional (SRS frozen) → Design (architecture approved) → Product (code reviewed) → Release (v1.0 shipped)

**Key:** Before baseline → quick informal changes. After baseline → formal procedure required.

### SCM Roles
| Role | Analogy | Responsibility |
|------|---------|---------------|
| **Configuration Manager** | Librarian | Identify CIs, enforce SCM process |
| **Developer** | Author | Change code, resolve conflicts |
| **Auditor** | Editor | SCM audits, verify consistency |
| **User** | Reader | Understand SCM, use latest version |

### SCM Responsibilities
Version Control / Baseline Management / Change Management / Build & Release Management / Branching & Merging / Access Control & Security

### 5 Functions of Management
1. **Planning** — roadmap, risks, solutions
2. **Organizing** — hierarchy to carry out tasks
3. **Staffing** — assign by knowledge/skills/abilities
4. **Directing** — supervise, communicate, track progress
5. **Controlling** — measure progress against goals, coordinate

---

## Quick Reference: Key Formulas

| Formula | Equation | Unit |
|---------|----------|------|
| PERT Expected Time | $t_e = (a + 4m + b)/6$ | — |
| PERT Variance | $\sigma^2 = ((b-a)/6)^2$ | — |
| Present Worth | $PW = \sum F_t/(1+i)^t$ | ₹ |
| Future Worth (Revenue) | $FW = -P(1+i)^n + A\frac{(1+i)^n-1}{i} + S$ | ₹ |
| Future Worth (Cost) | $FW = P(1+i)^n + C\frac{(1+i)^n-1}{i} - S$ | ₹ |
| Annual Worth | $AW = PW \times \frac{i(1+i)^n}{(1+i)^n-1}$ | ₹/yr |
| IRR | $\sum F_t/(1+IRR)^t = 0$ | % |
| BCR | $PV(Benefits)/PV(Costs)$ | ratio |
| Uniform Gradient PW | $PW = A_1(P/A,i,n) + G(P/G,i,n)$ | ₹ |
| Discounted Payback | $PP = Y_{-} + \frac{|Cum_{-}|}{CF_{+}}$ | yrs |
| ROI | $(Profit / Investment) \times 100\%$ | % |
| Schedule Variance | $SV = EV - PV$ | ₹ |
| Cost Variance | $CV = EV - AC$ | ₹ |
| SPI | $SPI = EV / PV$ | ratio |
| CPI | $CPI = EV / AC$ | ratio |
| EAC | $EAC = BAC / CPI$ | ₹ |
| ETC | $ETC = EAC - AC$ | ₹ |
| VAC | $VAC = BAC - EAC$ | ₹ |
| Float | $Float = LS - ES = LF - EF$ | days |
| Z-Score (PERT) | $Z = (T_S - T_E)/\sigma_{path}$ | — |
| Risk Exposure | $RE = Potential\ Damage \times P(occurrence)$ | ₹ |
| Interest Factor (P/F) | $P/F = 1/(1+i)^n$ | — |
| Interest Factor (F/P) | $F/P = (1+i)^n$ | — |
| Interest Factor (P/A) | $P/A = \frac{(1+i)^n-1}{i(1+i)^n}$ | — |
| Interest Factor (A/P) | $A/P = \frac{i(1+i)^n}{(1+i)^n-1}$ | — |
| Interest Factor (F/A) | $F/A = \frac{(1+i)^n-1}{i}$ | — |
| Interest Factor (A/F) | $A/F = \frac{i}{(1+i)^n-1}$ | — |
