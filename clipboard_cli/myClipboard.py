import json
import sys
import clipboard

saved_data = "clipboard.json"


def save_clipboard(filepath, text):
    with open(filepath, 'w') as f:
        json.dump(text, f)


def load_clipboard(filepath):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except:
        return {}


if len(sys.argv) > 1:
    user_input = sys.argv[1]
    data = load_clipboard(saved_data)

    if user_input == "--help":
        print("""
        Usage: myClipboard.py [content] \n
        commands: --------- \n "--save" - save input"
        \n "--get" - get t clipboard
        """)
    elif user_input == "--save":
        print("Your last clipboard data will be saved under clipboard.json, with a key name of your input")
        key = input("Enter key: ")
        data[key] = clipboard.paste()
        save_clipboard(saved_data, data)
        print("Saving content to clipboard")

    elif user_input == "--get":
        key = input("Enter key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Getting content from clipboard")
            print(data[key])
        else:
            print("Key not found")
    elif user_input == "--show":
        print("Showing all content from clipboard")
        print(data)

    else:
        print("Unknown command, use --help for help")
else:
    print("No content to save, please provide content or use --help")
# clipboard.copy(data)

# print(sys.argv)
