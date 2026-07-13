import requests

def check(email, timeout):
    url = 'https://www.deviantart.com/api/v1/oauth2/email/check'
    params = {'email': email}
    try:
        r = requests.get(url, params=params, timeout=timeout)
        res = r.json()
        exists = res.get('status', '') == 'exists'
    except:
        exists = None
    return {'service': 'deviantart', 'exists': exists, 'url': 'https://deviantart.com'}
