# Тапсырма 1

import psycopg2
from psycopg2 import sql
from db_query import*

class Database():
   def __init__(self) -> None:
      # Настроика
      self.conn = psycopg2.connect(database="db", user='postgres', password='123456', host='127.0.0.1', port= '5432') 
      self.cursor = self.conn.cursor()
   
   def Close(self):
      self.conn.commit()
      #self.conn.close()

   def create_table_1(self):
      self.cursor.execute(create_1)
      self.Close()
      print("The first table is created!")

   def create_table_2(self):
      self.cursor.execute(create_2)
      self.Close()
      print("The second table is created!")
      
   def create_table_3(self):
      self.cursor.execute(create_3)
      self.Close()
      print("The thrid table is created!")
   
   def create_table_4(self):
      self.cursor.execute(create_4)
      self.Close()
      print("The fouth table is created!")
   
   def create_table_5(self):
      self.cursor.execute(create_5)
      self.Close()
      print("The fifth table is created!")

   # Insert dep
   def insert_dep(self):
      self.cursor.execute(insert_dep)
      self.Close()   
   
   # Insert emp
   def insert_emp(self):
      self.cursor.execute(insert_emp)
      self.Close()   
   
   # Insert job
   def insert_job(self):
      self.cursor.execute(insert_job)
      self.Close()   
   
   # Insert count
   def insert_count(self):
      self.cursor.execute(insert_count)
      self.Close()   
   
   # Insert location
   def insert_location(self):
      self.cursor.execute(insert_location)
      self.Close()   
   
   def select_some(self, name: str):
      self.cursor.execute("SELECT first_name, last_name, salary, job_id FROM employees WHERE first_name='{}'".format(name))
      result = self.cursor.fetchall()
      print(result)
      self.Close()


'''
#Executing an MYSQL function using the execute() method
cursor.execute("select version()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ", data)

'''

if __name__ == "__main__":
   db = Database()
   # Таблицаларды құру

   #db.create_table_1()
   #db.create_table_2()
   #db.create_table_3()
   #db.create_table_4()
   #db.create_table_5()

   # Таблицаларға мәліметтер енгізу
   
   #db.insert_dep()
   #db.insert_emp()
   #db.insert_job()
   #db.insert_count()
   #db.insert_location()
   
   #db.cursor.execute("DROP TABLE employees")
   #db.cursor.execute("DROP TABLE location")
   #db.Close()

   db.select_some("Yerek")
   db.conn.close()