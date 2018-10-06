import pandas as pd
import ibm_db
import ibm_db_dbi

dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "BLUDB"
dsn_hostname = "dashdb-txn-sbox-yp-lon02-01.services.eu-gb.bluemix.net"
dsn_port = "50000"
dsn_protocol = "TCPIP"
dsn_uid = "hpz03638"
dsn_pwd = "5181ngx4^6rsphg1"

dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd)


try:
    conn = ibm_db.connect(dsn, "", "")
    print("Connected!")

except:
    print("Unable to connect to database")



pconn=ibm_db_dbi.Connection(conn)

selectstmt="select * from Employee"
pdf=pd.read_sql(selectstmt,pconn)

print(pdf.NAME[0])

print(pdf)

ibm_db.close(conn)