INSERT INTO patient (firstname, lastname, date_of_birth, sex)
VALUES ("Bob", "Steve", '1990-09-01', "Male");

INSERT INTO patient (firstname, lastname, date_of_birth, sex)
VALUES ("Joe", "Steve", '1991-09-01', "Male");

INSERT INTO patient (firstname, lastname, date_of_birth, sex)
VALUES ("Sally", "Steve", '1995-09-01', "Female");

INSERT INTO patient (firstname, lastname, date_of_birth, sex)
VALUES ("Bob", "Joe", '1998-09-01', "Male");

INSERT INTO patient (firstname, lastname, date_of_birth, sex)
VALUES ("Joe", "Bob", '1994-08-01', "Male");

INSERT INTO patient (firstname, lastname, date_of_birth, sex)
VALUES ("Jen", "Bob", '1995-08-01', "Female");

INSERT INTO patient (firstname, lastname, date_of_birth, sex)
VALUES ("Ava", "Bob", '1994-08-01', "Female");


INSERT INTO acquisition (patient_id, eye_type, site_name, date_taken, operator_name)
VALUES (1, "Left", "Retispec", '2001-08-01', "Dr. Steve");

INSERT INTO acquisition (patient_id, eye_type, site_name, date_taken, operator_name)
VALUES (1, "Right", "Retispec", '2001-08-01', "Dr. Steve");