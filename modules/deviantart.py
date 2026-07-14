from utils import retryrequest
import json
import sys

def check(email, timeout, session, verbose):
    url = 'https://www.deviantart.com/api/v1/oauth2/email/check'
    params = {'email': email}
    try:
        r = retryrequest('GET', url, session, timeout=timeout, params=params, verbose=verbose)
        res = r.json()
        exists = res.get('status', '') == 'exists'
    except Exception as e:
        exists = None
        if verbose:
            print(f'deviantart error: {str(e)}', file=sys.stderr)
    return {'service': 'deviantart', 'exists': exists, 'url': 'https://deviantart.com'}
