import mysql.connector as conn

def connect(host = "localhost" , user = "root" , password = "", db_name = ""):
  if db_name != "":
    mydb = conn.connect(
    host = host,
    user = user, 
    password = password,
    database = db_name
    )
    return mydb
  else:
    mydb = conn.connect(
      host = host,
      user = user,
      password = password
    ) 


connect()  

# Create Database
def create_database(db_name):
  try:
    mydb = connect()
    mycursor = mydb.cursor()
    query  = "CREATE DATABASE " + db_name 
    mycursor.execute(query)
    mycursor.close()
    mydb.close() 
  except Exception as e:
    print(e)

create_database("employes")


#============CREATE TABLE======================

def create_table(db_name, table_name):
    try:
        mydb = connect(db_name=db_name)
        mycursor = mydb.cursor()
        query = "CREATE TABLE "+ table_name +"(id integer primary key auto_increment, name varchar(255), dept varchar(255))"
        mycursor.execute(query)
        mycursor.close()
        mydb.close()
    except Exception as e:
        print(e)

create_table("employes","employes_info")

#============CREATE TABLE======================

def create_table(db_name, table_name):
  try:
      mydb = connect(db_name = db_name)
      mycursor = mydb.cursor()
      query = "CREATE TABLE "+ table_name +"(id integer primary key auto_increment, name varchar(255), phone varchar(255), salary varchar(255))"
     
      mycursor.execute(query)
      mycursor.close()
      mydb.close()
  except Exception as e:
      print(e) 

create_table("employes","employes_salary")


#============INSERT DATA INTO DATABASE======================

def insert_data(db_name, table_name, name, phone , salary):
  try:
    mydb = connect(db_name = db_name)
    mycursor = mydb.cursor()
    query = "INSERT INTO "+ table_name + "(id, name, phone, salary) VALUES(0, %s , %s, %s) "
    values = (name , phone, salary)
    mycursor.execute(query, values)
    mydb.commit()
    mycursor.close()
    mydb.close()
  except Exception as e:
    print(e)

insert_data("employes", "employes_salary", "Imtanan" , "01815514298" , "100000" )   
insert_data("employes", "employes_salary", "Asif" , "01819898989" , "120000" ) 
insert_data("employes", "employes_salary", "Anas" , "01814848484" , "130000" )

def fetch_data(db_name, table_name):
  try:
    mydb = connect(db_name = db_name)
    mycursor = mydb.cursor()
    query = "SELECT * FROM " + table_name
    mycursor.execute(query)
    res = mycursor.fetchall()
    for x in res:
      print(x)
    mycursor.close()
    mydb.close()
  except Exception as e:
    print(e)  

fetch_data("employes", "employes_salary")

