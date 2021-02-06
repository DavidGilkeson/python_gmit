import requests

resp = requests.post('https://textbelt.com/text', {
  'phone': '55555555',
  'message': 'Hello world',
  'key': 'textbelt',
})
print(resp.json())