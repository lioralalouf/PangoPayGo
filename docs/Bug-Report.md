# 🐞 Bug Report

## BUG1
## Title:
No error message login with valid credentials

## Steps to Reproduce:
1. Go to the Login page.
2. Enter valid credentials:  
   - Username: `validuser`  
   - Password: `correctpass`
3. Click on the "Login" button.

## ✅ Expected Result:
User should be redirected to the dashboard.

## ❌ Actual Result:
Error message appears: "Invalid credentials".

## Severity: High  
## ⚠Priority: Medium

## 📸 Screenshot:
![Login Error](./screenshots/login_no_error.PNG)

_______________________________________
## BUG2
## Title:
Start time and End time for parking is 3 hours earlier

## Test Steps
1. Navigate to the login page:  
   `http://localhost:5000/login`

2. Enter valid credentials:  
   - Username: `<valid username>`  
   - Password: `<valid password>`

3. Click on the **Login** button.  
   Ensure that you're redirected to the **Dashboard** page.

4. In the **Car Plate** field, enter: `01234561`

5. In the **Vehicle Type** dropdown, select: `Standard`

6. In the **Slot** field, enter: `22`

7. Click on the **Start Parking** button.

---

## ✅ Expected Result
A new parking session should appear on the screen with the following:

- Car Plate: `01234561`
- Slot: `22`
- Start Time: **Current system time**

## ❌ Actual Result
- Car Plate and Slot appear correctly.
- However, the **Start Time** is shown **3 hours earlier** than the current system time.
---
## Severity: Medium  
## ⚠Priority: Medium

## 🧠 Analysis
- The issue is likely related to a **timezone (TZ) misconfiguration** on the server or client.

![TZ Error](./screenshots/tz_error.PNG)
_______________________________________________


## BUG3
## Title:
Incorrect billing popup on parking end

## Steps to Reproduce:
1. Navigate to the login page:  
   `http://localhost:5000/login`

2. Enter valid credentials:  
   - Username: `<valid username>`  
   - Password: `<valid password>`

3. Click on the **Login** button.  
   Ensure that you're redirected to the **Dashboard**.

4. In the **Car Plate** field, enter: `01234561`

5. In the **Vehicle Type** dropdown, select: `Standard`

6. In the **Slot** field, enter: `22`

7. Click on the **Start Parking** button.

8. After a few seconds, click on **End Parking**.

---

## ✅ Expected Result:
A confirmation popup is displayed with a message:  
`Parking ended for 01234561. Fee: {fee} (Charge: success)`

## ❌ Actual Result:
A popup is displayed with an **error message**:  
`Parking ended for 01234561. Fee: {fee} (Charge: Error)`

---

## 🧠 Analysis:
- There may be a **problem in the billing integration** or **mocked payment logic** in the backend.
- Could also be related to how the parking fee is calculated or triggered too soon after starting.

## Severity: High  
## ⚠ Priority: High

## 📸 Screenshot:
![Fee Error](./screenshots/fee_parking_end_error.PNG)