Illinois EPA Test Tracking System
Description
This project is an individual effort aimed at developing a comprehensive test tracking and source management system for the Illinois Environmental Protection Agency (EPA). The system manages various environmental test requests, protocols, and inquiries to ensure efficient regulatory oversight.

Technologies Used
Backend: Python, Flask, SQLAlchemy
Database: MySQL
Containerization: Docker
Features
Management of test requests, protocols, and inquiries.
Integration with a MySQL database to store and manage data efficiently.
Secure user authentication and role-based access control.
Getting Started
Prerequisites:

Docker should be installed on your local machine.
Setup:

Clone the repository:
bash
Copy
Edit
git clone <repository_url>  
Navigate to the project directory:
bash
Copy
Edit
cd smu_testing  
Running the Application:

Build and run the containers using Docker Compose:
bash
Copy
Edit
docker-compose up -d  
Accessing the Database:

MySQL Database can be accessed at localhost:3306.
Use the credentials:
Username: user
Password: password
Database Schema
The database schema includes:

Sources: Information on various sources.
TestRequests: Test requests linked to sources.
SourceEquipment: Equipment associated with sources.
TestProtocol: Protocols related to tests.
TestInquiries: Inquiries submitted for test evaluations.
TestArchive: Archived test results and related information.

