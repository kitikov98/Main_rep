# Создать таблицу аудиторий в БД

creat_audit_table = """
CREATE TABLE IF NOT EXISTS audit (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number INTEGER NOT NULL,
    subject TEXT NOT NULL,
    FOREIGN KEY (subject) REFERENCES students(subject));
"""

creat_audit = """
INSERT INTO 
audit (number, subject)
VALUES (308,'Math'),
       (104,'English'),
       (404,'Physics'),
       (113,'Chemistry'),
       (102,'Biology'),
       (503,'Literature');
"""

select_audit = """
SELECT * from audit
"""