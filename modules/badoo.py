import requests

def check(email, timeout):
    url = 'https://badoo.com/api/v1/email/exists'
    data = {'email': email}
    try:
        r = requests.post(url, data=data, timeout=timeout)
        res = r.json()
        exists = res.get('exists', False)
    except:
        exists = None
    return {'service': 'badoo', 'exists': exists, 'url': 'https://badoo.com'}
