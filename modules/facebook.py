import requests

def check(email, timeout):
    url = 'https://www.facebook.com/login/identify/?ctx=recover&email=' + email
    try:
        r = requests.get(url, timeout=timeout)
        exists = 'account not found' not in r.text.lower()
    except:
        exists = None
    return {'service': 'facebook', 'exists': exists, 'url': 'https://facebook.com'}
