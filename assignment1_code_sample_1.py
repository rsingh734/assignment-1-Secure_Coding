import os
import pymysql
from urllib.request import urlopen
import smtplib
from email.mime.text import MIMEText

# Load database configuration from environment variables
db_config = {
    'host': os.getenv('DB_HOST', 'mydatabase.com'),
    'user': os.getenv('DB_USER', 'admin'),
    'password': os.getenv('DB_PASSWORD', 'secret123')  # In production, ensure this is set securely
}

def get_user_input():
    # Sanitize user input to prevent injection or harmful characters
    user_input = input('Enter your name: ')
    # Remove potentially dangerous characters (e.g., shell metacharacters)
    sanitized_input = ''.join(c for c in user_input if c.isalnum() or c in ' ')
    return sanitized_input

def send_email(to, subject, body):
    # Use smtplib for secure email sending instead of system commands
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'your_email@example.com'  # Replace with actual sender
    msg['To'] = to

    # Note: In production, use secure SMTP server and authentication
    server = smtplib.SMTP('smtp.example.com', 587)  # Replace with actual SMTP server
    server.starttls()
    server.login('your_username', 'your_password')  # Replace with credentials
    server.sendmail('your_email@example.com', to, msg.as_string())
    server.quit()

def get_data():
    # Use HTTPS for secure web requests
    url = 'https://secure-api.com/get-data'  # Assuming the API supports HTTPS
    data = urlopen(url).read().decode()
    return data

def save_to_db(data):
    # Use parameterized queries to prevent SQL injection
    query = "INSERT INTO mytable (column1, column2) VALUES (%s, %s)"
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query, (data, 'Another Value'))
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)
