# Overview

This document serves to outline the specific criteria,  features, functionality, and constraints of the system. It is meant to provide a clear and unambiguous refrence for stakeholders to understand and agree upon what needs to be designed, developed, and delivered. It acts as a foundational blueprint to guide the entire development process, ensuring that the final outcome aligns with the intended goals and meets the expectations of all parties involved.

# Functional Requirements

A functional requirement defines a specific behavior or action that a system, software, or product must perform to fulfill its intended purpose, often specifying inputs, processing, and outputs.

1.	User Registration
-	The system shall have a user-friendly form to enter necessary information during the registration process. 
-	The required pieces of information to register a new user shall be username, email address, TSA ID, password, reporting manager, and user role. 
-	System shall enforce password complexity rules including minimum length, use of uppercase, lowercase, numbers, and special characters to maintain system security. 
-   Users shall be required to confirm their password
-	System shall display a message to let the user know when they have sucessfully registered
-   System shall display all new users in the Users table
-	The system shall enforce unique account constraints on all accounts created.

2.	Customer Profile and Dashboard
-	System shall display key metrics for customers including open deduction balance and number of open deductions
-	System shall have the ability to update all customer information except the customer number
-	Only admin users shall have the ability to update customer information. 
-	All users shall have the ability to create an out-going email to the customer support team from the customer’s profile. 
-	All customer profiles shall have the option to include a profile picture for the customer. 


3.	User Profile Manager 
-	Users shall have the ability to make changes to their public profile. 
-	All users shall have the option to upload a picture to their profile. 
-	User information shall be available to all users. 
-	Admin users shall have the ability to deactivate former employees. 
-	Admin users shall have the ability to edit user data. 

4.	Data Entry Operations
-	System shall enforce all data constraints for user entered data. 
-	System shall generate error messages for any violations or data constraints. 
-	Users shall be able to export data to CSV. 
-	The system shall record any changes made to the data by recording the time at which the change was made.
-	The system shall record any changes made to the data by recording the user who made the change. 

5.	User Authentication 
-	Login/Welcome splash screen show be user-friendly with fields to enter a password/username. 
- When users are logged in the login and registration buttons shall not be visable
- When no user is logged in the login and registration buttons shall be visable
-	Users shall have the option to reset their password. 
-	System shall tie out after 30 active minutes and require users to re-enter their password to continue working. 
-	System shall lock out any users who have failed to enter their password correctly three times. 
-	Admin users shall have the ability to unlock accounts. 


# Non-Functional Requirements

A non-functional requirement outlines the quality attributes, performance characteristics, and constraints that a system, software, or product must adhere to, such as reliability, scalability, or security, without specifying specific functionalities.

Based Platform 
-	System shall be accessible across multiple web browsers (e.g., Chrome, Firefox, Edge) to accommodate user preference. 
-	System shall have a responsive design and adjust to different screen sizes.
-	System shall accommodate multiple devices including tablet, mobile phone, and desktop computer. 
-	System shall maintain a consistent UI design across all pages and components. 
-	System shall present user-friendly error messages with clear instructions for resolving issues. 

2.	Security 
-	The system shall only display data associated with W.K. Kellogg Co. 
-	Any users with backend access to data shall be required to sign NDA. 
-   The system shall store all passwords in hash form to protect security
-	Access to set strategy of the program shall be limited to director users only. 
-   Only users or users with role of admin can update a user profile

3.	Data Integrity
-	System shall be connected to an SQL Server managed via SSMS. 
-	Data in the system shall be accurate and tie out with the master data source (SAP)
-	Record counts shall tie out with master data source (SAP)
-	There shall be no duplicates in the data source. 
-	The system shall check to ensure the data is available and validated at least once per day.
4.	User Documentation 
-	User documentation shall be written in clear and easily understandable language.
-	Technical terms and jargon shall be explained or defined in the documentation. 
-	The documentation shall maintain consistency in terms of formatting, terminology, and style.
-	The documentation shall be easily accessible to all users. 
-	The documentation shall be hosted on W.K. Kellogg Co. SharePoint  
5.	Technical Documentation
-	Technical documentation shall be written in clear and easily understandable language. 
-	Business specific terms shall be clearly defined in the documentation. 
-	The documentation shall be hosted on W.K. Kellogg Enterprise GitHub in the ITC Reporting & Analytics repository. 
-	The documentation shall be accessible to only technical and admin users with access to the enterprise GitHub repo. 
-	Documentation shall be written in markdown formatting and shall maintain consistency in terms of formatting, terminology, and style.

