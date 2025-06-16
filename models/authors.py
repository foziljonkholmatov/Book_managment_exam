from db.connection import execute_query

def add_author(full_name: str):
    query = "INSERT INTO authors (full_name) VALUES (%s)"
    execute_query(query, (full_name,))

def get_all_authors():
    query = "SELECT * FROM authors ORDER BY id"
    return execute_query(query, fetch="all")
