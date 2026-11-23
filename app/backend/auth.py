from app.database.database import get_connection


def register_user(
    full_name,
    email,
    password,
    course,
    year_level
):

    email = email.strip().lower()

    connection = get_connection()
    cursor = connection.cursor()

    try:

        cursor.execute(
            """
            INSERT INTO users
            (
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
                full_name.strip(),
                course.strip(),
                year_level.strip()
            )
        )

        connection.commit()

        return {
            "success": True,
            "message": "Account created successfully!"
        }

    except Exception as error:

        print("REGISTRATION DATABASE ERROR:", error)

        if "UNIQUE constraint failed" in str(error):

            return {
                "success": False,
                "message": "This email is already registered."
            }

        return {
            "success": False,
            "message": "Registration failed."
        }

    finally:
        connection.close()


def login_user(email, password):

    email = email.strip().lower()

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

        user = cursor.fetchone()

        if user is None:

            return {
                "success": False,
                "message": "Account not found."
            }

        if password != user[3]:

            return {
                "success": False,
                "message": "Incorrect password."
            }

        return {
            "success": True,
            "message": "Login successful!",
            "user": {
                "id": user[0],
                "full_name": user[1],
                "email": user[2],
                "course": user[4],
                "year_level": user[5],
                "role": user[6]
            }
        }

    except Exception as error:

        print("LOGIN DATABASE ERROR:", error)

        return {
            "success": False,
            "message": "Login failed."
        }

    finally:
        connection.close()