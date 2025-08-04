# Software Test Plan (STP)

**Project:** Pango Pay & Go - Parking Lot Manager  
**Prepared by:** Lior Alalouf  
**Date:** August 3, 2025  

---

## 1. Introduction

This document describes the test plan for the **Pango Pay & Go - Parking Lot Manager** application.  
The purpose is to outline the testing strategy, scope, approach, and deliverables to ensure the quality of the system.

---

## 2. Objectives

- Verify core parking functionalities including vehicle entry and exit.  
- Validate that a vehicle cannot be parked by more than one driver simultaneously.  
- Ensure appropriate error messages are displayed.  
- Test user authentication and session management.  
- Automate key test cases for regression purposes.

---

## 3. Scope

**In Scope:**

- Functional testing of the web application UI  
- Covering main user flows  

**Out of Scope:**

- Direct API testing (no documented JSON API endpoints)  
- Performance and load testing  
- Verification of HTTP status codes and page content for key endpoints  

---

## 4. Test Approach

- Black-box testing without access to internal source code or API documentation  
- Automated UI tests using **Pytest** / **Selenium**  
- Manual exploratory testing for complex scenarios  

---

## 5. Test Environment

- Application runs locally via Docker on `localhost:5000`  
- Testing on Windows 10/11 with **Chrome** browser  
- **Docker Desktop** installed and configured  

---

## 6. Test Deliverables

- This Test Plan document (STP)  
- Software Test Design (STD) with detailed test cases  
- Automated test scripts and execution reports  
- Bug reports (if applicable)  
- Suggestions for system improvements  

---

## 7. Risks and Mitigation

| **Risk**                           | **Mitigation**                                                  |
|------------------------------------|------------------------------------------------------------------|
| Lack of API documentation          | Perform black-box testing based on UI and network analysis       |
| Environment inconsistencies        | Use Docker container for uniform environment                     |
| Authentication issues during automation | Implement session management in test scripts               |

---

## 8. Schedule

| **Task**                     | **Estimated Duration** |
|-----------------------------|-------------------------|
| STP & STD preparation       | 3 Hours                |
| Automation development      | 4 Hours                |
| Test execution & bug reporting | 1–2 Hours             |
| Documentation & submission  | 1 Hour                 |

