from utils import retryrequest
import json
import sys

def check(email, timeout, session, verbose):
    url = 'https://www.youtube.com/email_ajax?email=' + email
    try:
        r = retryrequest('GET', url, session, timeout=timeout, verbose=verbose)
        data = r.json()
        exists = data.get('status', '') == 'TAKEN'
    except Exception as e:
        exists = None
        if verbose:
            print(f'youtube error: {str(e)}', file=sys.stderr)
    return {'service': 'youtube', 'exists': exists, 'url': 'https://youtube.com'}
