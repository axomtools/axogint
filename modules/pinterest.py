import requests

def check(email, timeout):
    url = 'https://www.pinterest.com/resource/EmailExistsResource/get/'
    params = {'email': email}
    try:
        r = requests.get(url, params=params, timeout=timeout)
        data = r.json()
        exists = data.get('resource_response', {}).get('data', {}).get('exists', False)
    except:
        exists = None
    return {'service': 'pinterest', 'exists': exists, 'url': 'https://pinterest.com'}
