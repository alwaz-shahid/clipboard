import json
import sys
import clipboard


def save_clipboard(filepath, text):
    with open(filepath, 'w') as f:
        json.dump(text, f)


def load_clipboard(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)


save_clipboard("data.json", {'key': 'value'})

data = clipboard.paste()

if len(sys.argv) > 1:
    user_input = sys.argv[1]
    if user_input == "--help":
        print("""
        Usage:
        myClipboard.py [content] \n
        commands: \n "--save" - save input"
        \n "--get" - get t clipboard
        """)
    elif user_input == "--save":
        print("Saving content to clipboard")

    elif user_input == "--get":
        print("Getting content from clipboard")
    elif user_input == "--show":
        print("Showing content from clipboard")

    else:
        print("Unknown command, use --help for help")
else:
    print("No content to save, please provide content or use --help")
# clipboard.copy(data)

# print(sys.argv)
