from utils import retryrequest
import json
import sys

def check(email, timeout, session, verbose):
    url = 'https://vk.com/rest/method/auth.checkPhone'
    data = {'email': email}
    try:
        r = retryrequest('POST', url, session, timeout=timeout, data=data, verbose=verbose)
        res = r.json()
        exists = res.get('response', {}).get('exists', False)
    except Exception as e:
        exists = None
        if verbose:
            print(f'vk error: {str(e)}', file=sys.stderr)
    return {'service': 'vk', 'exists': exists, 'url': 'https://vk.com'}
