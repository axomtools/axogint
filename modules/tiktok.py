import requests

def check(email, timeout):
    url = 'https://www.tiktok.com/api/v1/auth/email/exists/'
    data = {'email': email}
    try:
        r = requests.post(url, data=data, timeout=timeout)
        res = r.json()
        exists = res.get('data', {}).get('exists', False)
    except:
        exists = None
    return {'service': 'tiktok', 'exists': exists, 'url': 'https://tiktok.com'}
