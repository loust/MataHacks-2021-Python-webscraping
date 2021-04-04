import requests

URL = "https://www.linuxquestions.org/questions/slackware-14/what%27s-your-favorite-sql-editor-842171/"

data = requests.get(URL).text

print(data)
