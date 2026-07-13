import requests

def check(email, timeout):
    url = 'https://www.quora.com/api/v3/email/exists'
    data = {'email': email}
    try:
        r = requests.post(url, data=data, timeout=timeout)
        res = r.json()
        exists = res.get('exists', False)
    except:
        exists = None
    return {'service': 'quora', 'exists': exists, 'url': 'https://quora.com'}
