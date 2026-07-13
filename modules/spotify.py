import requests

def check(email, timeout):
    url = 'https://www.spotify.com/api/signup/validate'
    data = {'email': email}
    try:
        r = requests.post(url, data=data, timeout=timeout)
        res = r.json()
        exists = res.get('status') == 1
    except:
        exists = None
    return {'service': 'spotify', 'exists': exists, 'url': 'https://spotify.com'}
