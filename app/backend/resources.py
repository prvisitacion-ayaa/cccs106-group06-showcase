
import sqlite3
from app.database.database import get_connection


def create_resource(
    user_id,
    title,
    subject,
    topic,
    course,
    description,
    file_path=None
):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO notes (
                user_id,
                title,
                subject,
                topic,
                course,
                description,
                file_path,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                user_id,
                title,
                subject,
                topic,
                course,
                description,
                file_path,
                "pending"
            )
        )

        connection.commit()

        return {
            "success": True,
            "resource_id": cursor.lastrowid,
            "message": "Resource submitted for moderation."
        }

    except sqlite3.Error as error:
        return {
            "success": False,
            "message": str(error)
        }

    finally:
        connection.close()


def get_resources_by_user(user_id):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                id,
                title,
                subject,
                topic,
                course,
                description,
                file_path,
                status,
                created_at
            FROM notes
            WHERE user_id = ?
            ORDER BY created_at DESC
            """,
            (user_id,)
        )

        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()

        return [
            dict(zip(columns, row))
            for row in rows
        ]

    except sqlite3.Error as error:
        print("Error retrieving resources:", error)
        return []
    
    finally:
        connection.close()
        
def save_note_evaluation(
    note_id,
    accuracy_score=None,
    assessment_label=None,
    evaluation_summary=None,
    supported_information=None,
    insufficiently_supported_information=None,
    reference_materials=None
):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO note_evaluations (
                note_id,
                accuracy_score,
                assessment_label,
                evaluation_summary,
                supported_information,
                insufficiently_supported_information,
                reference_materials
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                note_id,
                accuracy_score,
                assessment_label,
                evaluation_summary,
                supported_information,
                insufficiently_supported_information,
                reference_materials
            )
        )

        connection.commit()

        return {
            "success": True,
            "evaluation_id": cursor.lastrowid,
            "message": "Note evaluation saved successfully."
        }

    except sqlite3.Error as error:
        return {
            "success": False,
            "message": str(error)
        }

    finally:
        connection.close()
        
def get_note_evaluations(note_id):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                id,
                note_id,
                accuracy_score,
                assessment_label,
                evaluation_summary,
                supported_information,
                insufficiently_supported_information,
                reference_materials,
                evaluated_at
            FROM note_evaluations
            WHERE note_id = ?
            ORDER BY evaluated_at DESC, id DESC
            """,
            (note_id,)
        )

        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()

        return [
            dict(zip(columns, row))
            for row in rows
        ]

    except sqlite3.Error as error:
        print("Error retrieving note evaluations:", error)
        return []

    finally:
        connection.close()
    
def moderate_resource(note_id, admin_id, decision, remarks=None):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        # Validate moderation decision
        if decision not in ("approved", "rejected"):
            return {
                "success": False,
                "message": "Invalid moderation decision."
            }

        # Verify that the user is an admin
        cursor.execute(
            "SELECT role FROM users WHERE id = ?",
            (admin_id,)
        )

        admin = cursor.fetchone()

        if admin is None or admin[0] != "admin":
            return {
                "success": False,
                "message": "Only administrators can moderate resources."
            }

        # Check whether the note exists
        cursor.execute(
            "SELECT id FROM notes WHERE id = ?",
            (note_id,)
        )

        if cursor.fetchone() is None:
            return {
                "success": False,
                "message": "Resource not found."
            }

        # Update the note status
        cursor.execute(
            """
            UPDATE notes
            SET status = ?
            WHERE id = ?
            """,
            (decision, note_id)
        )

        # Save moderation history
        cursor.execute(
            """
            INSERT INTO moderation_records (
                note_id,
                admin_id,
                decision,
                remarks
            )
            VALUES (?, ?, ?, ?)
            """,
            (note_id, admin_id, decision, remarks)
        )

        connection.commit()

        return {
            "success": True,
            "moderation_id": cursor.lastrowid,
            "message": "Resource moderated successfully."
        }

    except sqlite3.Error as error:
        connection.rollback()

        return {
            "success": False,
            "message": str(error)
        }
        
    finally:
        connection.close()

def get_moderation_history(note_id):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                moderation_records.id,
                moderation_records.note_id,
                moderation_records.admin_id,
                users.full_name AS admin_name,
                moderation_records.decision,
                moderation_records.remarks,
                moderation_records.moderated_at
            FROM moderation_records
            LEFT JOIN users
                ON moderation_records.admin_id = users.id
            WHERE moderation_records.note_id = ?
            ORDER BY moderation_records.moderated_at DESC,
                     moderation_records.id DESC
            """,
            (note_id,)
        )

        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()

        return [
            dict(zip(columns, row))
            for row in rows
        ]

    except sqlite3.Error as error:
        print("Error retrieving moderation history:", error)
        return []

    finally:
        connection.close()
        