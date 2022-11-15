import requests

url = "http://127.0.0.1:25000/perform_query"

payload={
  'cmd1': 'filter',
  'value1': 'GET',
  'cmd2': 'map',
  'value2': '0'
}

response = requests.request("POST", url, data=payload)
print(response.text)