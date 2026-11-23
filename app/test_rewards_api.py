
from datetime import datetime

from app.database.database import get_connection
from app.backend.rewards import (
    get_learnpoints_balance,
    award_learnpoints
)


connection = get_connection()
cursor = connection.cursor()

test_user_id = None
test_note_id = None

try:
    # Create a temporary test student
    unique_id = datetime.now().strftime("%Y%m%d%H%M%S")

    cursor.execute(
        """
        INSERT INTO users (
            username, email, password, full_name, role
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            f"test_rewards_{unique_id}",
            f"test_rewards_{unique_id}@example.com",
            "temporary_password",
            "Temporary Rewards Tester",
            "student"
        )
    )

    test_user_id = cursor.lastrowid

    # Create an approved test note
    cursor.execute(
        """
        INSERT INTO notes (user_id, title, status)
        VALUES (?, ?, ?)
        """,
        (test_user_id, "Temporary Rewards Test Note", "approved")
    )

    test_note_id = cursor.lastrowid
    connection.commit()

    print("Temporary test account and note created.")

    # Test awarding 50 LearnPoints
    result = award_learnpoints(test_note_id, 50)
    print("\nAWARD RESULT:", result)

    # Check the student's balance
    balance = get_learnpoints_balance(test_user_id)
    print("BALANCE:", balance)

    # Try awarding points to the same note again
    duplicate_result = award_learnpoints(test_note_id, 50)
    print("\nDUPLICATE AWARD RESULT:", duplicate_result)

    # Verify expected results
    assert result["success"] is True
    assert balance == 50
    assert duplicate_result["success"] is False

    print("\nALL REWARDS API TESTS PASSED!")

finally:
    # Remove temporary test records
    if test_note_id is not None:
        cursor.execute(
            "DELETE FROM learnpoints WHERE source_note_id = ?",
            (test_note_id,)
        )

    if test_user_id is not None:
        cursor.execute(
            "DELETE FROM learnpoints WHERE user_id = ?",
            (test_user_id,)
        )

        cursor.execute(
            "DELETE FROM notes WHERE id = ?",
            (test_note_id,)
        )

        cursor.execute(
            "DELETE FROM users WHERE id = ?",
            (test_user_id,)
        )

    connection.commit()
    connection.close()

    print("\nTemporary test records cleaned up.")
