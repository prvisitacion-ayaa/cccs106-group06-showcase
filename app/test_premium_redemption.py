
from datetime import datetime

from app.database.database import get_connection
from app.backend.rewards import (
    award_learnpoints,
    get_learnpoints_balance,
    get_available_premium_features,
    redeem_premium_feature,
    get_redemption_history
)


connection = get_connection()
cursor = connection.cursor()

test_user_id = None
test_note_id = None
test_feature_ids = []

try:
    unique_id = datetime.now().strftime("%Y%m%d%H%M%S")

    # 1. Create a temporary student
    cursor.execute(
        """
        INSERT INTO users (
            username, email, password, full_name, role
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            f"premium_test_{unique_id}",
            f"premium_test_{unique_id}@example.com",
            "temporary_password",
            "Premium Test Student",
            "student"
        )
    )

    test_user_id = cursor.lastrowid

    # 2. Create an approved test note
    cursor.execute(
        """
        INSERT INTO notes (user_id, title, status)
        VALUES (?, ?, ?)
        """,
        (test_user_id, "Temporary Premium Test Note", "approved")
    )

    test_note_id = cursor.lastrowid

    # 3. Create temporary premium features
    features = [
        (f"Test Feature {unique_id}", "Available test feature", 30, 1),
        (f"Expensive Feature {unique_id}", "Insufficient balance test", 1000, 1),
        (f"Unavailable Feature {unique_id}", "Unavailable test feature", 10, 0)
    ]

    for feature in features:
        cursor.execute(
            """
            INSERT INTO premium_features (
                feature_name, description, points_required, is_available
            )
            VALUES (?, ?, ?, ?)
            """,
            feature
        )
        test_feature_ids.append(cursor.lastrowid)

    connection.commit()

    print("Temporary test records created.")

    # 4. Award 100 LearnPoints
    award_result = award_learnpoints(test_note_id, 100)
    print("\nAWARD RESULT:", award_result)

    assert award_result["success"] is True

    # 5. Check available premium features
    available_features = get_available_premium_features()
    print("\nAVAILABLE FEATURES:", available_features)

    assert any(
        feature["id"] == test_feature_ids[0]
        for feature in available_features
    )

    # 6. Test successful redemption (30 points)
    redemption_result = redeem_premium_feature(
        test_user_id,
        test_feature_ids[0]
    )

    print("\nREDEMPTION RESULT:", redemption_result)

    assert redemption_result["success"] is True
    assert redemption_result["points_used"] == 30
    assert redemption_result["remaining_balance"] == 70

    # 7. Verify remaining balance
    balance = get_learnpoints_balance(test_user_id)
    print("\nREMAINING BALANCE:", balance)

    assert balance == 70

    # 8. Test redemption history
    history = get_redemption_history(test_user_id)
    print("\nREDEMPTION HISTORY:", history)

    assert len(history) == 1
    assert history[0]["points_used"] == 30

    # 9. Test insufficient balance
    insufficient_result = redeem_premium_feature(
        test_user_id,
        test_feature_ids[1]
    )

    print("\nINSUFFICIENT BALANCE RESULT:", insufficient_result)

    assert insufficient_result["success"] is False
    assert insufficient_result["message"] == "Insufficient LearnPoints."

    # 10. Test unavailable feature
    unavailable_result = redeem_premium_feature(
        test_user_id,
        test_feature_ids[2]
    )

    print("\nUNAVAILABLE FEATURE RESULT:", unavailable_result)

    assert unavailable_result["success"] is False

    # 11. Verify balance was not changed by failed redemptions
    final_balance = get_learnpoints_balance(test_user_id)
    print("\nFINAL BALANCE:", final_balance)

    assert final_balance == 70

    print("\nALL PREMIUM REDEMPTION TESTS PASSED!")

finally:
    # 12. Clean up temporary records
    if test_user_id is not None:
        cursor.execute(
            "DELETE FROM premium_redemptions WHERE user_id = ?",
            (test_user_id,)
        )

        cursor.execute(
            "DELETE FROM learnpoints WHERE user_id = ?",
            (test_user_id,)
        )

    if test_note_id is not None:
        cursor.execute(
            "DELETE FROM notes WHERE id = ?",
            (test_note_id,)
        )

    for feature_id in test_feature_ids:
        cursor.execute(
            "DELETE FROM premium_features WHERE id = ?",
            (feature_id,)
        )

    if test_user_id is not None:
        cursor.execute(
            "DELETE FROM users WHERE id = ?",
            (test_user_id,)
        )

    connection.commit()
    connection.close()

    print("\nTemporary test records cleaned up.")
