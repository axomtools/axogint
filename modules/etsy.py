import requests

def check(email, timeout):
    url = 'https://www.etsy.com/api/v3/ajax/email/check'
    data = {'email': email}
    try:
        r = requests.post(url, data=data, timeout=timeout)
        res = r.json()
        exists = res.get('email_exists', False)
    except:
        exists = None
    return {'service': 'etsy', 'exists': exists, 'url': 'https://etsy.com'}
