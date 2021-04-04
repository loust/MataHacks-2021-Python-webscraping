from bs4 import BeautifulSoup as bs
import re

with open('linuxquestions.html', 'r') as f:
    data = f.read()

reader = bs(data, features="html.parser")

print(reader.title) # Get the title

print(reader.find('div', attrs={"id": "post_message"})) # This will not work, since the post IDs are as follows: post_message_######

# So, we do it with regex:

print(reader.find_all("div", attrs={"id": re.compile('(post_message_[0-9]+)')})) # This will work, but it saves it in a single list, and grabs everything.

# Ultimately, you will need to parse everything and clean it up.
# If there are any formatting issues, you can use UTF-8 encoding: encoding='utf-8'
