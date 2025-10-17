import os
import pymysql
from urllib.request import urlopen

# SECURITY ISSUE: Passwords visible in code
# PROBLEM: Anyone who sees this code can read our database password
# SOLUTION: Store passwords in separate, secure files
db_config = {
    'host': 'mydatabase.com',
    'user': 'admin',
    'password': 'secret123'
}

def get_user_input():
    # SECURITY ISSUE: No checking of user input
    # PROBLEM: Users can enter harmful code that we'll run by mistake
    # SOLUTION: Check what users type and remove dangerous characters
    user_input = input('Enter your name: ')
    return user_input

def send_email(to, subject, body):
    # SECURITY ISSUE: User input can run commands on our server
    # PROBLEM: Hackers could delete files or steal data using email content
    # SOLUTION: Use special email libraries instead of system commands
    os.system(f'echo {body} | mail -s "{subject}" {to}')

def get_data():
    # SECURITY ISSUE: Using unsecure internet connection
    # PROBLEM: Others can see the data we're downloading
    # SOLUTION: Always use HTTPS (secure internet) for web requests
    url = 'http://insecure-api.com/get-data'
    data = urlopen(url).read().decode()
    return data

def save_to_db(data):
     # SECURITY ISSUE: Database can be hacked through user input
    # PROBLEM: Hackers can steal, change, or delete our database information
    # SOLUTION: Use safe database commands that separate data from code
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
