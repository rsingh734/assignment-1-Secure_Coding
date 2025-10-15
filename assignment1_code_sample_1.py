

import os
import pymysql
from urllib.request import urlopen

'''
The vulnerabiity here is that, the database credentials is hard coded in the code.
If an attacker gets access to this code then they have free access to the database.

A07:2021 – Identification and Authentication Failures
'''

db_config = {
    'host': 'mydatabase.com',
    'user': 'admin',
    'password': 'secret123'
}


'''
The vulnerability here is that we are taking the user input directly without validation and the user input may contain malious code.

A03:2021 – Injection
'''

def get_user_input():
    user_input = input('Enter your name: ')
    return user_input

def send_email(to, subject, body):
    os.system(f'echo {body} | mail -s "{subject}" {to}')

'''
The vulnerability here is that the external data is not validated

A10:2021 – Server-Side Request Forgery (SSRF)
'''
def get_data():
    url = 'http://insecure-api.com/get-data'
    data = urlopen(url).read().decode()
    return data


'''
The vulnerabilty here is that the unvalidated data is stored in the database directly, which has exposed the database to SQL Injection.

A03:2021 – Injection
'''

def save_to_db(data):
    query = f"INSERT INTO mytable (column1, column2) VALUES ('{data}', 'Another Value')"
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)
