import requests

def check(email, timeout):
    url = 'https://api.gotinder.com/v2/auth/email'
    data = {'email': email}
    try:
        r = requests.post(url, data=data, timeout=timeout)
        res = r.json()
        exists = res.get('data', {}).get('exists', False)
    except:
        exists = None
    return {'service': 'tinder', 'exists': exists, 'url': 'https://tinder.com'}
