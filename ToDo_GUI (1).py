#!/usr/bin/env python
# coding: utf-8

# In[1]:


import FreeSimpleGUI as sg
import functions
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt','w') as file:
        pass

sg.theme('LightBrown')

# creating variables through functions as input in Window method
clock = sg.Text('',key='clock')
label = sg.Text("Type in a todo: ")
input_box = sg.InputText(tooltip="Enter todo",key="todo")
add_button = sg.Button('ADD',size=10 , mouseover_colors='LightGreen',key='ADD')

list_box = sg.Listbox(values = functions.get_todos(),
                      key="todos",
                      enable_events=True,
                      size=[45,10])

edit_button = sg.Button("EDIT",size=10, mouseover_colors='LightGreen')
complete_button = sg.Button("COMPLETE",size=10, mouseover_colors='LightGreen')
exit_button = sg.Button("EXIT",size=10, mouseover_colors='Red')

# this creates a window that encompasses everything
window = sg.Window("My todo APP" , 
                   layout=[[label,clock],
                           [input_box,add_button],
                           [list_box],
                           [complete_button,edit_button , exit_button]], # 1 list for 1 line
                   font=("Helvetica",20))  

while True:
    event , value = window.read(timeout=10)
    window['clock'].update(value=time.strftime("%b %d %Y %H:%M:%S"))
    
    match event:
        case "ADD":
            todos = functions.get_todos()
            new_todo = value["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value='')
            
        case "EDIT":
            try:
                todo_to_edit = value["todos"][0]
                new_todo = value["todo"]
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value='')
            except IndexError:
                sg.popup("Please select a todo first",font=("Helvetica",20))
            
        case "COMPLETE":
            try:
                todos_to_complete = value["todos"][0]
                todos = functions.get_todos()
                todos.remove(todos_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value='')
            except IndexError:
                sg.popup("Please select a todo first",font=("Helvetica",20))
            
        case "EXIT":
            break
            
        case "todos":
            window["todo"].update(value=value['todos'][0])
            
        case sg.WIN_CLOSED:
            break
        
window.close()


# In[ ]:





# In[ ]:




