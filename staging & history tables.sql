CREATE TABLE attendance_staging(RollNo TEXT,StudentName TEXT,Class TEXT,
	PhoneNumber TEXT,Email TEXT,Status TEXT);

CREATE TABLE marks_staging(RollNo TEXT,StudentName TEXT,Class TEXT,
	PhoneNumber TEXT,Email TEXT,Math TEXT,Science TEXT,English TEXT,History TEXT,Art TEXT,Total TEXT);

CREATE TABLE attendance_history(RollNo integer,StudentName varchar(50),Class integer,
	PhoneNumber bigint,Email varchar(50),Status varchar(15));
insert into attendance_history(RollNo,StudentName,Class,PhoneNumber,Email,Status)
select RollNo::integer,StudentName,Class::integer,PhoneNumber::bigint,Email,Status from attendance_staging;

CREATE TABLE marks_history(RollNo integer,StudentName varchar(50),Class integer,PhoneNumber bigint,Email varchar(50),
	Math integer,Science integer,English integer,History integer,Art integer,Total integer);
insert into marks_history(RollNo,StudentName,Class,PhoneNumber,Email,Math,Science,English,History,Art,Total)
select RollNo::integer,StudentName,Class::integer,PhoneNumber::bigint,Email,Math::integer,
	Science::integer,English::integer,History::integer,Art::integer,Total::integer from marks_staging;