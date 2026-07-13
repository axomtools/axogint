import requests

def check(email, timeout):
    url = 'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&email=' + email
    try:
        r = requests.get(url, timeout=timeout)
        exists = 'invalid email' not in r.text.lower()
    except:
        exists = None
    return {'service': 'microsoft', 'exists': exists, 'url': 'https://outlook.com'}
