from utils import retryrequest
import json
import sys

def check(email, timeout, session, verbose):
    url = 'https://www.patreon.com/api/auth/check_email'
    data = {'email': email}
    try:
        r = retryrequest('POST', url, session, timeout=timeout, data=data, verbose=verbose)
        res = r.json()
        exists = res.get('email_taken', False)
    except Exception as e:
        exists = None
        if verbose:
            print(f'patreon error: {str(e)}', file=sys.stderr)
    return {'service': 'patreon', 'exists': exists, 'url': 'https://patreon.com'}
