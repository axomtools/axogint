import requests

def check(email, timeout):
    url = 'https://id.twitch.tv/oauth2/validate?email=' + email
    try:
        r = requests.get(url, timeout=timeout)
        exists = r.status_code != 400
    except:
        exists = None
    return {'service': 'twitch', 'exists': exists, 'url': 'https://twitch.tv'}
