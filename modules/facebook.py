from utils import retryrequest
import sys

def check(email, timeout, session, verbose):
    url = 'https://www.facebook.com/login/identify/?ctx=recover&email=' + email
    try:
        r = retryrequest('GET', url, session, timeout=timeout, verbose=verbose)
        exists = 'account not found' not in r.text.lower()
    except Exception as e:
        exists = None
        if verbose:
            print(f'facebook error: {str(e)}', file=sys.stderr)
    return {'service': 'facebook', 'exists': exists, 'url': 'https://facebook.com'}
