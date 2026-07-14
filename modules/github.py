from utils import retryrequest
import sys

def check(email, timeout, session, verbose):
    url = 'https://github.com/login?email=' + email
    try:
        r = retryrequest('GET', url, session, timeout=timeout, verbose=verbose)
        exists = 'This account has been' not in r.text
    except Exception as e:
        exists = None
        if verbose:
            print(f'github error: {str(e)}', file=sys.stderr)
    return {'service': 'github', 'exists': exists, 'url': 'https://github.com'}
