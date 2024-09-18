CREATE TABLE missingdata(
   ID   INTEGER,
   Name VARCHAR(8),
   Age  INTEGER,
   City VARCHAR(10)
);
INSERT INTO missingdata(ID,Name,Age,City) VALUES (1,'Jeremy',23,'Bristol');
INSERT INTO missingdata(ID,Name,Age,City) VALUES (2,'Michelle',30,NULL);
INSERT INTO missingdata(ID,Name,Age,City) VALUES (3,NULL,46,'Lincoln');
INSERT INTO missingdata(ID,Name,Age,City) VALUES (4,'Indy',NULL,'Cardiff');
INSERT INTO missingdata(ID,Name,Age,City) VALUES (5,'Amber',25,NULL);
INSERT INTO missingdata(ID,Name,Age,City) VALUES (6,'Sarah',70,'Liverpool');
INSERT INTO missingdata(ID,Name,Age,City) VALUES (7,'Jack',NULL,'Swansea');
INSERT INTO missingdata(ID,Name,Age,City) VALUES (8,'Anna',68,'Birmingham');
INSERT INTO missingdata(ID,Name,Age,City) VALUES (9,'Juliet',58,NULL);
