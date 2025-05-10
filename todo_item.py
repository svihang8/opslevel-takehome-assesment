class TodoItem:
    def __init__(self, id:int, description:str, priority:int, is_complete:bool):
        self.id = id
        self.description = description
        self.priority = priority
        self.is_complete = is_complete
    
    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        complete_string = "(C)" if self.is_complete else "(NC)"
        return f"ID: {self.id} | Priority: {self.priority} | {self.description} | {complete_string}"
    
