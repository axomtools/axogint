import requests

def check(email, timeout):
    url = 'https://www.patreon.com/api/auth/check_email'
    data = {'email': email}
    try:
        r = requests.post(url, data=data, timeout=timeout)
        res = r.json()
        exists = res.get('email_taken', False)
    except:
        exists = None
    return {'service': 'patreon', 'exists': exists, 'url': 'https://patreon.com'}
