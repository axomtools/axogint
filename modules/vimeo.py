import requests

def check(email, timeout):
    url = 'https://vimeo.com/api/v2/users/email/' + email
    try:
        r = requests.get(url, timeout=timeout)
        exists = r.status_code == 200
    except:
        exists = None
    return {'service': 'vimeo', 'exists': exists, 'url': 'https://vimeo.com'}
