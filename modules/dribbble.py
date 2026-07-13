import requests

def check(email, timeout):
    url = 'https://dribbble.com/session'
    data = {'user[email]': email}
    try:
        r = requests.post(url, data=data, timeout=timeout, allow_redirects=False)
        exists = r.status_code == 302
    except:
        exists = None
    return {'service': 'dribbble', 'exists': exists, 'url': 'https://dribbble.com'}
