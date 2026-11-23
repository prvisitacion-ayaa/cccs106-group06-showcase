
import hashlib
import hmac
import secrets

from app.database.database import get_connection


# Password hashing settings
HASH_ALGORITHM = "pbkdf2_sha256"
HASH_ITERATIONS = 600_000


def hash_password(password):
    """Create a salted password hash."""

    salt = secrets.token_bytes(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        HASH_ITERATIONS
    )

    return (
        f"{HASH_ALGORITHM}$"
        f"{HASH_ITERATIONS}$"
        f"{salt.hex()}$"
        f"{password_hash.hex()}"
    )


def verify_password(password, stored_password):
    """
    Verify a password.

    Returns:
        (True, True)  - Valid legacy password; needs upgrading.
        (True, False) - Valid hashed password.
        (False, False) - Invalid password.
    """

    if stored_password.startswith(HASH_ALGORITHM + "$"):

        try:
            algorithm, iterations, salt_hex, hash_hex = (
                stored_password.split("$")
            )

            if algorithm != HASH_ALGORITHM:
                return False, False

            iterations = int(iterations)

            if not 100_000 <= iterations <= 2_000_000:
                return False, False

            salt = bytes.fromhex(salt_hex)
            expected_hash = bytes.fromhex(hash_hex)

            actual_hash = hashlib.pbkdf2_hmac(
                "sha256",
                password.encode("utf-8"),
                salt,
                iterations
            )

            return hmac.compare_digest(
                actual_hash,
                expected_hash
            ), False

        except (ValueError, TypeError):
            return False, False

    # Support existing accounts with plain-text passwords.
    is_valid = hmac.compare_digest(
        password,
        stored_password
    )

    return is_valid, is_valid


def register_user(full_name, email, password, course, year_level):

    email = email.strip().lower()
    connection = get_connection()
    cursor = connection.cursor()

    try:
        password_hash = hash_password(password)

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
                password_hash,
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

        is_valid, needs_upgrade = verify_password(
            password,
            user[3]
        )

        if not is_valid:
            return {
                "success": False,
                "message": "Incorrect password."
            }

        # Upgrade an old plain-text password after successful login.
        if needs_upgrade:
            new_password_hash = hash_password(password)

            cursor.execute(
                """
                UPDATE users
                SET password = ?
                WHERE id = ?
                """,
                (new_password_hash, user[0])
            )

            connection.commit()

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
