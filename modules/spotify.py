from utils import retryrequest
import json
import sys

def check(email, timeout, session, verbose):
    url = 'https://www.spotify.com/api/signup/validate'
    data = {'email': email}
    try:
        r = retryrequest('POST', url, session, timeout=timeout, data=data, verbose=verbose)
        res = r.json()
        exists = res.get('status') == 1
    except Exception as e:
        exists = None
        if verbose:
            print(f'spotify error: {str(e)}', file=sys.stderr)
    return {'service': 'spotify', 'exists': exists, 'url': 'https://spotify.com'}
