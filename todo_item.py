class TodoItem:
    def __init__(self, id:int, description:str, priority:int):
        self.id = id
        self.description = description
        self.priority = priority
    
    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return f"ID: {self.id} | Priority: {self.priority} | {self.description}"
    
