from app.database.database import get_connection


def create_user(
    full_name,
    email,
    password,
    course,
    year_level
):

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO users (
                username,
                email,
                password,
                full_name,
                course,
                year_level
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                email,
                email,
                password,
                full_name,
                course,
                year_level
            )
        )

        connection.commit()

        return True, "Account created successfully!"

    except Exception as error:

        print("CREATE USER ERROR:", error)

        if "UNIQUE constraint failed" in str(error):
            return False, "This email is already registered."

        return False, "Registration failed."

    finally:
        connection.close()


def get_user_by_email(email):

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            SELECT
                id,
                full_name,
                email,
                password,
                course,
                year_level,
                role
            FROM users
            WHERE email = ?
            """,
            (email,)
        )

        return cursor.fetchone()

    finally:
        connection.close()


def get_user_by_id(user_id):

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            SELECT
                id,
                full_name,
                email,
                course,
                year_level,
                role,
                created_at
            FROM users
            WHERE id = ?
            """,
            (user_id,)
        )

        return cursor.fetchone()

    finally:
        connection.close()


def get_all_users():

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            SELECT
                id,
                full_name,
                email,
                course,
                year_level,
                role,
                created_at
            FROM users
            ORDER BY id
            """
        )

        return cursor.fetchall()

    finally:
        connection.close()