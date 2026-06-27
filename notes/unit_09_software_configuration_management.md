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
> **Software Configuration Management (SCM)** is the practice of identifying, organizing, and controlling changes to the software and related objects throughout the software development life cycle. SCM is a critical process for ensuring that software products are developed, tested, and released in a controlled and predictable manner, and that changes to the software are tracked and managed efficiently.

**The First Law of System Engineering:**
> "*No matter where you are in the system life cycle, the system will change, and the desire to change it will persist throughout the life cycle.*"

### 1.1 The Four Aspects of Software Evolution

| Type | Description | Examples |
|------|-------------|----------|
| **Corrective changes** | Required to maintain control over the system's day-to-day functions. Made as *faults* or *bugs* are found during development. Some changes may be long-term and fundamental; some may be *patches* to keep the system in operation (emergency fixes). | Bug fixes, emergency patches |
| **Adaptive changes** | Essentially maintaining control over system modifications. As one part of the system changes, other impacted areas will need to be updated. | Database upgrades, use of a new compiler or development tool |
| **Perfective changes** | The domain of *refactoring* designs falls into this category. Done to increase the long-term maintainability or elegance of the solution. | Changes to design or data structures for better efficiency, updates to documentation to improve quality, enhancing code to make it more readable |
| **Preventive changes** | Preventing the system performance from degrading to unacceptable levels. Involves alterations made to ensure that the system has a defense against potential failures. | System hardening, performance monitoring, fault tolerance improvements |

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

> **Definition:**
> **Configuration Items (CIs)** — Components of the software that need to be managed, such as source code, documentation, requirements, and design artifacts.

---

## 4. SCM Roles and Responsibilities

### 4.1 Roles in SCM

| Role | Responsibilities |
|------|-----------------|
| **Configuration Manager** | The head who is responsible for identifying configuration items. Ensures the team follows the SCM process. |
| **Developer** | Needs to change the code as per standard development activities or change requests. Responsible for maintaining configuration of code. Should check the changes and resolve conflicts. |
| **Auditor** | Responsible for SCM audits and reviews. Must ensure the consistency and completeness of release. |
| **User** | The end user should understand the key SCM terms to ensure they have the *latest version* of the software. |

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

> **Definition:** The *function of management* helps us to stay informed about what we need to do and how staff can be guided accordingly.

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
> A **Baseline** is a specification or product that has been *formally reviewed and agreed upon*, that thereafter serves as the basis for further development, and that can be changed only through formal change control procedures.

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
