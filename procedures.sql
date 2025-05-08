/*join procedure(attendance)*/
CREATE PROCEDURE attn_join_proc()
LANGUAGE 'plpgsql'
AS $BODY$
DECLARE
BEGIN

INSERT INTO attendance_staging (RollNo,StudentName,Class,PhoneNumber,Email,Status) 
SELECT a.RollNo,a.StudentName,a.Class,a.PhoneNumber,a.Email,b.Status
FROM temp_students a
JOIN temp_attendance b ON a.RollNo = b.RollNo;

END;
$BODY$;

/*attendance procedure*/
CREATE PROCEDURE attn_proc()
LANGUAGE plpgsql
AS $Body$
BEGIN
insert into attendance_history(RollNo,StudentName,Class,PhoneNumber,Email,Status)
select RollNo::integer,StudentName,Class::integer,PhoneNumber::bigint,Email,Status from attendance_staging;
END;
$Body$;

/*join procedure(marks)*/
CREATE PROCEDURE marks_join_proc()
LANGUAGE 'plpgsql'
AS $BODY$
DECLARE
BEGIN

INSERT INTO marks_staging (RollNo,StudentName,Class,PhoneNumber,Email,Math,Science,English,History,Art,Total) 
SELECT a.RollNo,a.StudentName,a.Class,a.PhoneNumber,a.Email,c.Math,c.Science,c.English,c.History,c.Art,c.Total
FROM temp_students a
JOIN temp_marks c ON a.RollNo = c.RollNo;

END;
$BODY$;

/*marks procedure*/
CREATE PROCEDURE marks_proc()
LANGUAGE plpgsql
AS $Body$
BEGIN
insert into marks_history(RollNo,StudentName,Class,PhoneNumber,Email,Math,Science,English,History,Art,Total)
select RollNo::integer,StudentName,Class::integer,PhoneNumber::bigint,Email,Math::integer,
	Science::integer,English::integer,History::integer,Art::integer,Total::integer from marks_staging;
END;
$Body$;