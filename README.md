
# ClassPulse: Automated Student Attendance and Grade Notification System

Developed a comprehensive system that automates the process of student attendance and grade management using Python, PostgreSQL, and CSV file processing. The system reads attendance and grade data from CSV files, processes the information, and stores it in a PostgreSQL database. It also automates email notifications to students, informing them of their attendance status or grade updates. The project included the use of temporary tables, stored procedures, and dynamic configuration management to ensure efficient data handling and secure communication.


## Features

- Read and process CSV files for student attendance and marks
- Store and manage data in PostgreSQL using temporary and staging tables
- Execute stored procedures for efficient data handling
- Send automated email notifications to students
- Modular script structure (attendance, marks, email)


## Key Technologies

Python, PostgreSQL, smtplib, CSV, SQL, Email Automation
## How to run: 

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/student-attendance-grade-system.git
   cd student-attendance-grade-system

   Set up PostgreSQL
2. **Create your database**

Run provided table creation and stored procedure scripts.


3. **Configure config.ini**
```bash
[postgresql]
host = localhost
database = your_db
user = your_user
password = your_password

[email]
sender = your_email@example.com
password = your_app_password

[processing]
type = attendance
```

4. **Run scripts**
```bash
python main.py attendance
python main.py marks
```


## Screenshots

![Screenshot 2025-05-08 114401](https://github.com/user-attachments/assets/5d13cfed-a509-4ad4-a488-6e65bd54710a)

![Screenshot 2025-05-08 114411](https://github.com/user-attachments/assets/b4a555ab-7684-4199-9ad3-3526195cb7ab)

![Screenshot 2025-05-08 114442](https://github.com/user-attachments/assets/10aa6adb-1676-44c7-b543-b0ffc90aa9fc)


