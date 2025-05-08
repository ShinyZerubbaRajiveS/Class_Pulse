import configparser
import psycopg2

def process_attendance():
    config_file = "C:\\Users\\zerub\\OneDrive\\Desktop\\MINI project\\file processing\\data.config"
    config = configparser.ConfigParser()
    config.read(config_file)
  
    config_db = config["DEFAULT"]
    db_user_name = config_db.get("db_user_name")
    db_user_pswd = config_db.get("db_user_pswd")
    db_name = config_db.get("db_name")
    db_host = config_db.get("db_host")
    db_port = config_db.get("db_port")
    conn_string = f"dbname={db_name} user={db_user_name} password={db_user_pswd} host={db_host} port={db_port}"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()


    # Load CSV data into temp tables
    file1 = "C:\\Users\\zerub\\OneDrive\\Desktop\\MINI project\\file processing\\students_data.csv"
    file2 = "C:\\Users\\zerub\\OneDrive\\Desktop\\MINI project\\file processing\\attendance_data.csv"
    attendance_staging = "attendance_staging"
    temp_students = "temp_students"
    temp_attendance = "temp_attendance"

    cursor.execute("""CREATE TEMP TABLE temp_students (
    RollNo TEXT,
    StudentName TEXT,
    Class TEXT,
    PhoneNumber TEXT,
	Email TEXT);""")

    cursor.execute("""CREATE TEMP TABLE temp_attendance (
    RollNo TEXT,
    StudentName TEXT,
    Status TEXT);""")

    cursor.execute("TRUNCATE TABLE " + temp_students + ";")
    cursor.execute("TRUNCATE TABLE " + temp_attendance + ";")
    conn.commit()

    # Load data into temp tables
    sql1 = "COPY temp_students FROM STDIN WITH (FORMAT csv, HEADER);"
    with open(file1, "r") as file:
        cursor.copy_expert(sql1, file)
    conn.commit()

    sql2 = "COPY temp_attendance FROM STDIN WITH (FORMAT csv, HEADER);"
    with open(file2, "r") as file:
        cursor.copy_expert(sql2, file)
    conn.commit()
   
    cursor.execute("TRUNCATE TABLE "+ attendance_staging + ";")

    # Process and join the data
    cursor.execute("CALL attn_join_proc();") 
    conn.commit()

    cursor.execute("CALL attn_proc();") 
    conn.commit()

    cursor.close()
    conn.close()

if __name__ == "__main__":
    process_attendance()
