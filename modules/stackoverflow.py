import requests

def check(email, timeout):
    url = 'https://stackoverflow.com/users/account-recovery'
    data = {'email': email}
    try:
        r = requests.post(url, data=data, timeout=timeout, allow_redirects=False)
        exists = r.status_code == 302
    except:
        exists = None
    return {'service': 'stackoverflow', 'exists': exists, 'url': 'https://stackoverflow.com'}
