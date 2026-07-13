import requests

def check(email, timeout):
    url = 'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/'
    headers = {'x-requested-with': 'XMLHttpRequest'}
    data = {'email': email}
    try:
        r = requests.post(url, headers=headers, data=data, timeout=timeout)
        res = r.json()
        exists = res.get('email_is_taken', False)
    except:
        exists = None
    return {'service': 'instagram', 'exists': exists, 'url': 'https://instagram.com'}
