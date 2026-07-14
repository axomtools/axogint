from utils import retryrequest
import sys

def check(email, timeout, session, verbose):
    url = 'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&email=' + email
    try:
        r = retryrequest('GET', url, session, timeout=timeout, verbose=verbose)
        exists = 'invalid email' not in r.text.lower()
    except Exception as e:
        exists = None
        if verbose:
            print(f'microsoft error: {str(e)}', file=sys.stderr)
    return {'service': 'microsoft', 'exists': exists, 'url': 'https://outlook.com'}
