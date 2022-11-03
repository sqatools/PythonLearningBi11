import sqlite3
import logging

logging.basicConfig(filename='database.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
logging.warning('This will get logged to a file')
logger = logging.getLogger(__name__)

con = sqlite3.connect("student_record.db")

def create_table(tablename):
    query = f"create table {tablename} (name TEXT, email TEXT, mobile INT,  address TEXT);"
    con.execute(query)
    print("Query executed successfully")

def insert_data_to_the_table(tablename, query=None):
    if query is None:
        query = f"INSERT INTO {tablename}(name,  email, mobile, address) values('yogesh', 'yogesh@gmail.com', 78798798, 'Mumbai')"
    try:
        con.execute(query)
        con.commit()
    except Exception as e:
        logger.debug(e)

def create_fake_data(file_name='dummy_data.txt'):
    with open(file_name, 'a') as file:
        for i in range(1,301):
            line = f"yogesh_{i}, yogesh{i}@gmail.com, {78798798+i}, Mumbai \n"
            file.write(line)


def insert_bulk_data_from_file(file_name='dummy_data.txt', table_name= "student"):
    with open(file_name, 'r') as file:
        file_lines = file.readlines()
        for line in file_lines:
            try :
                lines_data = line.split(",")
                name = lines_data[0].strip()
                email = lines_data[1].strip()
                mobile = lines_data[2].strip()
                address = lines_data[3].strip()
                if name and email and mobile and address :
                    print("All field has proper value")
                    query = f"INSERT INTO {table_name}(name,  email, mobile, address) values('{name}', '{email}', {mobile}, '{address}')"
                    insert_data_to_the_table(table_name, query)
                else:
                    print("Any field does not have proper value")
                    logger.info(line)

            except Exception as e:
                logger.info(line)
                logger.debug(e)

def notify_info(info, file_name='data_insert_info.txt'):
    with open(file_name, "a") as file:
        file.write(info)

def notify_bulk_data_import(file_name='dummy_data.txt', table_name= "student"):
    with open(file_name, 'r') as file:
        file_lines = file.readlines()
        for line in file_lines:
            try :
                lines_data = line.split(",")
                name = lines_data[0].strip()
                email = lines_data[1].strip()
                mobile = lines_data[2].strip()
                address = lines_data[3].strip()
                if name and email and mobile and address :
                    print("All field has proper value")
                    query = f"INSERT INTO {table_name}(name,  email, mobile, address) values('{name}', '{email}', {mobile}, '{address}')"
                    insert_data_to_the_table(table_name, query)
                else:
                    print("Any field does not have proper value")
                    logger.info(line)
                    
                if file_lines.index(line)%100 == 0 and file_lines.index(line) != 0:
                    info_text = f"{file_lines.index(line)} records successfully updated in the database"
                    logger.info("#" * 50)
                    logger.info(info_text)
                    logger.info("#" * 50)
                    #notify_info(info=info_text)

            except Exception as e:
                logger.info(line)
                logger.debug(e)

def generate_fake_Data_With_faker():
    from faker import Faker
    fk = Faker()
    print(dir(fk))
    for _ in range(2000):
        with open("faker_data.txt", "a") as file:
            #print(fk.name(),  fk.email(), fk.address(),  fk.phone_number())
            file.write(f"{fk.name()}, {fk.email()}, {fk.address()},  {fk.phone_number()}, {fk.city()}\n")

#create_table('student')
#insert_data_to_the_table('student')
#con.close()
#create_fake_data()
#insert_bulk_data_from_file()
#notify_bulk_data_import()
#con.close()

generate_fake_Data_With_faker()