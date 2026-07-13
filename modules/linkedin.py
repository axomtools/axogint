import requests

def check(email, timeout):
    url = 'https://www.linkedin.com/checkpoint/lg/login-submit'
    data = {'email': email, 'session_key': email}
    try:
        r = requests.post(url, data=data, timeout=timeout, allow_redirects=False)
        exists = r.status_code == 302 and 'login' not in r.headers.get('location', '')
    except:
        exists = None
    return {'service': 'linkedin', 'exists': exists, 'url': 'https://linkedin.com'}
