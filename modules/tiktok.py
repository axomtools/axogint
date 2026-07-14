from utils import retryrequest
import json
import sys

def check(email, timeout, session, verbose):
    url = 'https://www.tiktok.com/api/v1/auth/email/exists/'
    data = {'email': email}
    try:
        r = retryrequest('POST', url, session, timeout=timeout, data=data, verbose=verbose)
        res = r.json()
        exists = res.get('data', {}).get('exists', False)
    except Exception as e:
        exists = None
        if verbose:
            print(f'tiktok error: {str(e)}', file=sys.stderr)
    return {'service': 'tiktok', 'exists': exists, 'url': 'https://tiktok.com'}
