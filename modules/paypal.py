from utils import retryrequest

def check(email, timeout):
    url = 'https://www.paypal.com/signin/'
    data = {'login_email': email}
    try:
        r = retryrequest('POST', url, timeout=timeout, data=data, allow_redirects=False)
        exists = 'email' in r.text.lower()
    except:
        exists = None
    return {'service': 'paypal', 'exists': exists, 'url': 'https://paypal.com'}
