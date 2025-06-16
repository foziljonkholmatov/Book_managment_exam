from db.connection import execute_query

def add_book(title, author_id, published_at, total_count):
    query = """
    INSERT INTO books (title, author_id, published_at, total_count, available_count)
    VALUES (%s, %s, %s, %s, %s)
    """
    execute_query(query, (title, author_id, published_at, total_count, total_count))

def update_book(book_id, title, author_id, published_at, total_count, available_count):
    query = """
    UPDATE books
    SET title=%s, author_id=%s, published_at=%s, total_count=%s, available_count=%s
    WHERE id=%s
    """
    execute_query(query, (title, author_id, published_at, total_count, available_count, book_id))

def delete_book(book_id):
    query = "DELETE FROM books WHERE id=%s"
    execute_query(query, (book_id,))

def get_all_books():
    query = """
    SELECT b.id, b.title, a.full_name AS author, b.published_at, b.total_count, b.available_count
    FROM books b
    JOIN authors a ON b.author_id = a.id
    ORDER BY b.id
    """
    return execute_query(query, fetch="all")

def search_books_by_author(author_name):
    query = """
    SELECT b.id, b.title, a.full_name, b.published_at, b.available_count
    FROM books b
    JOIN authors a ON b.author_id = a.id
    WHERE LOWER(a.full_name) LIKE %s
    """
    return execute_query(query, (f"%{author_name.lower()}%",), fetch="all")
