from todo_app import TodoApp

def run_tests():
    app = TodoApp()

    print("\n=== Test 1: Add valid items ===")
    app.add_item("Task 1", 1)
    app.add_item("Task 2", 3)
    app.add_item("Task 3", 5)
    app.get_items()

    print("\n=== Test 2: Add items with duplicate priorities ===")
    app.add_item("Duplicate Priority 5", 5)
    app.get_items()

    print("\n=== Test 3: Add item with invalid priority (0) ===")
    try:
        app.add_item("Invalid Priority 0", 0)
    except Exception as e:
        print(f"Error: {e}")

    print("\n=== Test 4: Add item with negative priority ===")
    try:
        app.add_item("Negative Priority", -2)
    except Exception as e:
        print(f"Error: {e}")

    print("\n=== Test 5: Missing priorities after adding ===")
    app.get_missing_priorities()

    print("\n=== Test 6: Delete existing item ===")
    app.delete_item(2)  # Should delete "Task 2"
    app.get_items()

    print("\n=== Test 7: Delete non-existent item ===")
    app.delete_item(100)  # Should raise not found

    print("\n=== Test 8: Delete twice same ID ===")
    app.delete_item(2)  # Already deleted, should not crash

    print("\n=== Test 9: Missing priorities after deletion ===")
    app.get_missing_priorities()

    print("\n=== Test 10: Deleting all and checking list empty ===")
    app.delete_item(1)
    app.delete_item(3)
    app.delete_item(4)
    app.get_items()

    print("\n=== Test 11: Missing priorities when no items ===")
    app.get_missing_priorities()

if __name__ == "__main__":
    run_tests()
