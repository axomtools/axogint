from utils import retryrequest
import json
import sys

def check(email, timeout, session, verbose):
    url = 'https://www.quora.com/api/v3/email/exists'
    data = {'email': email}
    try:
        r = retryrequest('POST', url, session, timeout=timeout, data=data, verbose=verbose)
        res = r.json()
        exists = res.get('exists', False)
    except Exception as e:
        exists = None
        if verbose:
            print(f'quora error: {str(e)}', file=sys.stderr)
    return {'service': 'quora', 'exists': exists, 'url': 'https://quora.com'}
