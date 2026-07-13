import requests

def check(email, timeout):
    url = 'https://vk.com/rest/method/auth.checkPhone'
    data = {'email': email}
    try:
        r = requests.post(url, data=data, timeout=timeout)
        res = r.json()
        exists = res.get('response', {}).get('exists', False)
    except:
        exists = None
    return {'service': 'vk', 'exists': exists, 'url': 'https://vk.com'}
