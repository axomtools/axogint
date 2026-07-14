from utils import retryrequest
import json
import sys

def check(email, timeout, session, verbose):
    url = 'https://www.etsy.com/api/v3/ajax/email/check'
    data = {'email': email}
    try:
        r = retryrequest('POST', url, session, timeout=timeout, data=data, verbose=verbose)
        res = r.json()
        exists = res.get('email_exists', False)
    except Exception as e:
        exists = None
        if verbose:
            print(f'etsy error: {str(e)}', file=sys.stderr)
    return {'service': 'etsy', 'exists': exists, 'url': 'https://etsy.com'}
