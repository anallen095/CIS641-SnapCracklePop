# Overview

This document serves to outline the specific criteria, features, functionality, and constraints of the system. It is meant to provide a clear and unambiguous reference for stakeholders to understand and agree upon what needs to be designed, developed, and delivered. It acts as a foundational blueprint to guide the entire development process, ensuring that the final outcome aligns with the intended goals and meets the expectations of all parties involved.

# Functional Requirements

A functional requirement defines a specific behavior or action that a system, software, or product must perform to fulfill its intended purpose, often specifying inputs, processing, and outputs.

1. **User Registration**
   - The system shall have a user-friendly form to enter necessary information during the registration process.
   - The required pieces of information to register a new user shall be username, email address, TSA ID, password, reporting manager, and user role.
   - The system shall enforce password complexity rules, including minimum length, use of uppercase, lowercase, numbers, and special characters to maintain system security.
   - Users shall be required to confirm their password.
   - The system shall display a message to let the user know when they have successfully registered.
   - The system shall display all new users in the Users table.
   - The system shall enforce unique account constraints on all accounts created.

2. **Customer Profile and Dashboard**
   - The system shall display key metrics for customers, including open deduction balance and the number of open deductions.
   - The system shall have the ability to update all customer information except the customer number.
   - Only admin users shall have the ability to update customer information.
   - All users shall have the ability to create an outgoing email to the customer support team from the customer’s profile.
   - All customer profiles shall have the option to include a profile picture for the customer.

3. **User Profile Manager**
   - Users shall have the ability to make changes to their public profile.
   - All users shall have the option to upload a picture to their profile.
   - User information shall be available to all users.
   - Admin users shall have the ability to deactivate former employees.
   - Admin users shall have the ability to edit user data.

4. **Data Entry Operations**
   - The system shall enforce all data constraints for user-entered data.
   - The system shall generate error messages for any violations or data constraints.
   - Users shall be able to export data to CSV.
   - The system shall record any changes made to the data by recording the time at which the change was made.
   - The system shall record any changes made to the data by recording the user who made the change.

5. **User Authentication**
   - Login/Welcome splash screen show be user-friendly with fields to enter a password/username.
   - When users are logged in, the login and registration buttons shall not be visible.
   - When no user is logged in, the login and registration buttons shall be visible.
   - Users shall have the option to reset their password.
   - The system shall tie out after 30 active minutes and require users to re-enter their password to continue working.
   - The system shall lock out any users who have failed to enter their password correctly three times.
   - Admin users shall have the ability to unlock accounts.
   - The system shall store all passwords in hash form to protect security.

# Non-Functional Requirements

A non-functional requirement outlines the quality attributes, performance characteristics, and constraints that a system, software, or product must adhere to, such as reliability, scalability, or security, without specifying specific functionalities.

1. **Based Platform**
   - The system shall be accessible across multiple web browsers (e.g., Chrome, Firefox, Edge) to accommodate user preference.
   - The system shall have a responsive design and adjust to different screen sizes.
   - The system shall accommodate multiple devices, including tablet, mobile phones, and desktop computers.
   - The system shall maintain a consistent UI design across all pages and components.
   - The system shall present user-friendly error messages with clear instructions for resolving issues.

2. **Security**
   - The system shall only display data associated with W.K. Kellogg Co.
   - Any users with backend access to data shall be required to sign an NDA.
   - All sensitive data, such as passwords, shall be securely encrypted in the database.
   - User accounts shall be automatically locked after a defined number of consecutive unsuccessful login attempts, with an option for users to unlock their accounts or contact administrators for assistance.
   - The system shall enforce role-based access control (RBAC), ensuring that users have access only to the functionalities and data necessary for their roles.
     
3. **Data Integrity**
   - The system shall be connected to an SQL Server managed via SSMS.
   - Data in the system shall be accurate and tie out with the master data source (SAP).
   - Record counts shall tie out with the master data source (SAP).
   - There shall be no duplicates in the data source.
   - The system shall check to ensure the data is available and validated at least once per day.

4. **Performance, Usability & Maintainability**
   - System UI shall respond to user inputs quickly and appropriately.
   - The system shall load the main dashboard within 3 seconds of a user's request.
   - All database queries shall return results within a maximum of 2 seconds.
   - Users shall be able to easily navigate the site and use features.
   - Code shall be fully documented so developers and sustainment teams can easily understand and work with existing code.
   - The system shall be optimized to handle a concurrent user load of 100 users without a degradation in performance.
   - User interface elements, such as buttons and links, shall have a consistent design and placement across all pages for improved usability.
   - The system shall provide clear and concise error messages to users, guiding them on how to resolve issues.
   - Regular system backups shall be automated and performed during non-peak hours to minimize disruption to users.
   - The application shall include version control to track changes in the codebase and allow for easy rollback in case of issues.




6. **Technical Documentation**
   - The documentation shall clearly define the target audience, specifying whether it is intended for developers, administrators, or other stakeholders.
   - Each section shall have clear headings and subheadings to facilitate quick reference.
   - The documentation shall maintain a revision history, tracking changes, updates, and contributors over time.
   - The documentation shall include a mechanism for users to provide feedback, report errors, or suggest improvements.
   - The documentation shall be hosted on W.K. Kellogg Enterprise GitHub in the ITC Reporting & Analytics repository.

