from utils import retryrequest
import json
import sys

def check(email, timeout, session, verbose):
    url = 'https://api.twitter.com/i/users/email_available.json?email=' + email
    try:
        r = retryrequest('GET', url, session, timeout=timeout, verbose=verbose)
        data = r.json()
        exists = not data.get('valid', True)
    except Exception as e:
        exists = None
        if verbose:
            print(f'twitter error: {str(e)}', file=sys.stderr)
    return {'service': 'twitter', 'exists': exists, 'url': 'https://twitter.com'}
