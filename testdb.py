import pymysql

HOSTNAME= 'localhost'
USER = 'root'
PASS = 'root'
DB = 'employeedb'
TABLE = 'details'

try:
    conn = pymysql.connect(host = HOSTNAME , user = USER , password = PASS , db = DB)
except:
    raise Exception("error in credentials")
finally:
    c = conn.cursor()

insert_queries = []

def insert_records():
    choice = "y"

    while(choice.lower() == "y"):
        name = input("enter your name:")
        address = input("enter your address:")
        cid = int(input("enter your id number:"))
        salary = int(input("enter your salary"))
        insert_queries.append(format_statement(name,address,cid,salary))

        choice = input("enter y/n")

    try:
        for insert in insert_queries:
            print("Inserted values:" , insert[26:])
            c.execute(insert)


        conn.commit()
    except Exception as error:
        print(error)
        conn.rollback()

def format_statement(name,address,cid,salary):
    return("insert into {0} values('{1}','{2}',{3},{4})".format(TABLE , name, address, cid , salary))



def see_records():

    emp_name = str(input("enter the name of the employee or their employee id:"))
    print("{0:<20}{1:20}{2:<20}{3:<10}".format("name", "address", "employee id", "salary"))
    print("----------------------------------------------------------------------")

    c.execute("select * from {0} where name = '{1}' or cid = {2} ".format(TABLE,emp_name,emp_name))
    allrecords = c.fetchall()
    for i in allrecords:
        print("{0:<20}{1:20}{2:<20}{3:<10}".format(i[0],i[1],i[2],i[3],))


def delete_records():
    emp_names =(input("input name to be deleted: "))

    try:
        c.execute("delete from {0} where name = '{1}'".format(TABLE,emp_names))

        print("successfully deleted !!")
        conn.commit()

    except:
        print("error")
        conn.rollback()



def update_record():
    old_name = input("Enter the name to be replaced")
    new_name = input("Enter the name to be replaced with")

    query = "update {} set name='{}' where name = '{}'".format(TABLE, new_name, old_name)

    try:
        c.execute(query)

    except:
        raise Exception("Error")
        conn.rollback()

    conn.commit()



def main():


    print("Select Option\n1.Insert Records\n2.See all Records\n3.Delete Records\n4.Update Name")
    user_choice = input("Enter your choice")
    if user_choice == '1':
        insert_records()
    elif user_choice == '2':
        see_records()
    elif user_choice == '3':
        delete_records()
    elif user_choice == '4':
        update_record()
    else:
        print("Wrong choice")

    conn.close()


if __name__ == '__main__':
    main()
