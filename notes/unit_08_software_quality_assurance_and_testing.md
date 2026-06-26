# Unit 08: Software Quality Assurance and Testing

> **Hours:** 5 Hrs. | **Source:** `Chapter_8_ Software Quality Assurance and Testing.pdf`

---

## Table of Contents

- [1. Testing Principles and Objectives](#1-testing-principles-and-objectives)
- [2. Testing vs Verification vs Validation vs Debugging](#2-testing-vs-verification-vs-validation-vs-debugging)
- [3. Manual Testing vs Automation Testing](#3-manual-testing-vs-automation-testing)
- [4. Levels of Testing](#4-levels-of-testing)
- [5. Test Strategies](#5-test-strategies)
- [6. Test Plan and Test Case](#6-test-plan-and-test-case)
- [7. Verification and Validation](#7-verification-and-validation)
- [8. Software Quality](#8-software-quality)
- [9. Software Quality Assurance (SQA)](#9-software-quality-assurance-sqa)
- [10. SEI-CMM (Capability Maturity Model)](#10-sei-cmm-capability-maturity-model)
- [11. SQA Activities and Plan](#11-sqa-activities-and-plan)
- [12. Mission of SEI](#12-mission-of-sei)
- [Quick Revision Summary](#quick-revision-summary)

---

## 1. Testing Principles and Objectives

> **Definition:** **Testing** is the execution of a program to find its faults. It is an iterative process carried out in conjunction with implementation — the most common way of checking that software meets its specification and does what the customer wants.

Testing is a critical element of **Software Quality Assurance** and represents the ultimate review of specification, design, and code generation. An investigation conducted to provide stakeholders with information about the quality of the product or service under test.

### Objectives of Testing

- To demonstrate to the developer and the customer that the software meets its requirements
- Finding defects which may get created by the programmer while developing the software
- Gaining confidence in and providing information about the level of quality
- To make sure that the end result meets the business and user requirements
- To ensure that it satisfies **Business Requirement Specification** and **System Requirement Specification (SRS)**
- To gain the confidence of the customers by providing them a quality product

### Principles of Testing (Standard Principles)

1. **Testing shows the presence of defects**

  * Testing can reveal bugs but **cannot prove their absence**

2. **Exhaustive testing is impossible**

  * It is not feasible to test all inputs and conditions
  * Example: 10 alphabetic characters → **26¹⁰ (~141 trillion combinations)**
  * 1 test per microsecond → **~4.5 million years**

3. **Early testing (Shift Left)**

  * Testing should begin as early as possible
  * Early detection reduces **cost and effort**

4. **Defect clustering (Pareto Principle)**

  * Around **80% of defects are found in 20% of components**

5. **Pesticide paradox**

  * Repeating the same tests finds fewer new defects
  * Test cases should be **regularly reviewed and updated**

6. **Testing is context-dependent**

  * Different systems require different testing approaches

7. **Absence-of-errors fallacy**

  * Software without defects is useless if it **does not meet user requirements**

---

### 🧠 Mnemonic (Exam Use)

**P-E-E-D-P-T-A**

* **P** → Presence of defects
* **E** → Exhaustive testing impossible
* **E** → Early testing
* **D** → Defect clustering
* **P** → Pesticide paradox
* **T** → Testing is context-dependent
* **A** → Absence-of-errors fallacy

---


> ⚠️ **Important:** Exhaustive testing is impossible. Effective testing depends on selecting a **small, high-impact subset of test cases** and removing as many defects as possible *before* testing begins.

---

## 2. Testing vs Verification vs Validation vs Debugging

| Concept | Definition |
|---------|-----------|
| **Testing** | The execution of a program to find its faults |
| **Verification** | The process of proving the program's correctness |
| **Validation** | The process of finding errors by executing the program in a real environment |
| **Debugging** | Diagnosing the error and correcting it |

Testing is done to improve:
- **Quality**
- **Verify and validate**
- **Reliability estimation**

> ⚠️ **Important:** Testing and debugging are **different activities**. Debugging must be accommodated in *any* testing strategy. Make a clear distinction between **verification** ("are we building the product right?") and **validation** ("are we building the right product?").

---

## 3. Manual Testing vs Automation Testing

| Aspect | Manual Testing | Automation Testing |
|--------|---------------|-------------------|
| **Approach** | Testing the software manually without using any automated tool or script | Testing by writing scripts and using another software to test the software |
| **Role of Tester** | Tester takes over the role of an end-user and tests the software to identify unexpected behavior or bugs | Tester writes scripts that automate the manual process |
| **Reusability** | Must be re-executed manually each time | Can re-run test scenarios quickly and repeatedly |
| **Speed** | Slower | Faster |
| **Best For** | Exploratory, usability, and ad-hoc testing | Regression testing, repeated execution |

---

## 4. Levels of Testing

Testing levels are the procedure for finding missing areas and avoiding overlapping and repetition between the development life cycle stages. In software testing, we have four different levels:

| Level | Description | Performed By | Purpose |
|-------|-------------|-------------|---------|
| **Unit Testing** | Tests for a single component or a single unit | Developer | Validate the performance of unit components |
| **Integration Testing** | Combining different software modules and testing as a group | Testers | Ensure the integrated system is ready for system testing |
| **System Testing** | Final test to identify that the system meets specification and criteria | Testers | Evaluate both function and non-functional needs |
| **Acceptance Testing** | Evaluate whether the system complies with end-user requirements | QA Team / Users | Determine if the system is ready for deployment |

---

### 4.1 Unit Testing

- Uses tests for a **single component** or a **single unit** in software testing
- Performed by the **developer**
- First level of *functional testing*
- **Primary goal:** Validate the performance of unit components
- **Unit** is the smallest testable portion of the system or application
- **Main aim:** Test that each component/unit is correct, fulfilling requirements and desired functionality

### 4.2 Integration Testing

- Combining different software modules and phases and testing as a **group**
- Ensures the integrated system is ready for system testing
- Tests how different components function at their **interface**
- Performed by **testers**
- Finds the **data flow** from one module to other modules

### 4.3 System Testing

- Most probably the **final test** to identify that the system meets the specification and criteria
- Evaluates both **functional** and **non-functional** needs
- Allows checking the system's compliance as per requirements
- All components are tested as a **whole**
- Involves: **load**, **reliability**, **performance**, and **security testing**
- Very important step — software is almost ready for production
- Tested in an environment very close to the **market/user-friendly environment**

### 4.4 Acceptance Testing

- Aims to evaluate whether the system complies with **end-user requirements** and is ready for **deployment**
- Uses pre-written scenarios and test cases
- QA/testing team can find out how the product will perform when installed on the user's system
- Ranges from easily finding **spelling mistakes** and **cosmetic errors** to **major bugs** that could cause major errors

> ⭐ **Key Takeaways — Levels of Testing:**
> - Testing progresses from **small (unit)** → **grouped (integration)** → **whole system (system)** → **user-ready (acceptance)**
> - Each level has a distinct goal, performer, and scope
> - System testing includes non-functional aspects (load, reliability, performance, security)

---

## 5. Test Strategies

A strategy for software testing must accommodate:
- **Low-level tests** — verify that a small source code segment has been correctly implemented
- **High-level tests** — validate major system functions against customer requirements

A strategy must provide:
- **Guidance** for the practitioner
- **A set of milestones** for the manager

Because testing occurs when deadline pressure rises, progress must be measurable and problems must surface as early as possible.

| Strategy | Description | Focus |
|----------|-------------|-------|
| **Static Test Strategy** | Evaluates quality without actually running the system; looks at portions or system elements to detect problems early | Saves time and money by detecting problems early |
| **Structural Test Strategy** | Needs to be operated on real devices; system must run in its entirety to find all bugs; often run on individual components and interfaces | Identifies localized errors in data flows |
| **Behavioral Test Strategy** | Focuses on **how** a system acts rather than the mechanism behind its functions | Workflows, configurations, performance, user journey |

Key points about test strategies:
- Testing begins at the **component level** and works outward toward integration of the entire computer-based system
- Different testing techniques are appropriate at **different points in time**
- The developer conducts testing and may be assisted by **independent test groups** for large projects
- The role of the **independent tester** is to remove the conflict of interest inherent when the builder tests their own product
- Testing and debugging are **different activities** — debugging must be accommodated in any testing strategy

---

## 6. Test Plan and Test Case

### Test Case

> **Definition:** A **test case** in software engineering is a set of conditions or variables under which a tester will determine whether an application or software system is working correctly.

- A rich variety of test case design methods provide the developer with a **systematic approach** to testing
- These methods can help ensure the **completeness of tests** and provide the highest likelihood for uncovering errors
- The mechanism for determining whether a program has passed or failed such a test is known as a **test oracle**

### Test Plan

> **Definition:** A **test plan** is a document detailing a systematic approach to testing a system such as a machine or software.

- Contains a detailed understanding of the eventual workflow
- Documents the strategy used to **verify and ensure** that a product meets its design specifications and other requirements
- Usually prepared by or with significant input from **Test Engineers**

A test plan typically includes:

- Introduction to the Test Plan document
- Assumptions when testing the application
- List of test cases included in testing the application
- List of features to be tested
- What sort of approach to use when testing the software
- List of deliverables that need to be tested
- Resources allocated for testing the application
- Any risks involved during the testing process
- A schedule of tasks and milestones as testing progresses

---

## 7. Verification and Validation

> **Definition:**
> - **Verification** — The set of tasks that ensure that software correctly implements a specific function
> - **Validation** — The set of tasks that ensure that the software that has been built is traceable to customer requirements

### Boehm's Definitions

| Concept | Boehm's Question |
|---------|-----------------|
| **Verification** | *"Are we building the product right?"* |
| **Validation** | *"Are we building the right product?"* |

### Comparison Table

<!-- | Aspect | Verification | Validation |
|--------|-------------|------------|
| **Also Known As** | Static Testing | Dynamic Testing |
| **Key Question** | "Are we building the product right?" | "Are we building the right product?" |
| **Includes** | Business requirements, system requirements, design review, code walkthrough | Functional testing (UT, IT, ST) and non-functional testing (UAT) |
| **Checks** | That the developed application fulfills all requirements given by the client | That the software meets the business needs of the client | -->

| Aspect             | Verification                                                  | Validation                                            |
| ------------------ | -------------------- | ------------------- |
| Key Question       | Are we building the product right?  | Are we building the right product?                    |
| Compared Against   | Requirements, design, specifications | User needs, business goals, intended use              |
| Typical Activities | Requirement reviews, design reviews, code reviews, UT, IT, ST | UAT, beta testing, pilot testing, customer evaluation |
| Nature             | Static **and** dynamic | Mostly dynamic                                        |
| Performed By       | Developers, QA, architects | Customers, users, business stakeholders               |


### V-Model of SDLC

![Verification and Validation](assets/ch08_img_053.png)
![Verification and Validation](assets/ch08_img_054.png)
![Verification and Validation — V-Model](assets/ch08_img_055.jpeg)

The **V-Model** maps verification activities to the left side (planning/review) and validation activities to the right side (execution/testing), demonstrating the parallel relationship between development phases and testing phases.

> ⚠️ **Important:** Verification ensures **process correctness** — "did we build it right?" Validation ensures **product relevance** — "did we build the right thing?" Both are essential for quality.

---

## 8. Software Quality

> **Definition:** **Software quality** is defined as a field of study and practice that describes the desirable attributes of software products. It refers to the degree to which a software product meets its specified requirements and user expectations.

### Software Quality Factors

| Factor | Description |
|--------|-------------|
| **Functionality** | The degree to which the software satisfies stated requirements |
| **Reliability** | The ability of the software to perform without failure under stated conditions |
| **Usability** | The ease with which users can learn and use the software |
| **Efficiency** | The optimal use of system resources by the software |
| **Maintainability** | The ease with which the software can be modified to fix issues or add features |

### According to Deming

> *"The problem inherent in attempts to define the quality of a product, almost any product, were stated by the master Walter A. Shewhart. The difficulty in defining quality is to translate future needs of the user into measurable characteristics, so that a product can be designed and turned out to give satisfaction at a price that the user will pay. This is not easy, and as soon as one feels fairly successful in the endeavor, he finds that the needs of the consumer have changed, competitors have moved in, etc."*

### Methods for Ensuring Software Quality

- **Testing**
- **Code Reviews**
- **Quality Assurance Process**

The goal of these methods is to identify and fix defects and bugs, improve performance, and enhance user satisfaction.

### Key Points

- Quality refers to how well software meets **non-functional requirements** that support the delivery of functional requirements (robustness, maintainability)
- The degree to which the software was produced correctly
- Software must conform to **implicit requirements** (ease of use, maintainability, reliability) as well as its **explicit requirements**

---

## 9. Software Quality Assurance (SQA)

> **Definition:** **Software Quality Assurance (SQA)** consists of a means of monitoring the software engineering processes and methods used to ensure quality. It is the process of evaluating the quality of a product and enforcing commitment to software product standards and procedures.

### Scope of SQA

SQA encompasses the **entire software development process**, including:

- Requirements definition
- Software design
- Coding
- Source code control
- Code reviews
- Change management
- Configuration management
- Testing
- Release management
- Product integration

### Organization of SQA

SQA is organized into:
- **Goals**
- **Commitments**
- **Abilities**
- **Activities**
- **Measurements**
- **Verifications**

### Key Principles

- **Conformance to software requirements** is the foundation from which software quality is measured
- **Specified standards** define the development criteria used to guide how software is engineered
- Software must conform to **implicit requirements** (ease of use, maintainability, reliability) as well as its **explicit requirements**

---

## 10. SEI-CMM (Capability Maturity Model)

### About SEI

> **Definition:** **SEI** (Software Engineering Institute) — The Carnegie Mellon Software Engineering Institute is a federally funded research and development center headquartered on the campus of Carnegie Mellon University in Pittsburgh, Pennsylvania, United States.

**Principal areas of SEI:** Acquisition, process management, risk, security, software development, and system design.

### About CMM

> **Definition:** **CMM** (Capability Maturity Model) is a development model created after study of data collected from organizations that contracted with the U.S. Department of Defense. Its aim is to improve existing software-development processes.

### Five Aspects of CMM

| Aspect | Description |
|--------|-------------|
| **Maturity Levels** | A 5-level process maturity scale where the uppermost (5th) level is a notional ideal state of systematic process optimization and continuous improvement |
| **Key Process Areas** | A cluster of related activities that, when performed together, achieve a set of goals considered important |
| **Goals** | Summarize the states that must exist for a key process area to be implemented effectively; the extent goals are accomplished indicates organizational capability |
| **Common Features** | Practices that implement and institutionalize a key process area (5 types: commitment to perform, ability to perform, activities performed, measurement and analysis, verifying implementation) |
| **Key Practices** | Describe the elements of infrastructure and practice that contribute most effectively to implementation and institutionalization |

### SEI-CMM Maturity Levels

| Level | Name | Characteristics |
|-------|------|----------------|
| **Level 1** | **Initial** | Characterized by periodic efforts required by individuals to successfully complete projects. No formal processes. |
| **Level 2** | **Repeatable** | Software project tracking, requirements management, realistic planning, and configuration management processes are in place; successful practices can be repeated. |
| **Level 3** | **Defined** | Standard software development and maintenance processes are integrated throughout the organization; a **Software Engineering Process Group** is in place; training programs ensure understanding and compliance. |
| **Level 4** | **Managed** | **Metrics** are used to track productivity, processes, and products. Project performance is predictable, and quality is consistently high. |
| **Level 5** | **Optimizing** | The focus is on **continuous process improvement**. The impact of new processes and technologies can be predicted and effectively implemented when required. |

> ⭐ **Key Takeaways — SEI-CMM:**
> - **Level 1 (Initial):** Ad-hoc, individual heroics
> - **Level 2 (Repeatable):** Basic project management, repeatable practices
> - **Level 3 (Defined):** Standardized processes across the organization
> - **Level 4 (Managed):** Quantitative metrics and predictability
> - **Level 5 (Optimizing):** Continuous improvement culture
>
> Each level builds on the previous — an organization must satisfy all goals of a level to advance.

---

## 11. SQA Activities and Plan

### SQA Activities

Formulating a Quality Management Plan includes:
- Applying Software Engineering Techniques
- Conducting Formal Technical Reviews
- Applying a Multi-tiered Testing Strategy
- Enforcing Process Adherence
- Controlling Change
- Measuring Impact of Change
- Performing SQA Audits
- Keeping Records and Reporting

### Organizational Structure

- The organizational structure must provide the QA manager with direct organizational paths into every department
- **Small businesses:** Assign responsibilities to someone in management, give them authority to manage QA matters throughout the company, and create a QA reporting path to the executive level
- Employees continue to report to their department manager for disciplinary and non-QA matters, but report to the QA person on quality questions

![SQA Activities and Plan](assets/ch08_img_056.jpeg)

### SQA Plan

> **Definition:** The **Software Quality Assurance Plan** is a document that outlines the quality assurance strategy and approach for a software development process. It describes the activities, resources, and tools required to ensure the software product meets the specified quality standards and requirements.

### Components of an SQA Plan

| Section | Description |
|---------|-------------|
| **SQA Process** | The overall quality assurance process to be followed |
| **SQA Responsibilities** | Who is responsible for what quality activities |
| **SQA Tools** | Tools to be used in quality assurance |
| **SQA Deliverables** | What QA artifacts will be produced |

### Detailed Sections of SQA Plan

| Section | Contents |
|---------|----------|
| **Management Section** | Describes the place of SQA in the structure of the organization |
| **Documentation Section** | Describes each work product produced as part of the software process |
| **Standards, Practices, and Conventions Section** | Lists all applicable standards/practices applied during the software process and any metrics to be collected |
| **Reviews and Audits Section** | Provides an overview of the approach used in reviews and audits to be conducted during the project |
| **Problem Reporting and Corrective Action Section** | Defines procedures for reporting, tracking, and resolving errors or defects; identifies organizational responsibilities |
| **Test Section** | References the test plan and procedure document; defines test record keeping requirements |
| **Other** | Tools, SQA methods, change control, record keeping, training, and risk management |

---

## 12. Mission of SEI

| Area | Description |
|------|-------------|
| **Research** | Advancing the science and practice of software engineering |
| **Collaboration** | Bringing together and building on work found in industry, academia, and government |
| **Development and Demonstration** | Maturing promising technologies and practices and demonstrating their utility through trial application and prototypes |
| **Transition** | Propagating proven technologies and practices through publication, standards, and other venues |

---

## Quick Revision Summary

### Definitions at a Glance

| Term | Definition |
|------|-----------|
| **Testing** | Execution of a program to find faults |
| **Verification** | Proving the program's correctness (*are we building the product right?*) |
| **Validation** | Finding errors by executing in a real environment (*are we building the right product?*) |
| **Debugging** | Diagnosing the error and correcting it |
| **Software Quality** | Degree to which software meets specified requirements and user expectations |
| **SQA** | Monitoring software engineering processes to ensure quality |
| **CMM** | Capability Maturity Model — 5-level model for process improvement |

### Four Levels of Testing

1. **Unit Testing** — Single component, by developer
2. **Integration Testing** — Combined modules, by testers
3. **System Testing** — Whole system, includes load/reliability/performance/security
4. **Acceptance Testing** — End-user requirements, readiness for deployment

### Three Test Strategies

- **Static** — Without running the system
- **Structural** — Run on real devices
- **Behavioral** — Focus on system behavior and user journey

### SEI-CMM — 5 Levels (Quick Mnemonic: **I** **R**eally **D**o **M**ake **O**ptimizations)

| # | Level | Key Focus |
|---|-------|-----------|
| 1 | **I**nitial | Ad-hoc, individual effort |
| 2 | **R**epeatable | Basic project management, repeatable |
| 3 | **D**efined | Standardized processes organization-wide |
| 4 | **M**anaged | Quantitative metrics, predictable quality |
| 5 | **O**ptimizing | Continuous process improvement |

### SQA Plan Key Sections

- Management, Documentation, Standards, Reviews & Audits, Problem Reporting & Corrective Action, Testing, Other (Tools, methods, change control, training, risk)

### Mission of SEI

Research → Collaboration → Development & Demonstration → Transition

## Glossary

| Term | Definition |
|------|-----------|
| **Testing** | Execution of a program to find its faults |
| **Verification** | "Are we building the product right?" — checking against specifications |
| **Validation** | "Are we building the right product?" — checking against user needs |
| **Debugging** | Process of diagnosing an error and correcting it |
| **Software Quality** | Degree to which a software product meets specified requirements and user expectations |
| **SQA** | Software Quality Assurance — monitoring software engineering processes to ensure quality |
| **CMM** | Capability Maturity Model — 5-level model for process improvement |
| **SEI** | Software Engineering Institute — Carnegie Mellon research center |
| **Unit Testing** | Testing individual components; performed by developers |
| **Integration Testing** | Testing combined modules as a group; performed by testers |
| **System Testing** | Testing the complete system including load, reliability, performance, security |
| **Acceptance Testing** | Testing by users to determine if the system is ready for deployment |
| **Test Plan** | Document detailing the systematic approach to testing a system |
| **Test Case** | Set of conditions under which a tester determines if software works correctly |
| **V-Model** | SDLC model mapping verification (left side) to validation (right side) activities |
