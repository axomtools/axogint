from utils import retryrequest
import json
import sys

def check(email, timeout, session, verbose):
    url = 'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/'
    headers = {'x-requested-with': 'XMLHttpRequest'}
    data = {'email': email}
    try:
        r = retryrequest('POST', url, session, timeout=timeout, headers=headers, data=data, verbose=verbose)
        res = r.json()
        exists = res.get('email_is_taken', False)
    except Exception as e:
        exists = None
        if verbose:
            print(f'instagram error: {str(e)}', file=sys.stderr)
    return {'service': 'instagram', 'exists': exists, 'url': 'https://instagram.com'}
