import requests

def check(email, timeout):
    url = 'https://identity.flickr.com/checkusername'
    data = {'email': email}
    try:
        r = requests.post(url, data=data, timeout=timeout)
        res = r.json()
        exists = res.get('code') == 3
    except:
        exists = None
    return {'service': 'flickr', 'exists': exists, 'url': 'https://flickr.com'}
