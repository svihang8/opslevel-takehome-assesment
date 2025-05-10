from todo_app import TodoApp

if __name__ == "__main__":
    app = TodoApp()
    app.run()

"""
Assign tags to each TodoItem
Printing out todoitems, chunk them out as work, personal
Add a new function
Every TodoItem will have only one tag.
{
id : 1, 
description : 'Task 1'
priority : 2,
tag : 'Work'
}
{
id : 2, 
description : 'Task 2'
priority : 1,
tag : 'Work'
}

{
id : 3, 
description : 'Task 3'
priority : 1,
tag : 'Personal'
}

tags {
'work' : [id1, id2]
'Personal' : [id3]
}
chunk it out and then sort it id : 1, id : 2


Mark a task as complete / incomplete(default).
1. is_complete : False / True
2. complete_task(id:int) -> O(1) 



"""