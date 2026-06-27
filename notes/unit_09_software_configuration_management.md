# Unit 09: Software Configuration Management

> **Hours:** 3 Hrs. | **Source:** `Chapter_9_Software Configuration Management.pdf`

---

## Table of Contents

- [1. Introduction to SCM](#1-introduction-to-scm)
  - [1.1 The Four Aspects of Software Evolution](#1-1-the-four-aspects-of-software-evolution)
  - [1.2 The Case for Change Management](#1-2-the-case-for-change-management)
- [2. Need for SCM](#2-need-for-scm)
  - [2.1 Why SCM is Important](#2-1-why-scm-is-important)
  - [2.2 Benefits of Good SCM](#2-2-benefits-of-good-scm)
- [3. Basic Configuration Management](#3-basic-configuration-management)
- [4. SCM Roles and Responsibilities](#4-scm-roles-and-responsibilities)
  - [4.1 Roles in SCM](#4-1-roles-in-scm)
  - [4.2 Responsibilities of SCM](#4-2-responsibilities-of-scm)
- [5. Management Responsibilities](#5-management-responsibilities)
  - [5.1 The Five Functions of Management](#5-1-the-five-functions-of-management)
- [6. Baseline](#6-baseline)
  - [6.1 Key Characteristics](#6-1-key-characteristics)
  - [6.2 When Baselines Are Established](#6-2-when-baselines-are-established)
- [7. Quick Revision Summary](#7-quick-revision-summary)

---

## 1. Introduction to SCM

> **Definition:**
> **Software Configuration Management (SCM)** is the practice of identifying, organizing, and controlling changes to software and related artifacts throughout the SDLC — ensuring traceability, accountability, and the ability to revert to known safe states.

> 💡 **Why This Matters:** Without SCM, a team of 10 developers working on the same codebase would overwrite each other's work, lose track of which version is deployed, and have no way to roll back a bad change. SCM is the **safety net** of software engineering.

**The First Law of System Engineering:**
> "*No matter where you are in the system life cycle, the system will change, and the desire to change it will persist throughout the life cycle.*"

### 1.1 The Four Aspects of Software Evolution

| Type | Description | Software Example | Everyday Analogy |
|------|-------------|-----------------|------------------|
| **Corrective changes** | Required to maintain control over the system's day-to-day functions. Made as *faults* or *bugs* are found during development. Some changes may be long-term and fundamental; some may be *patches* to keep the system in operation (emergency fixes). | Fixing a login bug where valid users get "Access Denied" | **Fixing a leaky faucet** — the pipe worked before, now it doesn't |
| **Adaptive changes** | Essentially maintaining control over system modifications. As one part of the system changes, other impacted areas will need to be updated. | Upgrading from MySQL 5.7 to MySQL 8.0; updating code to use new Python 3.12 features | **Upgrading your phone** — apps need updates to work on the new OS |
| **Perfective changes** | The domain of *refactoring* designs falls into this category. Done to increase the long-term maintainability or elegance of the solution. | Refactoring a 500-line function into 5 smaller functions; rewriting documentation for clarity | **Rearranging your kitchen** — same tools, better layout, easier to cook |
| **Preventive changes** | Preventing the system performance from degrading to unacceptable levels. Involves alterations made to ensure that the system has a defense against potential failures. | Adding input validation to prevent SQL injection; setting up database replication for disaster recovery | **Getting a flu shot** — nothing is broken yet, but you're protecting against future problems |

> 🧠 **Memory Aid — CAP-P (pronounced "CAP"):**
> - **C**orrective — Fix what's broken
> - **A**daptive — Adapt to new environment
> - **P**erfective — Make it better
> - **P**reventive — Stop future problems

### 1.2 The Case for Change Management

If changes are **not controlled** in a project — things can and will get out of hand. The issue of *change management* is even more important when multiple people work on a project as well as on the same deliverable. Without proper strategies and mechanisms to control changes, one can never *revert back* to an older, more stable copy of the software. **Important:** every change introduces risk into the project.

| **The Facts** | **The Solution** |
|---------------|-------------------|
| Change is unavoidable in software | **Software Configuration Management (SCM)** |
| Changes need to be controlled | |
| Changes need to be managed | |

**SCM includes activities such as:**
- Version control
- Build management
- Release management
- Change management
- Configuration management

---

## 2. Need for SCM

As software evolves, many resources make changes to the system.

### 2.1 Why SCM is Important

- **CM prevents** avoidable errors that arise from *conflicting changes*.
- Often many versions of the software are released and require support — **CM allows a team to support many versions**.
- **CM allows changes in sequential versions to be propagated**.
- CM allows developers to track changes and *reverse any fatal changes* to take a software system back to its *last known safe state*.

### 2.2 Benefits of Good SCM

Good SCM **increases confidence** that we are:

- Building the *right system*
- *Testing* the system enough
- Changing it *correctly and carefully*

It also:

- Restrains *non-essential* changes
- Ensures that decisions and changes are *traceable*
- **Increases accountability**
- **Improves overall software quality**
- **Provides a fall back position** when things do not work

> ⚠️ **Important:** Without proper change management strategies, one can never revert back to an older, more stable copy of the software. Every change introduces risk into the project.

---

## 3. Basic Configuration Management

The basic configuration of SCM involves the following **7 steps**:

1. **Identify Configuration Items** — Identify configuration items such as source code, documentation, requirements, design, etc.
2. **Define the Repository Structure** — This may include creating a folder structure that reflects the organization of software artifacts.
3. **Choose a Version Control System** — Choose any version control system from popular ones like **Git**.
4. **Establish a Baseline** — Establish a baseline or a starting point of the software development process.
5. **Create a Change Management Process** — It outlines the procedures for making changes to the configuration items.
6. **Set up Build and Release Management** — It involves building the software and releasing it to users.
7. **Define Access Control and Security** — This may involve defining user roles and permissions, establishing password policies, and procedures for granting access, etc.

> **Definition:** **Configuration Items (CIs)** are software artifacts placed under SCM control — including source code, documentation, requirements, design specs, and test cases — each with a unique identifier for version tracking.

> 💡 **Real-World Example — Setting Up SCM for a Student Project:**
>
> A team of 4 students is building a Library Management System. Here's how they apply the 7 steps:
>
> | Step | What They Do |
> |------|-------------|
> | **1. Identify CIs** | Source code (.py files), database schema, UI mockups, requirements doc, test cases |
> | **2. Define Repository Structure** | Create folders: `/docs`, `/src`, `/tests`, `/sql` — all under a single project root |
> | **3. Choose VCS** | They set up a Git repository on GitHub with a `main` branch and a `develop` branch |
> | **4. Establish Baseline** | After finishing the requirements doc, they tag it as `v1.0-req-baseline` |
> | **5. Create Change Mgmt** | For any change, a team member creates a GitHub Issue → gets approval → creates a branch → makes changes → submits a Pull Request |
> | **6. Build & Release** | They set up a simple script that packages the code into a `.zip` for each release |
> | **7. Access Control** | Only the team lead can merge to `main`; everyone can create branches |

---

## 4. SCM Roles and Responsibilities

### 4.1 Roles in SCM

| Role | Responsibilities |
|------|-----------------|
| **Configuration Manager** | The head who is responsible for identifying configuration items. Ensures the team follows the SCM process. |
| **Developer** | Needs to change the code as per standard development activities or change requests. Responsible for maintaining configuration of code. Should check the changes and resolve conflicts. |
| **Auditor** | Responsible for SCM audits and reviews. Must ensure the consistency and completeness of release. |
| **User** | The end user should understand the key SCM terms to ensure they have the *latest version* of the software. |

> 🧠 **Memory Aid — Roles by Authority Level:**
> - **Config Manager** = *Librarian* — organizes, labels, enforces rules
> - **Developer** = *Author* — writes and revises content
> - **Auditor** = *Editor* — checks correctness and completeness
> - **User** = *Reader* — consumes the final product

### 4.2 Responsibilities of SCM

| Responsibility | Description |
|---------------|-------------|
| **Version Control** | Implementing and maintaining the version control system, and ensuring that developers are using it correctly. |
| **Baseline Management** | Creating and maintaining baselines of the software configuration items, and ensuring that they are properly labeled and stored in the repository. |
| **Change Management** | Establishing and maintaining the change management process, including defining the procedures for making changes to the software. |
| **Build and Release Management** | Managing the build and release process, including defining the build and release procedures. |
| **Branching and Merging** | Managing the branching and merging of code and ensuring that developers are following the best practices for branching and merging. |
| **Access Control and Security** | Managing access control and security for the SCM repository and ensuring that the appropriate security measures are in place to protect the software project. |

> ⭐ **Key Takeaway:** SCM roles ensure accountability and traceability. The **Configuration Manager** oversees the process, **Developers** implement changes, **Auditors** verify consistency, and **Users** validate the final product.

---

## 5. Management Responsibilities

> **Definition:** **Management Functions** are the core activities managers perform — planning, organizing, staffing, directing, and controlling — to guide the project team toward successful completion.

### 5.1 The Five Functions of Management

| Function | Description |
|----------|-------------|
| **Planning** | It sets the *road map* for the development of the project along with assumed risks and solutions. |
| **Organizing** | Here we put the plan into action by establishing a system of *hierarchy* to carry out developmental tasks. |
| **Staffing** | Here we assign tasks based on each team member's *knowledge, skills, and abilities*. Also, hire new staff if needed. |
| **Directing** | It is concerned with *supervising* the team's progress. Here we must keep an open channel of *communication* and get regular updates to stay on top of things. |
| **Controlling** | It is concerned with *measuring* the progress of each step established in the planning stage against our organizational goals. It helps to *coordinate* with employees to ensure that they are moving in the right direction in the right manner. |

---

## 6. Baseline

> **Definition:**
> A **Baseline** is a formally reviewed and agreed-upon version of a configuration item that serves as a fixed reference point for further development — changeable only through formal change control procedures.

> 💡 **Baseline Timeline Example:**
>
> ```
> Time ──────────────────────────────────────────────────────────────►
>
> [Req Review]────[Design Review]────[Code Freeze]────[Release]
>      |                 |                 |               |
>      ▼                 ▼                 ▼               ▼
>  Functional        Design            Product          Release
>  Baseline          Baseline          Baseline          Baseline
>  (SRS frozen)      (Architecture      (All code        (v1.0 shipped
>                     approved)          reviewed)        to client)
> ```
>
> After each baseline, any change requires a **formal change request** — no more "quick fixes."

### 6.1 Key Characteristics

- Before a software configuration item becomes a baseline, changes may be made *quick and informal*.
- However, once a baseline is established, we figuratively pass through a *swinging one-way door*.
- Changes can be made, but a **specific, formal procedure** must be applied to evaluate and verify each change.

### 6.2 When Baselines Are Established

A baseline is typically established at a *significant point* in the development process, such as:
- After completing a major *milestone*
- Before making *significant changes* to the software

Once a baseline is established, it is:
- Stored in the **SCM repository**
- Used as a *future reference* for further development work

> ⚠️ **Important:** A baseline can only be changed through **formal change control procedures**. This ensures that all modifications are evaluated, verified, and documented before being applied.

> ⭐ **Key Takeaway:** Baselines provide a *stable foundation* for development. They mark formal review points and ensure that all changes are traceable and controlled.

---

## 7. Quick Revision Summary

| Topic | Key Points |
|-------|------------|
| **First Law of System Engineering** | Systems will always change; desire to change persists throughout the life cycle. |
| **Four Types of Changes** | **Corrective** (bug fixes), **Adaptive** (environment changes), **Perfective** (refactoring/enhancement), **Preventive** (degradation prevention) |
| **SCM Definition** | Practice of identifying, organizing, and controlling changes to software and related objects throughout the SDLC. |
| **Need for SCM** | Prevents conflicting changes, supports multiple versions, enables rollback, increases confidence and accountability. |
| **Basic CM Steps (7)** | Identify CIs → Define Repository Structure → Choose VCS → Establish Baseline → Create Change Management Process → Set up Build/Release → Define Access Control |
| **SCM Roles** | **Configuration Manager** (process owner), **Developer** (code changes), **Auditor** (compliance/review), **User** (latest version) |
| **SCM Responsibilities** | Version Control, Baseline Management, Change Management, Build & Release Management, Branching & Merging, Access Control & Security |
| **Management Functions (5)** | **Planning** (road map), **Organizing** (hierarchy), **Staffing** (assign tasks), **Directing** (supervise), **Controlling** (measure progress) |
| **Baseline** | Formally reviewed & agreed-upon specification; changed only through formal change control procedures; stored in SCM repository. |

## Past Exam Questions

**2082 Q7.** Explain the purposes of Software Configuration Management.

**Answer:** **Software Configuration Management (SCM)** is the process of identifying, organizing, and controlling changes to software throughout its lifecycle. The purposes of SCM are: (1) **Identify configuration items** — uniquely identifying all components (code, documents, data, tools) that need to be managed; (2) **Control changes** — ensuring changes are evaluated, approved, and tracked systematically; (3) **Maintain integrity** — ensuring that the system remains consistent as changes are made; (4) **Traceability** — maintaining the relationship between requirements, design, code, and tests across versions; (5) **Reproducible builds** — enabling any previous version of the software to be reconstructed; (6) **Team coordination** — preventing conflicting changes when multiple developers work on the same code.

**2081 Q10.** Explain the responsibilities of configuration management.

**Answer:** Configuration management responsibilities include: (1) **Configuration Identification** — uniquely identifying and labeling all configuration items (source code, documents, data files, tools); (2) **Configuration Control** — managing changes through a formal process involving change requests, impact analysis, approval, and implementation; (3) **Configuration Status Accounting** — recording and reporting the status of all configuration items and change requests at all times; (4) **Configuration Auditing** — verifying that the system conforms to its configuration documentation; (5) **Version Control** — managing multiple versions of configuration items and controlling concurrent access; (6) **Build Management** — ensuring consistent and repeatable builds of the system from controlled components.

**2081 Q12a.** Write short note on baseline.

**Answer:** A **baseline** is a formally approved version of a configuration item that serves as a fixed reference point for future changes. Common baselines in software projects: **Functional Baseline** — approved requirements specification; **Allocated Baseline** — approved design specification; **Product Baseline** — approved tested product ready for delivery. Once baselined, changes to an item must go through a formal change control process. Baselines enable rollback to known good states, provide traceability from requirements to code, and serve as checkpoints for project reviews and audits.

**2080 Q10.** How does SCM help in change control and version control?

**Answer:** SCM helps in **change control** by providing a formal process: (1) Change request submitted; (2) Impact analysis performed (cost, schedule, technical impact); (3) Change Control Board (CCB) reviews and approves/rejects; (4) Approved changes are implemented against the checked-out baseline; (5) Changes are tested and the new version is baselined. SCM helps in **version control** by: (1) Tracking all versions of every configuration item; (2) Preventing simultaneous editing conflicts through check-in/check-out mechanisms; (3) Maintaining version history for audit and rollback; (4) Supporting branching and merging for parallel development; (5) Tagging/labeling versions for release management.

**2079 Q10.** What is a baseline? Why is SCM critical for software projects?

**Answer:** A **baseline** is a formally reviewed and agreed-upon version of a configuration item that serves as a fixed reference point. Once baselined, changes require formal approval through the change control process. **SCM is critical** because software is uniquely **invisible** (changes may go unnoticed) and **flexible** (easy to make changes, making uncontrolled changes common). Without SCM: multiple developers may overwrite each other's work, debugging becomes impossible because the exact version that caused the error is unknown, released systems cannot be reproduced for maintenance. SCM provides the discipline needed to manage software evolution reliably.

**2078 Q10.** Explain SCM process in detail.

**Answer:** The **SCM process** consists of the following steps: (1) **Planning** — create a Configuration Management Plan defining what items will be managed, naming conventions, tools, and processes; (2) **Identification** — identify all Configuration Items (CIs) that need to be controlled and assign unique identifiers — includes source files, documents, models, test data, build scripts, and tools; (3) **Version Control** — manage access to CIs through a repository with check-in/check-out, version labeling, branching, and merging capabilities; (4) **Change Control** — formal process for evaluating and coordinating changes: Change Request → Impact Analysis → CCB Approval → Implementation → Re-verification → New Baseline; (5) **Status Accounting** — maintain records of all CIs and their current status — what versions exist, which is the current baseline, what changes are pending; (6) **Auditing** — periodically verify that the actual product matches its documentation and that approved processes are being followed; (7) **Release Management** — build and package software for delivery, ensuring all components come from the correct, approved versions.

## Glossary

| Term | Definition |
|------|-----------|
| **SCM** | Software Configuration Management — practice of identifying, organizing, and controlling changes throughout the SDLC |
| **Configuration Item (CI)** | Any work product (code, docs, test cases) placed under SCM control |
| **Baseline** | Formally reviewed and agreed-upon version of a CI that serves as a reference point |
| **Version Control** | System for managing revisions to configuration items |
| **Change Management** | Formal process for evaluating, approving, and implementing changes |
| **Build Management** | Process of compiling and assembling software from source code |
| **Release Management** | Process of packaging and distributing software versions to users |
| **Repository** | Central storage location for configuration items and their histories |
| **Configuration Manager** | Person responsible for defining CIs and ensuring team follows SCM process |
| **Corrective Change** | Change made to fix faults or bugs |
| **Adaptive Change** | Change made to accommodate environmental changes |
| **Perfective Change** | Change made to improve maintainability or performance |
| **Preventive Change** | Change made to prevent future degradation or failures |
