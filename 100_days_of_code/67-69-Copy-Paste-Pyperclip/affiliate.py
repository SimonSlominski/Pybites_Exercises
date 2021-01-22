import pyperclip

AFFILIATE_CODE = "&tag=baymax"

url = pyperclip.paste()

if 'amazon' not in url:
    print("Invalid link")
else:
    new_link = url + AFFILIATE_CODE
    pyperclip.copy(new_link)
    print("Affiliate link generated and copied to clipboard")

# To run the script copy random link and check the results
# https://www.amazon.de&tag=baymax