import functions
import FreeSimpleGUI as sg
import time
import os

# create a todos.txt file if one does not exist
if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

# apply a theme
sg.theme("Black")

# create a label to show current date and time
clock = sg.Text('', key="clock")

# create the required labels and text boxes
label = sg.Text("Enter a todo")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add")

# Add an 'edit' feature for the todos
list_box = sg.Listbox(values=functions.get_todos(),
                      key="todos",
                      enable_events=True,
                      size=(45,10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

# create the window object
window = sg.Window("My Todo App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read(timeout=500)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            new_todo = values["todo"].strip() + "\n"
            todos = functions.get_todos()
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"].strip() + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Select an item to edit.", font=("Helvetica", 20))

        case "Complete":
            try:
                todo_to_complete = values["todos"][0].strip() + "\n"
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value='')
            except IndexError:
                sg.popup("Select an item to complete.", font=("Helvetica", 20))

        case "Exit":
            break

        case "todos":
            # when clicking on an edit in the list box , that item appears in the input text box waiting to be edited
            window["todo"].update(value=values["todos"][0])

        case sg.WINDOW_CLOSED:
            break

window.close()


