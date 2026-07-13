import requests

def check(email, timeout):
    url = 'https://www.youtube.com/email_ajax?email=' + email
    try:
        r = requests.get(url, timeout=timeout)
        data = r.json()
        exists = data.get('status', '') == 'TAKEN'
    except:
        exists = None
    return {'service': 'youtube', 'exists': exists, 'url': 'https://youtube.com'}
