from utils import retryrequest
import json
import sys

def check(email, timeout, session, verbose):
    url = 'https://www.reddit.com/api/username_available.json?user=' + email.split('@')[0]
    try:
        r = retryrequest('GET', url, session, timeout=timeout, verbose=verbose)
        data = r.json()
        exists = not data
    except Exception as e:
        exists = None
        if verbose:
            print(f'reddit error: {str(e)}', file=sys.stderr)
    return {'service': 'reddit', 'exists': exists, 'url': 'https://reddit.com'}
