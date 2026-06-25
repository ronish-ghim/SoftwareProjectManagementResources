# Unit 09: Software Configuration Management

> **Hours:** 3 Hrs. | **Source:** `Chapter_9_Software Configuration Management.pdf`

---

## Introduction to SCM

The First Law of System Engineering "* No matter where you are in the system life cycle, the system will change, and the desire to change it will persist throughout the life cycle.*" The four aspects of software evolution are:
***Corrective changes***
***Adaptive changes***
***Perfective changes***
***Preventive changes***
***Corrective changes***
Required to maintain control over the system's day-to-day functions.
These changes are made as faults (or) bugs are found during the development time.
Some changes may be long-term and fundamental, some may be patches to keep the system in operation (emergency fixes)
***Adaptive changes*** Essentially maintaining control over system modifications.
As one part of the system changes, other impacted areas will need to be updated Examples
*Database upgrades.* *Use of a new compiler or development tool*
***Perfective changes*** The domain of Refactoring designs falls into this category.
Perfective changes are done to increase the long-term maintainability or elegance of the solution
*Involves changes to design or data structures for better efficiency*
*Updates to documentation to improve their quality* *Enhancing the code to make it more readable*
***Preventive changes*** Preventing the system performance from degrading unacceptable levels Involves alterations made to ensure that the system has a defense against potential failures
If changes are not controlled in a project - things can and will get out of hand The issue of change management is even more important when multiple people work on a project as well as on the same deliverable.
Without proper strategies and mechanisms to control
changes - one can never revert back to an older more stable copy of the software.
Important as every change introduces risk into the project
**The facts** *Change is unavoidable in software*
*Changes needs to be controlled*
*Changes need to be managed* **The solution**
*Software Configuration Management (SCM)*

Management Software Configuration Management (SCM) is the practice of identifying, organizing, and controlling changes the software and related objects throughout the software development life cycle.
SCM is a critical process for ensuring that software products. are developed, tested, and released in a controlled and predictable manner, and that changes to the software are tracked and managed efficiently.
SCM includes activities such as: Version control, Build management, Release management, Change management and Configuration management.

## Need for SCM

As software evolves - many resources make changes to the system
*CM prevents avoidable errors that arise from conflicting*
*changes.* Often many versions of the software are released and require support *CM allows a team to support many versions.*
*CM*
*allows*
*changes*
*in*
*sequential*
*versions*
*to*
*be*
*propagated.* CM allows developers to track changes and reverse any fatal changes to take a software system back to its last known safe state
Good SCM increases confidence that we are:
*Building the right system.* *Testing the system enough.*
*Changing it correctly and carefully.* It also:
*Restrains non-essential changes.* *Ensures that decisions and changes are traceable.*
*Increases accountability.*
*Improves overall software quality.* *Provides a fall back position when things do not work.*

## Basic Configuration Management

The basic configuration of SCM Involves following steps:
***Identify Configuration Items:*** Identify configuration items such as source code, documentation, requirements; design etc.
***Define the Repository Structure:*** This may include creating folder structure that reflects the organization of a software artifacts.
***Choose a Version Control System:*** Choose any version control system from popular ones
like*** Git.***
***Establish a Baseline:*** Establish a baseline or a starting point of the software development process.
***Create a Change Management Process:*** It outlines the procedures for making changes to the configuration items.
***Set up build and release management:*** It involve building the software and releasing it to users.
***Define Access Control and Security:*** This may involve defining user roles and permissions, establishing password policies, procedures for granting access etc.

## SCM Roles and Responsibilities

Following are some of the*** roles*** of SCM:
***Configuration Manager:*** Configuration Manager is the head who is responsible for identifying configuration items.
Configuration Manager ensures team follows SCM process.
***Developer:*** The developer needs to change the code as per standard development activities or change requests.
Developer is responsible for maintaining configuration of code.
The developer should check the changes and resolve conflicts.
***Auditor:*** The auditor is responsible for SCM audits and reviews.
Auditor need ensure the consistency and completeness of release.
***User:*** The end user should understand the key SCM terms to ensure he has the latest version of the software,
Following are some of the responsibilities of SCM:
***Version Control:*** Implementing and maintaining the version control system, and ensuring that developers are using it correctly.
***Baseline Management:*** Creating and maintaining baselines of the software configuration items, and ensuring that they are properly labeled and stored in the repository.
***Change Management:*** Establishing and maintaining the change management process, including defining the procedures for making changes to the software.
***Build and Release Management:*** Managing the build and release, process, including defining the build and release procedures.
***Branching and Merging:*** Managing the branching and merging of code and ensuring that developers are following the best practices for branching and merging.
***Access Control and Security:*** Managing access control and security for the SCM repository and ensuring that the appropriate security measures are in place to protect the software project.

## Management Responsibilities

Function of management help us to stay informed about we need to do and how can staffs be guided accordingly.
The functions of management are:
*Planning*
*Organizing*
*Staffing*
*Directing*
*Controlling*
***Planning*** It sets the road map for the development of project along with assumed risks and solution.
***Organizing*** Here we put plan into action by establishing a system of hierarchy to carry out developmental tasks.
***Staffing*** Here we assign tasks based on each team members knowledge, skills, and abilities.
Also, hire new staffs, if needed.
***Directing*** It is concerned with supervising teams progress.
Here have keep open channel Communication and get regular updates to stay on top of things.
***Controlling*** It is concerned with measuring the process of each step established the planning stage against our organizational goals.
It helps to coordinate with employees to ensure that they're moving in right direction in right manner.

## Baseline

A specification or product that has been formally reviewed and agreed upon, that thereafter serves as the basis for further development, and that can be changed only through formal change control procedures!!
Before a software configuration item becomes a baseline, change may be made quick and informal.
However, once a baseline is established, we figuratively pass through a swinging one way door.
Changes can be made, but a specific, formal procedure must be applied to evaluate and verify each change.
A baseline is typically established at a significant point in the development process such as after completing a major milestone or before making significant changes to the software.
Once a baseline is established, it is stored in the SCM repository and can be used as a future reference for further development work.
