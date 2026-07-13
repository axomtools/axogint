import requests

def check(email, timeout):
    url = 'https://mail.google.com/mail/gxlu?email=' + email
    try:
        r = requests.get(url, timeout=timeout)
        exists = 'Success' in r.text
    except:
        exists = None
    return {'service': 'google', 'exists': exists, 'url': 'https://mail.google.com'}
