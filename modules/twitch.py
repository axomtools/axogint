from utils import retryrequest
import sys

def check(email, timeout, session, verbose):
    url = 'https://id.twitch.tv/oauth2/validate?email=' + email
    try:
        r = retryrequest('GET', url, session, timeout=timeout, verbose=verbose)
        exists = r.status_code != 400
    except Exception as e:
        exists = None
        if verbose:
            print(f'twitch error: {str(e)}', file=sys.stderr)
    return {'service': 'twitch', 'exists': exists, 'url': 'https://twitch.tv'}
