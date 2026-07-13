import requests

def check(email, timeout):
    url = 'https://github.com/login?email=' + email
    try:
        r = requests.get(url, timeout=timeout)
        exists = 'This account has been' not in r.text
    except:
        exists = None
    return {'service': 'github', 'exists': exists, 'url': 'https://github.com'}
