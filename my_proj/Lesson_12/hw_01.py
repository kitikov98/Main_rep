# Создать таблицу со студентами в БД



create_students_table = """
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    surname TEXT NOT NULL,
    subject TEXT NOT NULL);
"""

create_students = """
INSERT INTO students(surname, subject)
VALUES ('John','Math'),
       ('Ivan','English'),
       ('Nick','Math'),
       ('Julia','Math'),
       ('OLga','English'),
       ('Oleg','Physics'),
       ('Kate','Physics'),
       ('Dmitri','Physics'),
       ('Sveta','Chemistry'),
       ('Yuri','Chemistry'),
       ('Kostya','Biology'),
       ('Boris_the_Blade','Biology'),
       ('Tanya','Literature'), 
       ('Alexander','Literature');       
"""

select_students = """
SELECT * from students
"""
