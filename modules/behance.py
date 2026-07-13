import requests

def check(email, timeout):
    url = 'https://www.behance.net/v2/users/email/' + email
    try:
        r = requests.get(url, timeout=timeout)
        exists = r.status_code == 200
    except:
        exists = None
    return {'service': 'behance', 'exists': exists, 'url': 'https://behance.net'}
