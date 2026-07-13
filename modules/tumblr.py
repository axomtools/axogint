import requests

def check(email, timeout):
    url = 'https://www.tumblr.com/svc/account/register'
    data = {'email': email}
    try:
        r = requests.post(url, data=data, timeout=timeout)
        res = r.json()
        exists = res.get('errors', {}).get('email', []) != []
    except:
        exists = None
    return {'service': 'tumblr', 'exists': exists, 'url': 'https://tumblr.com'}
