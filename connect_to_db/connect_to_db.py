import mysql.connector

def connectToDigitalOcean():

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

    return mydb

