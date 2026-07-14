import json
import sys
import time
import requests
from requests.exceptions import Timeout, ConnectionError, RequestException

def formatoutput(results, fmt):
    # filter out non-registered (exists != True)
    registered = {s: r for s, r in results.items() if r.get('exists') is True}

    if not registered:
        print("no registered accounts found")
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
        print(fmtline.format(*headers))
        print('-+-'.join('-' * w for w in colwidths))
        for row in rows:
            print(fmtline.format(*row))

def retryrequest(method, url, timeout=10, retries=3, backoff=2, **kwargs):
    last_exception = None
    for attempt in range(retries):
        try:
            if method.upper() == 'GET':
                resp = requests.get(url, timeout=timeout, **kwargs)
            elif method.upper() == 'POST':
                resp = requests.post(url, timeout=timeout, **kwargs)
            else:
                raise ValueError('unsupported method')
            resp.raise_for_status()
            return resp
        except (Timeout, ConnectionError, RequestException) as e:
            last_exception = e
            if attempt < retries - 1:
                sleep_time = backoff ** attempt
                time.sleep(sleep_time)
            else:
                raise last_exception
        except Exception as e:
            raise e
    raise last_exception
