CREATE TABLE patient (
    id INT AUTO_INCREMENT,
    firstname VARCHAR(30) NOT NULL,
    lastname VARCHAR(30) NOT NULL,
    date_of_birth DATE NOT NULL,
    sex VARCHAR(30) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE acquisition (
    id INT AUTO_INCREMENT,
    patient_id INT NOT NULL,
    eye_type VARCHAR(5),
    site_name VARCHAR(30),
    date_taken DATE NOT NULL,
    operator_name VARCHAR(30) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (patient_id) REFERENCES patient(id)
);
