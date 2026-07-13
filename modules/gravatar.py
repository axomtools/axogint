import requests
import hashlib

def check(email, timeout):
    h = hashlib.md5(email.strip().lower().encode('utf-8')).hexdigest()
    url = 'https://www.gravatar.com/avatar/' + h + '?d=404&s=1'
    try:
        r = requests.get(url, timeout=timeout)
        exists = r.status_code == 200
    except:
        exists = None
    return {'service': 'gravatar', 'exists': exists, 'url': 'https://gravatar.com/' + h}
