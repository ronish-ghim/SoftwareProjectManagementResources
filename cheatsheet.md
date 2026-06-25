# Software Project Management — Cheatsheet

> **Course:** CSC415 | **Textbook:** Hughes & Cotterell | **Exam:** 60 marks theory

---

## Table of Contents

- [Unit 1: Introduction to SPM](#unit-1-introduction-to-spm)
  - [Key Definitions](#key-definitions)
  - [SP vs. Other Projects](#sp-vs-other-projects)
  - [Categorizing SPs](#categorizing-sps)
  - [SPM Framework (5 Process Groups)](#spm-framework-5-process-groups)
  - [Types of Project Plan](#types-of-project-plan)
- [Unit 2: Project Analysis](#unit-2-project-analysis)
  - [Strategic Assessment](#strategic-assessment)
  - [Technical Assessment](#technical-assessment)
  - [Economic Analysis Formulas](#economic-analysis-formulas)
  - [Decision Rules](#decision-rules)
- [Unit 3: Activity Planning & Scheduling](#unit-3-activity-planning--scheduling)
  - [Work Breakdown Structure (WBS)](#work-breakdown-structure-wbs)
  - [Gantt Chart (Bar Chart)](#gantt-chart-bar-chart)
  - [Network Planning Models](#network-planning-models)
  - [CPM Formulas](#cpm-formulas)
  - [PERT Formulas](#pert-formulas)
  - [Shortening Project Duration](#shortening-project-duration)
- [Unit 4: Risk Management](#unit-4-risk-management)
  - [Risk Categories](#risk-categories)
  - [Risk Analysis (PERT Z-value)](#risk-analysis-pert-z-value)
  - [Z-Table Interpretation](#z-table-interpretation)
  - [Risk Response Strategies](#risk-response-strategies)
- [Unit 5: Resource Allocation](#unit-5-resource-allocation)
  - [Resource Types](#resource-types)
  - [Resource Allocation Process](#resource-allocation-process)
  - [Resource Smoothing](#resource-smoothing)
  - [Resource Balancing](#resource-balancing)
- [Unit 6: Monitoring & Control](#unit-6-monitoring--control)
  - [Data Collection Methods](#data-collection-methods)
  - [Earned Value Analysis](#earned-value-analysis)
  - [Project Control](#project-control)
- [Unit 7: Managing Contracts & People](#unit-7-managing-contracts--people)
  - [Contract Types](#contract-types)
  - [FP Variants](#fp-variants)
  - [CP Variants](#cp-variants)
  - [Contract Stages](#contract-stages)
  - [Managing People - Key Concepts](#managing-people---key-concepts)
  - [Organizational Structures](#organizational-structures)
- [Unit 8: SQA & Testing](#unit-8-sqa--testing)
  - [Testing Principles](#testing-principles)
  - [Test Levels](#test-levels)
  - [Test Strategies](#test-strategies)
  - [V-Model](#v-model)
  - [Verification vs. Validation](#verification-vs-validation)
  - [Software Quality (ISO 9126)](#software-quality-iso-9126)
  - [SEI-CMM Levels](#sei-cmm-levels)
  - [SQA Activities](#sqa-activities)
  - [SQA Plan Contents](#sqa-plan-contents)
- [Unit 9: Software Configuration Management](#unit-9-software-configuration-management)
  - [Why SCM?](#why-scm)
  - [SCM Basics](#scm-basics)
  - [SCM Activities](#scm-activities)
  - [Branching Strategies](#branching-strategies)
- [Quick Reference: Key Formulas](#quick-reference-key-formulas)

---

## Unit 1: Introduction to SPM

### Key Definitions

| Term | Definition |
|------|-----------|
| **Software Product** | A computer program delivered to a customer with associated documentation |
| **Software Project** | A temporary endeavor to create a unique product/service/result |
| **SPM** | The application of knowledge, skills, tools, and techniques to project activities to meet project requirements |

### SP vs. Other Projects
- **Unique** — each software project produces a different product
- **Intangible** — deliverables are not physical
- **Complex** — requirements evolve, technology changes
- **Deterministic** — schedule/cost can be estimated upfront (unlike R&D)

### Categorizing SPs
| Category | Description |
|----------|-------------|
| **Custom** | Built for a specific client |
| **Package** | Mass-market product |
| **Systems** | Infrastructure/integration projects |
| **Applications** | End-user applications |

### SPM Framework (5 Process Groups)
1. **Initiating** — define project, get authorization
2. **Planning** — scope, schedule, cost, risk plans
3. **Executing** — do the work
4. **Monitoring & Controlling** — track, review, regulate progress
5. **Closing** — formal acceptance, handover

### Types of Project Plan
- **Project plan** — overall management document
- **Quality plan** — quality standards and activities
- **Configuration management plan** — version control
- **Communication plan** — stakeholder info flow

---

## Unit 2: Project Analysis

### Strategic Assessment
- Does the project align with organizational goals?
- Is it technically feasible?
- What are the constraints (time, budget, scope)?

### Technical Assessment
- Technology readiness
- Team skills and experience
- Existing systems compatibility

### Economic Analysis Formulas

**Present Worth (PW)**
$$PW = \sum_{t=0}^{n} \frac{F_t}{(1+i)^t}$$

**Future Worth (FW)**
$$FW = PW \times (1+i)^n$$

**Annual Worth (AW)**
$$AW = PW \times \frac{i(1+i)^n}{(1+i)^n - 1}$$

**Internal Rate of Return (IRR)**
Find $i$ where $NPV = 0$:
$$\sum_{t=0}^{n} \frac{F_t}{(1+IRR)^t} = 0$$

**Benefit-Cost Ratio (BCR)**
$$BCR = \frac{PV(\text{Benefits})}{PV(\text{Costs})}$$

**Uniform Gradient Cash Flow**
$$PW = A_1 \times (P/A, i, n) + G \times (P/G, i, n)$$

### Decision Rules
- **PW > 0**: Accept project
- **FW > 0**: Accept project
- **AW > 0**: Accept project
- **IRR > MARR**: Accept project
- **BCR > 1**: Accept project

---

## Unit 3: Activity Planning & Scheduling

### Work Breakdown Structure (WBS)
- Hierarchical decomposition of total scope
- Levels: Project → Phase → Deliverable → Work Package
- **100% Rule**: child elements = parent element

### Gantt Chart (Bar Chart)
- Horizontal bars show task duration
- Shows: start/end dates, dependencies, progress
- **Limitation**: does not show inter-task relationships

### Network Planning Models

| Method | Deterministic? | Key Feature |
|--------|---------------|-------------|
| **CPM** | Yes (fixed durations) | Finds critical path, cost-time tradeoff |
| **PERT** | No (probabilistic) | Uses 3 time estimates, Z-values for risk |
| **PDM** | Yes | Uses 4 dependency types (FS, FF, SS, SF) |

### CPM Formulas
- **ES** (Early Start) = max(EF of all predecessors)
- **EF** (Early Finish) = ES + Duration
- **LF** (Late Finish) = min(LS of all successors)
- **LS** (Late Start) = LF − Duration
- **Float** = LS − ES = LF − EF
- **Critical Path**: path with Float = 0

### PERT Formulas
$$t_e = \frac{a + 4m + b}{6}$$
$$\sigma^2 = \left(\frac{b - a}{6}\right)^2$$

Where: $a$ = optimistic, $m$ = most likely, $b$ = pessimistic

### Shortening Project Duration
1. Identify critical path
2. Reduce duration of critical activities
3. Consider cost-time tradeoff (crash cost vs. savings)
4. Re-evaluate network (new critical paths may emerge)

---

## Unit 4: Risk Management

### Risk Categories
| Type | Example |
|------|---------|
| **Technical** | New technology, unclear requirements |
| **Cost** | Budget overruns, estimation errors |
| **Schedule** | Unrealistic deadlines |
| **Staffing** | Key person leaves |
| **Organizational** | Politics, shifting priorities |

### Risk Analysis (PERT Z-value)
$$Z = \frac{T_S - T_E}{\sigma_{path}}$$

Where:
- $T_S$ = scheduled completion time
- $T_E$ = expected completion time (sum of $t_e$ on path)
- $\sigma_{path} = \sqrt{\sum \sigma^2}$ (sum of variances on path)

### Z-Table Interpretation
| Z Value | Probability of Meeting Deadline |
|---------|--------------------------------|
| 0.0 | 50% |
| 1.0 | 84% |
| 1.28 | 90% |
| 1.645 | 95% |
| 2.0 | 97.7% |
| 3.0 | 99.9% |

### Risk Response Strategies
- **Avoid** — eliminate the threat
- **Transfer** — shift risk to third party (insurance, outsourcing)
- **Mitigate** — reduce probability or impact
- **Accept** — acknowledge and prepare contingency

---

## Unit 5: Resource Allocation

### Resource Types
- **Staff** — developers, testers, managers
- **Equipment** — hardware, tools, licenses
- **Facilities** — offices, labs
- **Materials** — documentation, media

### Resource Allocation Process
1. Identify resource requirements per activity
2. Estimate resource availability
3. Assign resources to activities
4. Resolve conflicts (resource leveling)

### Resource Smoothing
- Adjusts activities within their **float**
- Does **not** extend project duration
- Keeps resource usage within limits

### Resource Balancing
- May **extend** project duration
- Resolves resource over-allocation
- Priority: critical activities first

---

## Unit 6: Monitoring & Control

### Data Collection Methods
- **Timesheets** — weekly effort tracking
- **Status reports** — periodic progress updates
- **Milestones** — checkpoint reviews
- **Walkthroughs** — informal reviews

### Earned Value Analysis

| Metric | Formula | Meaning |
|--------|---------|---------|
| **PV** (Planned Value) | — | Budgeted cost of work scheduled |
| **EV** (Earned Value) | — | Budgeted cost of work performed |
| **AC** (Actual Cost) | — | Actual cost of work performed |
| **SV** (Schedule Variance) | $EV - PV$ | > 0 = ahead of schedule |
| **CV** (Cost Variance) | $EV - AC$ | > 0 = under budget |
| **SPI** (Schedule Performance Index) | $EV / PV$ | > 1 = ahead |
| **CPI** (Cost Performance Index) | $EV / AC$ | > 1 = under budget |
| **EAC** (Estimate at Completion) | $BAC / CPI$ | Revised total cost estimate |
| **ETC** (Estimate to Complete) | $EAC - AC$ | Remaining cost |
| **VAC** (Variance at Completion) | $BAC - EAC$ | Expected over/under |

### Project Control
- Compare actual vs. planned
- Take corrective action if variances exceed thresholds
- Update plans and communicate changes

---

## Unit 7: Managing Contracts & People

### Contract Types

| Type | Risk to Buyer | Risk to Seller |
|------|--------------|----------------|
| **FP (Fixed Price)** | Low | High |
| **CP (Cost Plus)** | High | Low |
| **T&M (Time & Material)** | Medium | Medium |

### FP Variants
- **Firm Fixed Price (FFP)** — price set at contract start
- **Fixed Price Incentive (FPIF)** — incentives for meeting targets
- **Fixed Price with Economic Price Adjustment (FP-EPA)** — adjusts for inflation

### CP Variants
- **CPFF** — Cost Plus Fixed Fee
- **CPIF** — Cost Plus Incentive Fee
- **CPAF** — Cost Plus Award Fee

### Contract Stages
1. **Planning** — define requirements, budget
2. **Solicitation** — invite bids
3. **Selection** — evaluate proposals, choose vendor
4. **Negotiation** — agree on terms
5. **Administration** — monitor performance, manage changes
6. **Closeout** — final delivery, payment, lessons learned

### Managing People — Key Concepts
- **Maslow's Hierarchy**: Physiological → Safety → Social → Esteem → Self-actualization
- **Herzberg's Theory**: Hygiene factors (prevent dissatisfaction) vs. Motivators (drive satisfaction)
- **Types of Power**: Legitimate, Reward, Coercive, Expert, Referent
- **Leadership Styles**: Autocratic, Democratic, Laissez-faire

### Organizational Structures
| Structure | PM Authority | Resource Availability |
|-----------|-------------|----------------------|
| **Functional** | Low/None | Little/None |
| **Matrix (Weak)** | Low | Limited |
| **Matrix (Balanced)** | Moderate | Moderate |
| **Matrix (Strong)** | High | High |
| **Projectized** | High/Total | High/Total |

---

## Unit 8: SQA & Testing

### Testing Principles
1. Testing shows presence of defects, not absence
2. Exhaustive testing is impossible
3. Early testing saves time and cost
4. Defects cluster together (Pareto principle)
5. Pesticide paradox — repeat tests find fewer bugs
6. Testing is context-dependent
7. Absence-of-errors fallacy

### Test Levels
| Level | Who Tests | Focus |
|-------|----------|-------|
| **Unit** | Developers | Individual modules |
| **Integration** | Developers/Testers | Module interactions |
| **System** | Testers | Complete system |
| **Acceptance** | Users/Business | Business requirements |

### Test Strategies
- **Top-down** — stubs replace lower modules
- **Bottom-up** — drivers replace upper modules
- **Sandwich** — combination of both

### V-Model
```
Requirements ←→ Acceptance Testing
Design ←→ System Testing
Architecture ←→ Integration Testing
Module Design ←→ Unit Testing
```

### Verification vs. Validation
- **Verification**: "Are we building the product right?" (reviews, inspections)
- **Validation**: "Are we building the right product?" (testing)

### Software Quality (ISO 9126)
- **Functionality** — does it do what it should?
- **Reliability** — fault tolerance, recovery
- **Usability** — ease of use
- **Efficiency** — performance
- **Maintainability** — ease of change
- **Portability** — transferability

### SEI-CMM Levels
| Level | Name | Key Process Area |
|-------|------|-----------------|
| 1 | Initial | Ad hoc, chaotic |
| 2 | Repeatable | Requirements management, project planning |
| 3 | Defined | Organization-wide standards |
| 4 | Managed | Quantitative quality management |
| 5 | Optimizing | Continuous process improvement |

### SQA Activities
- Quality planning
- Technical reviews
- Testing
- Defect tracking
- Process improvement
- Configuration management

### SQA Plan Contents
- Purpose, scope, activities
- Standards and procedures
- Reviews and audits
- Test plan
- Defect reporting
- Tools and techniques

---

## Unit 9: Software Configuration Management

### Why SCM?
- Track changes across versions
- Enable parallel development
- Ensure consistency
- Support release management

### SCM Basics
- **Configuration Item (CI)** — any work product under SCM control
- **Baseline** — approved version of a CI
- **Repository** — central storage for CIs
- **Version** — specific revision of a CI

### SCM Activities
1. **Identification** — name and label CIs
2. **Version Control** — manage revisions
3. **Change Control** — formal process for changes
4. **Status Accounting** — report CI status
5. **Verification & Audit** — ensure completeness

### Branching Strategies
- **Trunk-based** — single main line, short-lived branches
- **Git Flow** — main, develop, feature, release, hotfix branches
- **Feature flags** — toggle features without branching

---

## Quick Reference: Key Formulas

| Formula | Equation |
|---------|----------|
| PERT Expected Time | $t_e = \frac{a + 4m + b}{6}$ |
| PERT Variance | $\sigma^2 = (\frac{b-a}{6})^2$ |
| Present Worth | $PW = \sum \frac{F_t}{(1+i)^t}$ |
| Future Worth | $FW = PW \times (1+i)^n$ |
| Annual Worth | $AW = PW \times \frac{i(1+i)^n}{(1+i)^n-1}$ |
| Schedule Variance | $SV = EV - PV$ |
| Cost Variance | $CV = EV - AC$ |
| SPI | $SPI = EV / PV$ |
| CPI | $CPI = EV / AC$ |
| EAC | $EAC = BAC / CPI$ |
| Z-Score | $Z = \frac{T_S - T_E}{\sigma_{path}}$ |
| Float | $Float = LS - ES = LF - EF$ |
