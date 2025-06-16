from db.connection import execute_query

def get_all_users():
    query = "SELECT * FROM users ORDER BY id"
    return execute_query(query, fetch="all")

def get_user_by_email_and_password(email: str, password: str):
    query = "SELECT * FROM users WHERE email = %s AND password = %s"
    return execute_query(query, (email, password), fetch="one")


def register_user(full_name: str, email: str, password: str):
    query = "INSERT INTO users (full_name, email, password) VALUES (%s, %s, %s) RETURNING id"
    result = execute_query(query, (full_name, email, password), fetch="one")
    return result['id'] if result else None


def get_admin_by_email_and_password(email: str, password: str):
    query = "SELECT * FROM admins WHERE email = %s AND password = %s"
    return execute_query(query, (email, password), fetch="one")

def register_admin(full_name: str, email: str, password: str):
    query = "INSERT INTO admins (full_name, email, password) VALUES (%s, %s, %s) RETURNING id"
    result = execute_query(query, (full_name, email, password), fetch="one")
    return result['id'] if result else None


