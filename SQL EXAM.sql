USE foundation_assessment_i;
drop table if exists results;
drop table if exists students;
drop table if exists exams;

create table students (
	student_id int not null,
    forename char(100),
    surname char(100),
    primary key(student_id)
);

create table exams (
	exam_id int not null,
    exam_name char(100),
    max_mark char(100),
    primary key(exam_id)
);

create table results (
	result_id int not null,
    student_id int not null,
    exam_id int not null,
    mark int,
    primary key(result_id)
    # foreign key(student_id) references students(student_id),
    # foreign key(exam_id) references exams(exam_id)
);

INSERT INTO students(Student_ID, FORENAME, SURNAME)
VALUES
   (1, "Alice", "Adams"),
   (2, "Belen", "Badillo"),
   (3, "Ciara", "Connelly"),
   (4, "Delia", "Dodds"),
   (5, "Everly", "Evans"),
   (6, "Fabia", "Fahim"),
   (7, "Grace", "Gonzalez")
;

insert into results(result_id, student_id, exam_id, mark)
VALUES
   # the results for the first exam
   (1, 1, 1, 0),
   (2, 2, 1, 62),
   (3, 3, 1, 62),
   (4, 4, 1, 39),
   (5, 5, 1, 98),
   (6, 6, 1, 48),
   (7, 7, 1, 23),
   # the results for the second exam
   (8, 1, 2, 43),
   (9, 2, 2, 68),
   (10, 3, 2, 54),
   (11, 4, 2, 21),
   (12, 5, 2, 68),
   (13, 6, 2, 74),
   (14, 7, 2, 14);


insert into exams(exam_id, exam_name, max_mark)
VALUES
   (1, "Algorithms", 100),
   (2, "Cyber Security", 80);
   
select * from students;
select * from exams;
select * from results;

select s.forename, s.surname, m.mark
from students s
inner join results m
on 
s.student_id=m.student_id
where 
m.mark > 60;




