import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
while True:
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:].strip()

        # read the existing todos from the file
        with open('todos.txt', 'a+') as file:
            file.seek(0)
            todos = file.readlines()
        todos.append(todo.lower() + '\n')

        # append the new todos to the file
        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}. {item.title()}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[4:].strip())
            number = number - 1

            todos = functions.get_todos()

            new_todo = input('Enter a new todo item: ').strip()
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print('Your command is not valid. Please enter an integer that represents the task number you want to edit.')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[8:].strip())
            number = number - 1

            todos = functions.get_todos()

            todos.pop(number)
            functions.write_todos(todos)
        except IndexError:
            print('There is no task with that number.')
            continue
        except ValueError:
            print('Your command is not valid. Please enter an integer that represents the task number you want to complete.')

    elif user_action.startswith('exit'):
        break

    else:
        print('Command not valid.')

print('Bye!')