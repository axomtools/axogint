from utils import retryrequest
import sys

def check(email, timeout, session, verbose):
    url = 'https://vimeo.com/api/v2/users/email/' + email
    try:
        r = retryrequest('GET', url, session, timeout=timeout, verbose=verbose)
        exists = r.status_code == 200
    except Exception as e:
        exists = None
        if verbose:
            print(f'vimeo error: {str(e)}', file=sys.stderr)
    return {'service': 'vimeo', 'exists': exists, 'url': 'https://vimeo.com'}
