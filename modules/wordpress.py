import requests

def check(email, timeout):
    url = 'https://public-api.wordpress.com/rest/v1.1/users/email/' + email + '/exists'
    try:
        r = requests.get(url, timeout=timeout)
        res = r.json()
        exists = res.get('exists', False)
    except:
        exists = None
    return {'service': 'wordpress', 'exists': exists, 'url': 'https://wordpress.com'}
