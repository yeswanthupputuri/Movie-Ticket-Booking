use bookyourticket;

CREATE TABLE screen_11(
row_s11 int ,
Col INT,
Name VARCHAR(50),
Gender VARCHAR(20),
PhoneNo VARCHAR(10),
Status VARCHAR(10),
PRIMARY KEY(row_s11,Col));

CREATE TABLE screen_12(
row_s12 INT,
Col INT,
Name VARCHAR(50),
Gender VARCHAR(20),
PhoneNo VARCHAR(10),
Status VARCHAR(10),
PRIMARY KEY(row_s12,Col));

CREATE TABLE statistics(
Screen VARCHAR(20),
NoOfTickets INT,
Percenatge INT,
CurrentIncome INT,
TotolIncome INT);

INSERT INTO statistics(Screen ,TotolIncome)
VALUES("screen1",640);
INSERT INTO statistics (Screen ,TotolIncome)
VALUES ("screen2",640);

update statistics set TotolIncome = 490 where screen = "screen1";

