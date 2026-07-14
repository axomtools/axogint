from utils import retryrequest
import sys

def check(email, timeout, session, verbose):
    url = 'https://www.behance.net/v2/users/email/' + email
    try:
        r = retryrequest('GET', url, session, timeout=timeout, verbose=verbose)
        exists = r.status_code == 200
    except Exception as e:
        exists = None
        if verbose:
            print(f'behance error: {str(e)}', file=sys.stderr)
    return {'service': 'behance', 'exists': exists, 'url': 'https://behance.net'}
