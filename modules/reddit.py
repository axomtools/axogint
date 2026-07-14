from utils import retryrequest
import json

def check(email, timeout):
    url = 'https://www.reddit.com/api/username_available.json?user=' + email.split('@')[0]
    try:
        r = retryrequest('GET', url, timeout=timeout)
        data = r.json()
        exists = not data
    except:
        exists = None
    return {'service': 'reddit', 'exists': exists, 'url': 'https://reddit.com'}
