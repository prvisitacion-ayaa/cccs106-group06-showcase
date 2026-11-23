
import sqlite3
from app.database.database import get_connection

def is_valid_id(value):
    return (
        isinstance(value, int)
        and not isinstance(value, bool)
        and value > 0
    )

def get_learnpoints_balance(user_id):
    if not is_valid_id(user_id):
        return 0
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT COALESCE(SUM(points), 0)
            FROM learnpoints
            WHERE user_id = ?
            """,
            (user_id,)
        )

        return cursor.fetchone()[0]

    except sqlite3.Error as error:
        print("Error retrieving LearnPoints balance:", error)
        return 0

    finally:
        connection.close()


def award_learnpoints(note_id, points):
    if not is_valid_id(note_id):
        return {
            "success": False,
            "message": "Invalid resource ID."
        }

    if isinstance(points, bool) or not isinstance(points, int) or points <= 0:
        return {
            "success": False,
            "message": "Points must be a positive integer."
        }
    connection = get_connection()

    try:

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT user_id, status
            FROM notes
            WHERE id = ?
            """,
            (note_id,)
        )

        note = cursor.fetchone()

        if note is None:
            return {
                "success": False,
                "message": "Resource not found."
            }

        user_id, status = note

        if status != "approved":
            return {
                "success": False,
                "message": "Only approved resources can earn LearnPoints."
            }

        cursor.execute(
            """
            INSERT INTO learnpoints (
                user_id, points, reason, source_note_id
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                user_id,
                points,
                "Approved academic resource contribution",
                note_id
            )
        )

        connection.commit()

        return {
            "success": True,
            "points_awarded": points,
            "user_id": user_id,
            "message": "LearnPoints awarded successfully."
        }

    except sqlite3.IntegrityError:
        connection.rollback()

        return {
            "success": False,
            "message": "LearnPoints have already been awarded for this note."
        }

    except sqlite3.Error as error:
        connection.rollback()

        return {
            "success": False,
            "message": str(error)
        }

    finally:
        connection.close()


def get_available_premium_features():
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT id, feature_name, description, points_required
            FROM premium_features
            WHERE is_available = 1
            ORDER BY points_required ASC
            """
        )

        features = cursor.fetchall()

        return [
            {
                "id": feature[0],
                "feature_name": feature[1],
                "description": feature[2],
                "points_required": feature[3]
            }
            for feature in features
        ]

    except sqlite3.Error as error:
        print("Error retrieving premium features:", error)
        return []

    finally:
        connection.close()


def redeem_premium_feature(user_id, feature_id):
    if not is_valid_id(user_id):
        return {
            "success": False,
            "message": "Invalid student ID."
        }

    if not is_valid_id(feature_id):
        return {
            "success": False,
            "message": "Invalid premium feature ID."
        }
    connection = get_connection()

    try:
        cursor = connection.cursor()

        # Prevent simultaneous redemptions from overspending
        cursor.execute("BEGIN IMMEDIATE")

        cursor.execute(
            "SELECT id FROM users WHERE id = ? AND role = 'student'",
            (user_id,)
        )

        if cursor.fetchone() is None:
            connection.rollback()
            return {
                "success": False,
                "message": "Student account not found."
            }

        cursor.execute(
            """
            SELECT feature_name, points_required
            FROM premium_features
            WHERE id = ? AND is_available = 1
            """,
            (feature_id,)
        )

        feature = cursor.fetchone()

        if feature is None:
            connection.rollback()
            return {
                "success": False,
                "message": "Premium feature not found or unavailable."
        }

        feature_name, points_required = feature

        cursor.execute(
            """
            SELECT COALESCE(SUM(points), 0)
            FROM learnpoints
            WHERE user_id = ?
            """,
            (user_id,)
        )

        balance = cursor.fetchone()[0]

        if balance < points_required:
            connection.rollback()
            return {
                "success": False,
                "message": "Insufficient LearnPoints."
        }

        cursor.execute(
            """
            INSERT INTO learnpoints (
                user_id, points, reason, source_note_id
            )
            VALUES (?, ?, ?, NULL)
            """,
            (
                user_id,
                -points_required,
                f"Redeemed premium feature: {feature_name}"
            )
        )

        cursor.execute(
            """
            INSERT INTO premium_redemptions (
                user_id, feature_id, points_used
            )
            VALUES (?, ?, ?)
            """,
            (user_id, feature_id, points_required)
        )

        redemption_id = cursor.lastrowid

        connection.commit()

        return {
            "success": True,
            "redemption_id": redemption_id,
            "feature_name": feature_name,
            "points_used": points_required,
            "remaining_balance": balance - points_required,
            "message": "Premium feature redeemed successfully."
        }

    except sqlite3.Error as error:
        connection.rollback()

        return {
            "success": False,
            "message": str(error)
        }

    finally:
        connection.close()


def get_redemption_history(user_id):
    if not is_valid_id(user_id):
        return []
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                pr.id,
                pf.feature_name,
                pr.points_used,
                pr.redeemed_at
            FROM premium_redemptions pr
            JOIN premium_features pf
                ON pr.feature_id = pf.id
            WHERE pr.user_id = ?
            ORDER BY pr.redeemed_at DESC, pr.id DESC
            """,
            (user_id,)
        )

        redemptions = cursor.fetchall()

        return [
            {
                "redemption_id": item[0],
                "feature_name": item[1],
                "points_used": item[2],
                "redeemed_at": item[3]
            }
            for item in redemptions
        ]

    except sqlite3.Error as error:
        print("Error retrieving redemption history:", error)
        return []

    finally:
        connection.close()
