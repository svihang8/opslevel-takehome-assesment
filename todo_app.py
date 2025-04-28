from todo_item import TodoItem

class TodoApp:
    def __init__(self):
        self.items:list[TodoItem] = []
        self.counter = 1

    def add_item(self, description:str, priority:int):
        try:
            if priority <= 0:
                raise Exception("Invalid priority value.")
            item = TodoItem(self.counter, description, priority)
            self.items.append(item)
            self.counter += 1
        except Exception as e:
            print(e)
    
    def delete_item(self, id:int):
        try:
            items_length = len(self.items)
            self.items = [item for item in self.items if item.id != id]
            if items_length == len(self.items):
                raise Exception(f"Item with id {id} not found")
        except Exception as e:
            print(e)
    
    def get_items(self):
        try:
            for item in sorted(self.items, key = lambda x : (x.priority, x.id)):
                print(f"{item}")
            print()
        except Exception as e:
            print(e)

    def get_missing_priorities(self):
        if not self.items:
            print(f"No missing priorities")
            return
        existing_priorities = sorted(set(item.priority for item in self.items))
        missing_priorities = []
        for priority in range(1, existing_priorities[-1]):
            if priority not in existing_priorities:
                missing_priorities.append(str(priority))
        if len(missing_priorities) == 0:
            print(f"No missing priorities")
        else:
            print("Missing priorities:", ','.join(missing_priorities))
    
    def run(self):
        def list_options():
            print("1. Add Item")
            print("2. Delete Item")
            print("3. List Items")
            print("4. List Missing Priorities")
            print("5. Exit")
            return
        print("Welcome to the Todo App.")
        while True:
            list_options()
            choice = input("Choose an option: ").strip()
            if choice == '1':
                description = input("Enter description: ").strip()
                try:
                    priority = int(input("Enter priority (positive integer): ").strip())
                    if priority <= 0:
                        print("Priority must be a positive integer.")
                        continue
                    self.add_item(description, priority)
                except ValueError:
                    print("Invalid priority. Please enter a number.")
            elif choice == '2':
                try:
                    id_to_delete = int(input("Enter ID to delete: ").strip())
                    self.delete_item(id_to_delete)
                except ValueError:
                    print("Invalid ID. Please enter a number.\n")
            elif choice == '3':
                self.get_items()
            elif choice == '4':
                self.get_missing_priorities()
            elif choice == '5':
                print("Thank you for using Todo App.")
                break
            else:
                print("Invalid choice")