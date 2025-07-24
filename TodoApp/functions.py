FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return a list of todos.
    """
    with open(filepath, 'r') as file:
        my_todos = file.readlines()

    return my_todos


def write_todos(my_todos: list[str], filepath=FILEPATH):
    """ Write a list of todos to a text file
    """
    with open(filepath, 'w') as file:
        file.writelines(my_todos)

print(__name__)
if __name__ == "__main__":
    print('Hello')
    print(get_todos())
