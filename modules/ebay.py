import requests

def check(email, timeout):
    url = 'https://www.ebay.com/signin/'
    data = {'email': email}
    try:
        r = requests.post(url, data=data, timeout=timeout, allow_redirects=False)
        exists = r.status_code == 302
    except:
        exists = None
    return {'service': 'ebay', 'exists': exists, 'url': 'https://ebay.com'}
