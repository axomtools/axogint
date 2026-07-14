import json
import sys
import time
import requests
from requests.exceptions import Timeout, ConnectionError, RequestException
import dns.resolver
from colorama import Fore, Style, init
import socks

init(autoreset=True)

def formatoutput(results, fmt, color):
    registered = {s: r for s, r in results.items() if r.get('exists') is True}
    if not registered:
        if color:
            print(Fore.YELLOW + 'no registered accounts found')
        else:
            print('no registered accounts found')
        return
    if fmt == 'json':
        print(json.dumps(registered, indent=2))
    else:
        headers = ['service', 'exists', 'url']
        rows = []
        for s, r in registered.items():
            rows.append([s, str(r.get('exists')), r.get('url', '')])
        colwidths = [max(len(h), max((len(str(row[i])) for row in rows), default=0)) for i, h in enumerate(headers)]
        fmtline = ' | '.join('{:<' + str(w) + '}' for w in colwidths)
        if color:
            print(Fore.CYAN + fmtline.format(*headers))
            print(Fore.CYAN + '-+-'.join('-' * w for w in colwidths))
            for row in rows:
                print(Fore.GREEN + fmtline.format(*row))
        else:
            print(fmtline.format(*headers))
            print('-+-'.join('-' * w for w in colwidths))
            for row in rows:
                print(fmtline.format(*row))

def retryrequest(method, url, session, timeout=10, retries=3, backoff=2, verbose=False, **kwargs):
    last_exception = None
    for attempt in range(retries):
        try:
            if method.upper() == 'GET':
                resp = session.get(url, timeout=timeout, **kwargs)
            elif method.upper() == 'POST':
                resp = session.post(url, timeout=timeout, **kwargs)
            else:
                raise ValueError('unsupported method')
            resp.raise_for_status()
            return resp
        except (Timeout, ConnectionError, RequestException) as e:
            last_exception = e
            if verbose:
                print(f'retry {attempt+1}/{retries} for {url}: {str(e)}', file=sys.stderr)
            if attempt < retries - 1:
                sleep_time = backoff ** attempt
                time.sleep(sleep_time)
            else:
                raise last_exception
        except Exception as e:
            raise e
    raise last_exception

def checkdns(email):
    domain = email.split('@')[-1]
    try:
        dns.resolver.resolve(domain, 'MX')
        return True
    except:
        return False

def setup_session(proxy, usetor):
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    })
    if usetor:
        proxy = 'socks5://127.0.0.1:9050'
    if proxy:
        session.proxies = {
            'http': proxy,
            'https': proxy
        }
    return session
