from utils import retryrequest
import json
import sys

def check(email, timeout, session, verbose):
    url = 'https://soundcloud.com/signup/email/check'
    data = {'email': email}
    try:
        r = retryrequest('POST', url, session, timeout=timeout, data=data, verbose=verbose)
        res = r.json()
        exists = res.get('status', '') == 'taken'
    except Exception as e:
        exists = None
        if verbose:
            print(f'soundcloud error: {str(e)}', file=sys.stderr)
    return {'service': 'soundcloud', 'exists': exists, 'url': 'https://soundcloud.com'}
