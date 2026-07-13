import requests

def check(email, timeout):
    url = 'https://auth.services.adobe.com/signup/v2/users/email/' + email
    try:
        r = requests.get(url, timeout=timeout)
        res = r.json()
        exists = res.get('emailExists', False)
    except:
        exists = None
    return {'service': 'adobe', 'exists': exists, 'url': 'https://adobe.com'}
