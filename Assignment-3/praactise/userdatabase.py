
import pymysql
try:
    dbcon=pymysql.connect(host="localhost",user="root",password="",database="user")
    print("database created")
except Exception as e:
    print(e)

# Create table
cur=dbcon.cursor()

'''user=input("Enter table name:-")  
create_table=f"Create table {user} (id int primary key,name text,city text,grade text)"
try:
    cur.execute(create_table)
    print("table created")
except Exception as e:
    print(e)'''

# insert data
''''a=int(input("how many insert data:-"))
for i in range(a):
    id=input("Enter your id:-")
    name=input("Enter your name:-")
    city=input("Enter your city:-")
    grade=input("Enter your grade:-")

    insert_data=f"Insert into info values({id},'{name}','{city}','{grade}')"
    try:

        cur.execute(insert_data)
        dbcon.commit()
        print("Data inserted")
    except Exception as e:
        print(e)    '''
#update data
user=int(input("how many you changes"))
for i in range(user):

    a=input("what you change:-")
    aa=input("new update:-")
    b=input("which id")
    update_data=f"Update info set {a}='{aa}' where id={b} "
    try:
        cur.execute(update_data)
        dbcon.commit()
        print("record updated")
    except Exception as e:
        print(e)
         

#delete data
'''a=input("which want you delete")
delete_data=f"delete from info where id={a}" 
try:
    cur.execute(delete_data)
    dbcon.commit()
    print("data deleted")
except Exception as e:
    print(e)    '''
#alter colum add
'''users=input("enter new column")
alter_table=f"alter table info add {users} text"    
try:
    cur.execute(alter_table)
    dbcon.commit()
    print("Column added")
except Exception as e:
    print(e)'''

#select from
''''select__data="select * from info"
try:
    cur.execute(select__data)
    show=cur.fetchall()
    for i in  show:
        print(i[4])    
except Exception as e:
    print(e)'''        
      
