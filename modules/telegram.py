import requests

def check(email, timeout):
    url = 'https://telegram.org/dl'
    try:
        r = requests.get(url, timeout=timeout)
        exists = None  # trash but ight (inaccurate answer for the telegram) 
    except:
        exists = None
    return {'service': 'telegram', 'exists': exists, 'url': 'https://telegram.org'}
