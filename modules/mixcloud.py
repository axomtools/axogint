import requests

def check(email, timeout):
    url = 'https://www.mixcloud.com/register/'
    data = {'email': email}
    try:
        r = requests.post(url, data=data, timeout=timeout, allow_redirects=False)
        exists = r.status_code == 302
    except:
        exists = None
    return {'service': 'mixcloud', 'exists': exists, 'url': 'https://mixcloud.com'}
