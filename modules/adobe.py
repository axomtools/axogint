from utils import retryrequest
import json
import sys

def check(email, timeout, session, verbose):
    url = 'https://auth.services.adobe.com/signup/v2/users/email/' + email
    try:
        r = retryrequest('GET', url, session, timeout=timeout, verbose=verbose)
        res = r.json()
        exists = res.get('emailExists', False)
    except Exception as e:
        exists = None
        if verbose:
            print(f'adobe error: {str(e)}', file=sys.stderr)
    return {'service': 'adobe', 'exists': exists, 'url': 'https://adobe.com'}
