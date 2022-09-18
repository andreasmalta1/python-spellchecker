import requests

api_key = "68bd384fb68541cfa6e6b2933042c119"
endpoint = "https://icemalta.cognitiveservices.azure.com/bing/v7.0/SpellCheck"

text_file = open('source.txt')
contents = text_file.read()
text_file.close()

data = {"text": contents}

params = {
    "mkt": "en-us",
    "mode": "proof"
}

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Ocp-Apim-Subscription-Key": api_key
}

response = requests.post(endpoint, headers=headers, params=params, data=data)
json_response = response.json()

for hit in json_response["flaggedTokens"]:
    print("Unknown word", hit["token"], end=". ")
    print("Suggestions", end=' ')
    for suggestion in hit["suggestions"]:
        print(suggestion["suggestion"], end=", ")
    print()

