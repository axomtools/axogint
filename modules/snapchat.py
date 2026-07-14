from utils import retryrequest
import json
import sys

def check(email, timeout, session, verbose):
    url = 'https://accounts.snapchat.com/accounts/email_exists'
    data = {'email': email}
    try:
        r = retryrequest('POST', url, session, timeout=timeout, data=data, verbose=verbose)
        res = r.json()
        exists = res.get('exists', False)
    except Exception as e:
        exists = None
        if verbose:
            print(f'snapchat error: {str(e)}', file=sys.stderr)
    return {'service': 'snapchat', 'exists': exists, 'url': 'https://snapchat.com'}
