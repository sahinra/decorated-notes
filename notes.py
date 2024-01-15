import datetime
import time

NOTE_FILE = "notes.txt"


def print_ui_message(message):
    print(f"\n> {message}\n")


def print_menu(menu_dict):
    for key, value in menu_dict.items():
        print(f"{key}: {value}")


def let_user_select_menu(message, menu_elements):
    valid_input = menu_elements.keys()
    is_input_valid = False
    while not is_input_valid:
        user_input = input(message).upper()
        if user_input not in valid_input:
            print_ui_message(
                f"Invalid input: {user_input}. Please choose one of the following: {', '.join(valid_input)}")
        else:
            is_input_valid = True
    return user_input


def read_notes():
    try:
        with open(NOTE_FILE, "r") as note_file:
            notes = note_file.readlines()
        return notes
    except FileNotFoundError:
        with open(NOTE_FILE, "w"):
            pass
        return []


# Write a decorator function to measure the execution time of a function.
def exec_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"{func.__name__} took {end - start}ms")

    return wrapper


# Write a decorator to add logging functionality to a function.
def log_function(func):
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{func.__name__} called at {timestamp} with {args} {kwargs}")
        res = func(*args, **kwargs)
        print(f"{func.__name__} completed at {timestamp}")
        return res

    return wrapper


def handle_exception(func):
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return res
        except Exception as ex:
            return "Exception caught"

    return wrapper


@log_function
@exec_time
def list_notes():
    print_ui_message("Retrieving notes for you.")
    notes = read_notes()
    print("".join(notes), "\n")


@log_function
@exec_time
def add_note():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = input("Please type your note and hit Enter: ")
    note = f"{timestamp} {message}\n"
    with open(NOTE_FILE, "a") as note_file:
        note_file.writelines(note)
    print_ui_message("Note saved.")


def edit_note():
    list_notes()
    notes = read_notes()
    if not notes:
        print("No notes available")
        return
    try:
        index = int(input("Enter the index of the note you want to edit"))
        if index in range(len(notes)):
            edited_note = input("Edit your note")
            notes[index] = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%Sf')} {edited_note}"
            with open(NOTE_FILE, "w") as note_file:
                note_file.writelines(notes)
            print("Note edited")
    except ValueError:
        print("Invalid input")


def delete_note():
    list_notes()
    notes = read_notes()
    if not notes:
        print("No notes available")
        return
    try:
        index = int(input("Enter the index of the note you want to delete"))
        if index in range(len(notes)):
            del notes[index]
            with open(NOTE_FILE, "w") as note_file:
                note_file.writelines(notes)
            print("Note deleted")
    except ValueError:
        print("Invalid input")


def app():
    keep_going = True
    print_ui_message("Welcome to Decorated Notes!\nUser input is case-insensitive.")
    menu_elements = {"1": "Add new note", "2": "List saved notes", "3": "Edit a note", "4": "Delete a note", "Q": "Quit"}
    while keep_going:
        print_menu(menu_elements)
        user_input = let_user_select_menu("What would you like to do now? ", menu_elements)
        if user_input == "1":
            add_note()
        elif user_input == "2":
            list_notes()
        elif user_input == "3":
            edit_note()
        elif user_input == "4":
            delete_note()
        elif user_input == "Q":
            keep_going = False
    print_ui_message("Bye!")


if __name__ == '__main__':
    app()
