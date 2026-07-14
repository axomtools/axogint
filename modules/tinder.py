from utils import retryrequest
import json
import sys

def check(email, timeout, session, verbose):
    url = 'https://api.gotinder.com/v2/auth/email'
    data = {'email': email}
    try:
        r = retryrequest('POST', url, session, timeout=timeout, data=data, verbose=verbose)
        res = r.json()
        exists = res.get('data', {}).get('exists', False)
    except Exception as e:
        exists = None
        if verbose:
            print(f'tinder error: {str(e)}', file=sys.stderr)
    return {'service': 'tinder', 'exists': exists, 'url': 'https://tinder.com'}
