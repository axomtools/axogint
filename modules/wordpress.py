from utils import retryrequest
import json
import sys

def check(email, timeout, session, verbose):
    url = 'https://public-api.wordpress.com/rest/v1.1/users/email/' + email + '/exists'
    try:
        r = retryrequest('GET', url, session, timeout=timeout, verbose=verbose)
        res = r.json()
        exists = res.get('exists', False)
    except Exception as e:
        exists = None
        if verbose:
            print(f'wordpress error: {str(e)}', file=sys.stderr)
    return {'service': 'wordpress', 'exists': exists, 'url': 'https://wordpress.com'}
