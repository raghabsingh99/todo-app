import functions
import time
now = time.strftime("%b %d, %Y %H: %M:%S")
print("now")
while True:
    user_action = input("Type add, show, edit, complete, or exit: ").strip()

    if user_action.startswith('add'):
        todo = user_action[4:].strip()

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action == 'show':

        todos = functions.get_todos('files/todos.txt')

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1} - {item}"
            row = row.title()
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:].strip()) - 1
            print(number)
            todos = functions.get_todos()

            new_todo = input("Enter new todo: ").strip()
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Invalid input for edit. Please enter a valid number.")
        except IndexError:
            print("Todo number out of range.")

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:].strip()) - 1
            todos = functions.get_todos()

            todo_to_remove = todos[number].strip('\n')
            todos.pop(number)

            functions.write_todos(todos)

            message = f"Todo '{todo_to_remove}' was removed from the list."
            print(message)
        except ValueError:
            print("Invalid input for complete. Please enter a valid number.")
        except IndexError:
            print("Todo number out of range.")

    elif user_action == 'exit':
        break

print("Bye!")
