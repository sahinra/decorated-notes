import datetime

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
            print_ui_message(f"Invalid input: {user_input}. Please choose one of the following: {', '.join(valid_input)}")
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


def list_notes():
    print_ui_message("Retrieving notes for you.")
    notes = read_notes()
    print("".join(notes), "\n")


def add_note():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = input("Please type your note and hit Enter: ")
    note = f"{timestamp} {message}\n"
    with open(NOTE_FILE, "a") as note_file:
        note_file.writelines(note)
    print_ui_message("Note saved.")


def app():
    keep_going = True
    print_ui_message("Welcome to Decorated Notes!\nUser input is case-insensitive.")
    menu_elements = {"1": "Add new note", "2": "List saved notes", "Q": "Quit"}
    while keep_going:
        print_menu(menu_elements)
        user_input = let_user_select_menu("What would you like to do now? ", menu_elements)
        if user_input == "1":
            add_note()
        elif user_input == "2":
            list_notes()
        elif user_input == "Q":
            keep_going = False
    print_ui_message("Bye!")


if __name__ == '__main__':
    app()
