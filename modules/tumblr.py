from utils import retryrequest
import json
import sys

def check(email, timeout, session, verbose):
    url = 'https://www.tumblr.com/svc/account/register'
    data = {'email': email}
    try:
        r = retryrequest('POST', url, session, timeout=timeout, data=data, verbose=verbose)
        res = r.json()
        exists = res.get('errors', {}).get('email', []) != []
    except Exception as e:
        exists = None
        if verbose:
            print(f'tumblr error: {str(e)}', file=sys.stderr)
    return {'service': 'tumblr', 'exists': exists, 'url': 'https://tumblr.com'}
