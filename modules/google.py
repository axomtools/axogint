from utils import retryrequest

def check(email, timeout, session, verbose):
    url = 'https://mail.google.com/mail/gxlu?email=' + email
    try:
        r = retryrequest('GET', url, session, timeout=timeout, verbose=verbose)
        exists = 'Success' in r.text
    except Exception as e:
        exists = None
        if verbose:
            print(f'google error: {str(e)}', file=sys.stderr)
    return {'service': 'google', 'exists': exists, 'url': 'https://mail.google.com'}
