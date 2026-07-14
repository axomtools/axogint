from utils import retryrequest
import json
import sys

def check(email, timeout, session, verbose):
    url = 'https://identity.flickr.com/checkusername'
    data = {'email': email}
    try:
        r = retryrequest('POST', url, session, timeout=timeout, data=data, verbose=verbose)
        res = r.json()
        exists = res.get('code') == 3
    except Exception as e:
        exists = None
        if verbose:
            print(f'flickr error: {str(e)}', file=sys.stderr)
    return {'service': 'flickr', 'exists': exists, 'url': 'https://flickr.com'}
