import sys
import email_script
import attendance
import marks

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py [attendance|marks]")
        return
    
    processing_type = sys.argv[1].lower()

    conn = email_script.connect_db()
    try:
        if processing_type == 'attendance':
            attendance.process_attendance()
            email_script.fetch_and_send_emails(conn, 'attendance')

        elif processing_type == 'marks':
            marks.process_marks()
            email_script.fetch_and_send_emails(conn, 'marks')

        else:
            print("Unknown processing type. Use 'attendance' or 'marks'.")

    finally:
        conn.close()

if __name__ == "__main__":
    main()
