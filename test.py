import requests
import webbrowser

base = 'https://kauth.kakao.com/oauth/'
client_id = "e5b12f42b7066ec48166ae8e72c46af3"
redirect_uri = "https://localhost/oauth"
payload = {'client_id': client_id, 'redirect_uri': redirect_uri, 'response_type': 'code'}
r = requests.get(base+"authorize", params=payload)
webbrowser.open(r.url, new=0, autoraise=True)
webbrowser.open_new(r.url)
webbrowser.open_new_tab(r.url)