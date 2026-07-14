from utils import retryrequest
import sys

def check(email, timeout, session, verbose):
    url = 'https://telegram.org/dl'
    try:
        r = retryrequest('GET', url, session, timeout=timeout, verbose=verbose)
        exists = None
    except Exception as e:
        exists = None
        if verbose:
            print(f'telegram error: {str(e)}', file=sys.stderr)
    return {'service': 'telegram', 'exists': exists, 'url': 'https://telegram.org'}
