import requests

def check(email, timeout):
    url = 'https://accounts.snapchat.com/accounts/email_exists'
    data = {'email': email}
    try:
        r = requests.post(url, data=data, timeout=timeout)
        res = r.json()
        exists = res.get('exists', False)
    except:
        exists = None
    return {'service': 'snapchat', 'exists': exists, 'url': 'https://snapchat.com'}
