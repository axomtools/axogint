import requests

def check(email, timeout):
    url = 'https://soundcloud.com/signup/email/check'
    data = {'email': email}
    try:
        r = requests.post(url, data=data, timeout=timeout)
        res = r.json()
        exists = res.get('status', '') == 'taken'
    except:
        exists = None
    return {'service': 'soundcloud', 'exists': exists, 'url': 'https://soundcloud.com'}
