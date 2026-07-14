from utils import retryrequest
import json
import sys

def check(email, timeout, session, verbose):
    url = 'https://www.pinterest.com/resource/EmailExistsResource/get/'
    params = {'email': email}
    try:
        r = retryrequest('GET', url, session, timeout=timeout, params=params, verbose=verbose)
        data = r.json()
        exists = data.get('resource_response', {}).get('data', {}).get('exists', False)
    except Exception as e:
        exists = None
        if verbose:
            print(f'pinterest error: {str(e)}', file=sys.stderr)
    return {'service': 'pinterest', 'exists': exists, 'url': 'https://pinterest.com'}
