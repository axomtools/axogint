from utils import retryrequest
import json
import sys

def check(email, timeout, session, verbose):
    url = 'https://badoo.com/api/v1/email/exists'
    data = {'email': email}
    try:
        r = retryrequest('POST', url, session, timeout=timeout, data=data, verbose=verbose)
        res = r.json()
        exists = res.get('exists', False)
    except Exception as e:
        exists = None
        if verbose:
            print(f'badoo error: {str(e)}', file=sys.stderr)
    return {'service': 'badoo', 'exists': exists, 'url': 'https://badoo.com'}
