import sys

import clipboard


def save_clipboard(filepath, text):
   with open(filepath, 'w') as f:
      f.write(text)


data = clipboard.paste()

if len(sys.argv) > 1:
    user_input = sys.argv[1]
    # print(f"new_content - {new_content}")
    # clipboard.copy(content)
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
