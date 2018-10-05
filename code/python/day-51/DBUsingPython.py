import ibm_db
dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "BLUDB"            
dsn_hostname = "dashdb-txn-sbox-yp-lon02-01.services.eu-gb.bluemix.net"
dsn_port = "50000"                
dsn_protocol = "TCPIP"          
dsn_uid = "hpz03638"      
dsn_pwd = "5181ngx4^6rsphg1"

dsn=(
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd)

#print(dsn)


try:
    conn = ibm_db.connect(dsn, "", "")
    print("Connected!")

except:
    print("Unable to connect to database")


#1 createstmt=ibm_db.exec_immediate(conn,"create table Employee(name varchar(20), id int, dept char(10))")

#2 to insert a record

"""ins="insert into Employee values('Amritsar','18','BCA')"
insertstmt=ibm_db.exec_immediate(conn,ins)"""

#3 to drop a table
#dropstmt=ibm_db.exec_immediate(conn,"drop table Employee")

#4 getting data from table
selectquery="select * from Employee"
selectstmt=ibm_db.exec_immediate(conn,selectquery)

while ibm_db.fetch_row(selectstmt)!=False:
    print("Name:",ibm_db.result(selectstmt,0)," ID: ",ibm_db.result(selectstmt,1)," Dept: ",ibm_db.result(selectstmt,2))

ibm_db.close(conn)
