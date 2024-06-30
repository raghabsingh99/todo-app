FILEPATH = "todo.txt"
def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write a to-do item in a text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("hellow")
    print(get_todos())
