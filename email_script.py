from email.message import EmailMessage
import smtplib
import psycopg2
import configparser

# Read the configuration file
config_file = "C:\\Users\\zerub\\OneDrive\\Desktop\\MINI project\\file processing\\data.config"
config = configparser.ConfigParser()
config.read(config_file)

config_db = config["DEFAULT"]
db_user_name = config_db.get("db_user_name")
db_user_pswd = config_db.get("db_user_pswd")
db_name = config_db.get("db_name")
db_host = config_db.get("db_host")
db_port = config_db.get("db_port")

config_email = config["EMAIL"]
sender_email = config_email.get("sender")
email_password = config_email.get("password")

conn_string = f"dbname={db_name} user={db_user_name} password={db_user_pswd} host={db_host} port={db_port}"

def connect_db():
    return psycopg2.connect(conn_string)

def send_email(sender, recipient, password, subject, message):
    email = EmailMessage()
    email["From"] = sender
    email["To"] = recipient
    email["Subject"] = subject
    email.set_content(message)

    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
    smtp.starttls()
    smtp.login(sender, password)
    smtp.sendmail(sender, recipient, email.as_string())
    smtp.quit()

def fetch_and_send_emails(conn, processing_type):
    cursor = conn.cursor()

    try:
        if processing_type == 'attendance':
            cursor.execute("""
                SELECT Email, RollNo, StudentName
                FROM attendance_history
                WHERE Status = 'Absent';
            """)
            rows = cursor.fetchall()
            for row in rows:
                recipient_email = row[0]
                roll_no = row[1]
                student_name = row[2]
                message_body = (f"Dear {student_name},\n\n"
                                f"The attendance status for roll number {roll_no} is marked as Absent. Kindly mention the reason below. Please attend the classes regularly.\n\n"
                                "Regards,\nManagement")
                send_email(sender_email, recipient_email, email_password, "Attendance Status", message_body)

        elif processing_type == 'marks':
            cursor.execute("""
                SELECT Email, StudentName, Math, Science, English, History, Art, Total
                FROM marks_history;
            """)
            rows = cursor.fetchall()
            for row in rows:
                recipient_email = row[0]
                student_name = row[1]
                math = row[2]
                science = row[3]
                english = row[4]
                history = row[5]
                art = row[6]
                total = row[7]
                message_body = (f"Dear {student_name},\n\n"
                                "Your marks have been updated:\n"
                                f"Math: {math}\n"
                                f"Science: {science}\n"
                                f"English: {english}\n"
                                f"History: {history}\n"
                                f"Art: {art}\n"
                                f"Total: {total}\n\n"
                                "Regards,\nSchool Administration")
                send_email(sender_email, recipient_email, email_password, "Marks Status", message_body)

    finally:
        cursor.close()


