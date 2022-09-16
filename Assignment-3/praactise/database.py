import pymysql
try:
    dbcon=pymysql.connect(host="localhost",user="root",passwd="",database="db")
    print("data base created")
except Exception as e:
    print(e)
# create table
cur=dbcon.cursor()

'''user=input("enter table name")
create_table=f"create table {user}(id int primary key,name text,city text)"
try:
    cur.execute(create_table)
    print("Table Created")
except Exception as e:
    print(e)'''
# insert table
'''user=int(input("How many User inserted"))
for i in range(user):
  id=input("Enter id")
  name=(input("Enter name"))
  city=(input("Enter city"))
  insert_table=f"Insert into stud values({},'{name}','{city}')"
  try: 
    cur.execute(insert_table)
    dbcon.commit()
    print("Record inserted")
  except Exception as e:
      print(e)'''
# update data
update_table="update stud set name='virat' where id=1" 
try:
    cur.execute(update_table)
    dbcon.commit()
    print("updated data")
except Exception as e:
    print(e)

# delete data
delete_data="delete from stud where id=7"
try:
    cur.execute(delete_data)
    dbcon.commit()
    print("record deleted")
except Exception as e:
    print(e)
# select data
select_data="select * from stud"    
try:
    cur.execute(select_data)
    show=cur.fetchall()
    for i in show:
        print(i[1
            ])
except Exception as e:
    print(e)       
#truncate
truncate_data="truncate table stud"
try:
    cur.execute(truncate_data)
    print("table deleted")
        
except Exception as e:
    print(e)   
    
# alter columd add uses
alter_table="alter table table name add columnname data type" 
  
    
    
    
    
    
        
             


    


    
        
    

        
        


