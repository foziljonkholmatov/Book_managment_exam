from db.connection import execute_query

def borrow_book(user_id, book_id):
    query = """
    INSERT INTO borrows (user_id, book_id) VALUES (%s, %s);
    UPDATE books SET available_count = available_count - 1 WHERE id = %s AND available_count > 0
    """
    execute_query(query, (user_id, book_id, book_id))

def return_book(user_id, book_id):
    query = """
    UPDATE borrows
    SET returned_at = CURRENT_TIMESTAMP
    WHERE user_id = %s AND book_id = %s AND returned_at IS NULL;

    UPDATE books
    SET available_count = available_count + 1
    WHERE id = %s
    """
    execute_query(query, (user_id, book_id, book_id))

def get_user_borrows(user_id):
    query = """
    SELECT b.title, br.borrowed_at, br.returned_at
    FROM borrows br
    JOIN books b ON br.book_id = b.id
    WHERE br.user_id = %s
    ORDER BY br.borrowed_at DESC
    """
    return execute_query(query, (user_id,), fetch="all")

def get_all_borrows():
    query = """
    SELECT u.full_name, b.title, br.borrowed_at, br.returned_at
    FROM borrows br
    JOIN users u ON br.user_id = u.id
    JOIN books b ON br.book_id = b.id
    ORDER BY br.borrowed_at DESC
    """
    return execute_query(query, fetch="all")
