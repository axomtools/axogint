import requests

def check(email, timeout):
    url = 'https://medium.com/_/api/users/email/exists'
    data = {'email': email}
    try:
        r = requests.post(url, data=data, timeout=timeout)
        res = r.json()
        exists = res.get('exists', False)
    except:
        exists = None
    return {'service': 'medium', 'exists': exists, 'url': 'https://medium.com'}
