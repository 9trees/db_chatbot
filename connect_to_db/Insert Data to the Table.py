import mysql.connector

mydb = mysql.connector.connect(
    host="db-mysql-blr1-64778-do-user-11792980-0.b.db.ondigitalocean.com",
    user="doadmin",
    password="AVNS_Gls22gAwAQoB20qXQNV",
    port='25060',
    database="defaultdb",
    ssl_ca="""MIIEQTCCAqmgAwIBAgIUTTxkJriF/STHMdyP+vR62sQ2VhcwDQYJKoZIhvcNAQEM
BQAwOjE4MDYGA1UEAwwvNTFmY2RjODctN2JjZC00ZTU0LWJjMGItZmYwZjIyNzFl
NGZkIFByb2plY3QgQ0EwHhcNMjIwNjE2MDkxNDM5WhcNMzIwNjEzMDkxNDM5WjA6
MTgwNgYDVQQDDC81MWZjZGM4Ny03YmNkLTRlNTQtYmMwYi1mZjBmMjI3MWU0ZmQg
UHJvamVjdCBDQTCCAaIwDQYJKoZIhvcNAQEBBQADggGPADCCAYoCggGBANl2fjbE
Rm71nyB1HvZPNIBESNhXwEfq3NgUOUVOLV68zWqvN2zt50RnSQd6mRx8qDle4Ciz
JrngxO9oKhKn23HhnbXGEakjpGu9yy4rftXAn8m7eK0s2XFl/9QvNm7QZlI8LJ7J
Eu80Umkb/zu5xtqEkOarZeatRnjNmpDxIlpLJlPZanvtB81xnqlK7chh8vcJ6TXL
+BY1r5SITmLBnmNMTJF2vhfZOV6Kl6O0HOC4m6GabsoFcmvE+gOoV6OqqTzA1+MR
/aslR8mJRl531nShXdMVbSjynK2+qd+u8rZ4zcyDY813bWJY6VBm5wKf0y+b96in
CSFiOZJxKCJBn1+eHRePEEBmAw0l5W0TbYuOaoTzFJZHyAnU/+DzOqygSvm6IP0a
grtL13gCWGT+6vbTAl0fPEaIAIxhiIBVNSz89+o+zFQ6zg/AoXwexCTKCtlDtJRz
aj+vizhmOPQUmUAGALEer09H1mkWFUlYE4kbP3Idg+mN3sw//vo6K5NS4wIDAQAB
oz8wPTAdBgNVHQ4EFgQUbpqjaEeYBtR4gc16uqy1iVFAZF4wDwYDVR0TBAgwBgEB
/wIBADALBgNVHQ8EBAMCAQYwDQYJKoZIhvcNAQEMBQADggGBACK8vN2tZzvtJ7yx
xkBQmX0ya+ZlMOg/rHaBSzNZFmRwUq+LUktWhtnV5W5k2OVz4A92UCvlk/j37WJm
7w6ZEnAplOq4675pFHhSAXNRs4SyDX14zLD0Obrx1jTF9iXzDKxYxyzsR2F8/Y9C
f9aWSxuKaKb2njvC67Y2gi/1LlmggbYzklx29NfsVcssYBY34TnqT7n/3vHPk+qH
tAWusCksUluwBci5XHxd2ec6xlkR5L5IGHVipeBuZ+n59ge2uNPmtyi9/y1psgnA
CGitDg8Zbn1OtdEFuFP8fJ3RaDVj3ctF8zZ4HEfvoa3fyf7glaaI8iYKCjsDAQ/B
YKiSQuoy3WzzKbZvB6iRfkJqsjj7qd9QMgMkuLNLdomx5roj4MUMFIFUbBOOhzCZ
igpFtTE36QQpRab4FItYOhoygiw4QLxKkKnwOEAu2XXOSjsnyF+NsUAvSbci2lBJ
LBxiCOqsZhO/rnQCn3ujlZProt87v8EQSrJcnzZ53qKB5RY2fQ=="""
)


def rowToDict(cursor):
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    return results


cursor = mydb.cursor()
cursor.execute("""set sql_require_primary_key = off;""")
mydb.commit()

cursor.execute("""
CREATE TABLE `DT_test_Table1` (
`DT_ID` VARCHAR(150),
`AREA` VARCHAR(150),
`ALERT` VARCHAR(150),
`RATED_CAPACITY` INT,
`TIME_STAMP` Datetime(6),
`LOAD_DATA` INT,
`ALERT_STATUS` VARCHAR(150),
`ENERGY` INT,
`MAKE` VARCHAR(150),
`MANUFACTURE_YEAR` INT
);""")
mydb.commit()

cursor.execute("""INSERT INTO DT_test_Table1 (DT_ID,  AREA, ALERT, RATED_CAPACITY, TIME_STAMP, LOAD_DATA, ALERT_STATUS, ENERGY , MAKE , MANUFACTURE_YEAR)
VALUES
('Sno 100009','Nungampakkam','Aert 1',750,'2021-06-12 00:00:00',300,'clear',808069,'Siemens',1994),
('Sno 100010','TNagar','Alert 3',300,'2021-06-13 00:00:00',100,'pending',818069,'BDI',2000),
('Sno 100011','Velacherry','Alert 5',750,'2021-06-14 00:00:00',100,'clear',518069,'Siemens',1996),
('Sno 100012','Madipakkam','Alert 3',750,'2021-08-21 00:00:00',100,'pending',618069,'Siemens',1992),
('Sno 100013','Anna Nagar','Alert 10',750,'2022-06-14 00:00:00',500,'clear',613456,'BDI',1995),
('Sno 100014','R A Puram','Alert 3',750,'2022-01-14 00:00:00',500,'pending',789654,'Siemens',1995),
('Sno 100015','Anna Arivalyam','Alert 5',500,'2022-01-24 00:00:00',300,'clear',126784,'Siemens',1995),
('Sno 100016','Arcot','Alert 3',500,'2021-11-13 00:00:00',400,'pending',674567,'Siemens',1999),
('Sno 100017','Valluvar kottam','Alert 4',500,'2021-11-18 00:00:00',500,'pending',879654,'Triad Magnetics',1992),
('Sno 100009','Nungampakkam','Aert 1',750,'2022-06-12 00:00:00',300,'clear',808069,'Siemens',1994),
('Sno 100010','TNagar','Alert 3',300,'2022-06-13 00:00:00',100,'clear',818069,'BDI',2000),
('Sno 100011','Velacherry','Alert 5',750,'2022-06-14 00:00:00',100,'clear',518069,'Siemens',1996),
('Sno 100012','Madipakkam','Alert 3',750,'2022-06-15 00:00:00',100,'clear',618069,'Siemens',1992),
('Sno 100013','Anna Nagar','Alert 10',750,'2022-06-16 00:00:00',500,'clear',613456,'BDI',1995),
('Sno 100014','R A Puram','Alert 3',750,'2022-06-17 00:00:00',500,'pending',789654,'Siemens',1995),
('Sno 100015','Anna Arivalyam','Alert 5',500,'2022-06-18 00:00:00',300,'pending',126784,'Siemens',1995),
('Sno 100016','Arcot','Alert 3',500,'2022-06-19 00:00:00',400,'pending',674567,'Siemens',1999),
('Sno 100017','Valluvar kottam','Alert 4',500,'2022-06-20 00:00:00',500,'pending',879654,'Triad Magnetics',1992),
('Sno 100009','Nungampakkam','Alert 3',750,'2022-07-25 00:00:00',300,'pending',808069,'Siemens',1994),
('Sno 100010','TNagar','Alert 5',300,'2022-07-26 00:00:00',100,'pending',818069,'BDI',2000),
('Sno 100011','Velacherry','Alert 3',750,'2022-07-27 00:00:00',100,'pending',518069,'Siemens',1996),
('Sno 100012','Madipakkam','Alert 4',750,'2022-07-28 00:00:00',100,'pending',618069,'Siemens',1992),
('Sno 100013','Anna Nagar','Alert 3',750,'2022-07-29 00:00:00',500,'clear',613456,'BDI',1995),
('Sno 100014','R A Puram','Alert 5',750,'2022-07-30 00:00:00',500,'pending',789654,'Siemens',1995),
('Sno 100015','Anna Arivalyam','Alert 3',500,'2022-07-31 00:00:00',300,'pending',126784,'Siemens',1995),
('Sno 100016','Arcot','Alert 4',500,'2022-08-01 00:00:00',400,'pending',674567,'Siemens',1999),
('Sno 100017','Valluvar kottam','Alert 4',500,'2022-08-02 00:00:00',500,'pending',879654,'Triad Magnetics',1992);""")

mydb.commit()

mydb.close()