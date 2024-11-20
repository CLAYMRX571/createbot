import requests
from pprint import pprint as print

app_id = "362cdc02"
app_key = "803a1fd2b06175f953134d8c3ab7d81d"
language = "en-gb"

word_id = "python"
url = "https://od-api-sandbox.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()

r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
print(r.status_code)
res = r.json()
print(res)

# print(res['results'][0]['LexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])
# print(res['results'][0]['LexicalEntries'][0]['entries'][0]['pronunciations'][0]['audiofile'][0])
