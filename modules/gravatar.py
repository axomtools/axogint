from utils import retryrequest
import hashlib
import sys

def check(email, timeout, session, verbose):
    h = hashlib.md5(email.strip().lower().encode('utf-8')).hexdigest()
    url = 'https://www.gravatar.com/avatar/' + h + '?d=404&s=1'
    try:
        r = retryrequest('GET', url, session, timeout=timeout, verbose=verbose)
        exists = r.status_code == 200
    except Exception as e:
        exists = None
        if verbose:
            print(f'gravatar error: {str(e)}', file=sys.stderr)
    return {'service': 'gravatar', 'exists': exists, 'url': 'https://gravatar.com/' + h}
