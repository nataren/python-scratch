CREATE TABLE Courses(
       CourseID INTEGER,
       CourseName VARCHAR(255),
       TeacherID INTEGER
);

CREATE TABLE Teachers(
       TeacherID INTEGER,
       TeacherName VARCHAR(255)
);

CREATE TABLE Students(
       StudentID INTEGER,
       StudentName VARCHAR(255)
);

CREATE TABLE StudentCourses(
       CourseID INTEGER,
       StudentID INTEGER
);
