from utils import retryrequest
import sys

def check(email, timeout, session, verbose):
    url = 'https://www.ebay.com/signin/'
    data = {'email': email}
    try:
        r = retryrequest('POST', url, session, timeout=timeout, data=data, allow_redirects=False, verbose=verbose)
        exists = r.status_code == 302
    except Exception as e:
        exists = None
        if verbose:
            print(f'ebay error: {str(e)}', file=sys.stderr)
    return {'service': 'ebay', 'exists': exists, 'url': 'https://ebay.com'}
