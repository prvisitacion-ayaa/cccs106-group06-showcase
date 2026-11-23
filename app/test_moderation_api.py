
from app.database.database import get_connection
from app.backend.resources import moderate_resource, get_moderation_history
import uuid


admin_id = None
note_id = None
original_status = None

try:
    # Find a pending note for testing
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, status
        FROM notes
        WHERE status = 'pending'
        ORDER BY id
        LIMIT 1
    """)

    note = cursor.fetchone()

    if note is None:
        raise Exception("No pending note available for testing.")

    note_id = note[0]
    original_status = note[1]

    # Create a temporary admin account
    unique_id = uuid.uuid4().hex[:8]

    cursor.execute("""
        INSERT INTO users (
            username,
            email,
            password,
            full_name,
            role
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        f"temp_admin_{unique_id}",
        f"temp_admin_{unique_id}@test.local",
        "temporary_test_password",
        "Temporary Admin Test",
        "admin"
    ))

    admin_id = cursor.lastrowid
    connection.commit()
    connection.close()

    print("Temporary admin created.")
    print("Testing note ID:", note_id)

    # Test approval and rejection
    for decision in ("approved", "rejected"):

        result = moderate_resource(
            note_id,
            admin_id,
            decision,
            "Temporary moderation API test"
        )

        print(f"\n{decision.upper()} result:", result)

        if not result["success"]:
            raise Exception(result["message"])

        # Verify the note's updated status
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT status FROM notes WHERE id = ?",
            (note_id,)
        )

        current_status = cursor.fetchone()[0]
        connection.close()

        if current_status != decision:
            raise Exception(f"Expected status {decision}, got {current_status}")

        # Verify moderation history
        history = get_moderation_history(note_id)

        matching_record = any(
            record["admin_id"] == admin_id
            and record["decision"] == decision
            for record in history
        )

        if not matching_record:
            raise Exception(f"{decision} history was not saved.")

        print(f"PASS: {decision} and history verified.")

    print("\nALL MODERATION TESTS PASSED!")

finally:
    # Remove test records and restore the original note status
    if admin_id is not None:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM moderation_records WHERE admin_id = ?",
            (admin_id,)
        )

        if note_id is not None and original_status is not None:
            cursor.execute(
                "UPDATE notes SET status = ? WHERE id = ?",
                (original_status, note_id)
            )

        cursor.execute(
            "DELETE FROM users WHERE id = ?",
            (admin_id,)
        )

        connection.commit()
        connection.close()

        print("\nTemporary admin and test records cleaned up.")

    elif note_id is not None and original_status is not None:
        connection = get_connection()
        connection.execute(
            "UPDATE notes SET status = ? WHERE id = ?",
            (original_status, note_id)
        )
        connection.commit()
        connection.close()
