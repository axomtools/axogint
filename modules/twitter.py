import requests

def check(email, timeout):
    url = 'https://api.twitter.com/i/users/email_available.json?email=' + email
    try:
        r = requests.get(url, timeout=timeout)
        data = r.json()
        exists = not data.get('valid', True)
    except:
        exists = None
    return {'service': 'twitter', 'exists': exists, 'url': 'https://twitter.com'}
