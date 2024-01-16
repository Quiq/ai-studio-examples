'''
This example calls the publicly available [icanhazdadjoke API](https://icanhazdadjoke.com/api).
It uses the last customer message to search for a joke nd returns the joke as a 
message (assumes customer assistant)
'''

def request_joke(context):
  joke_topic = context['derivedData']['lastCustomerMessage']

  return {
    "headers": {"Accept": "application/json"},
    "method": "GET",
    "params": {"term": joke_topic},
    "path": "/search"
  }

def handle_joke(response, context):
  joke = response['body']['results'][0]['joke']

  if joke:
    return {
      "actions": [
        {"action": "sendMessage", 'message': {'text': joke}}
      ]
    }
