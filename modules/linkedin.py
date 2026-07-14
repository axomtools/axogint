from utils import retryrequest
import sys

def check(email, timeout, session, verbose):
    url = 'https://www.linkedin.com/checkpoint/lg/login-submit'
    data = {'email': email, 'session_key': email}
    try:
        r = retryrequest('POST', url, session, timeout=timeout, data=data, allow_redirects=False, verbose=verbose)
        exists = r.status_code == 302 and 'login' not in r.headers.get('location', '')
    except Exception as e:
        exists = None
        if verbose:
            print(f'linkedin error: {str(e)}', file=sys.stderr)
    return {'service': 'linkedin', 'exists': exists, 'url': 'https://linkedin.com'}
