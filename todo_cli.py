#!/usr/bin/env python
# coding: utf-8

# In[1]:


from functions import get_todos,write_todos
import time

now = time.strftime( "%b %d , %Y %H:%M:%S")
print("It is" , now)

while True:
    user_action = input("Type add , show , edit , complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = get_todos()

        todos.append(todo)

        write_todos(todos)
        
    elif user_action.startswith("show"):

        todos = get_todos("todo.txt")

        for index , item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + "\n"

            write_todos(todos)
                
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            num = int(user_action[9:])

            todos = get_todos()

            todos.pop(num-1)

            write_todos(todos)
                
        except (IndexError , ValueError):
            print("No item with that index")
            continue


    elif user_action.startswith("exit"):
        break  
        
    else:
        print("Invalid Input")

print("Bye")                          


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




