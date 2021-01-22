import pyperclip

def paste_from_clipboard():
    text = pyperclip.paste()
    return text

def replace_text(old_text):
    target = input('What would you like to replace?')
    replacement = input("And what you would like to replace")
    new_text = old_text.replace(target, replacement)
    return new_text

def copy_to_clipboard(new_text):
    pyperclip.copy(new_text)
    print("The new sting is now copied to the clipboard.")

if __name__ == "__main__":
    old_text = paste_from_clipboard()
    new_text = replace_text(old_text)
    copy_to_clipboard(new_text)