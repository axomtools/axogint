import importlib
import pkgutil
import modules
from concurrent.futures import ThreadPoolExecutor, as_completed
import sys
import time
from utils import retryrequest, checkdns, setup_session
from tqdm import tqdm
import threading

def loadmodules():
    mods = []
    for _, name, _ in pkgutil.iter_modules(modules.__path__):
        mod = importlib.import_module('modules.' + name)
        if hasattr(mod, 'check'):
            mods.append(mod)
    return mods

def runchecks(email, threads, timeout, whitelist, proxy, usetor, dodns, rate_limit, verbose):
    allmods = loadmodules()
    if whitelist:
        allmods = [m for m in allmods if m.__name__.split('.')[-1] in whitelist]
    if dodns and not checkdns(email):
        print('invalid email or no mx records')
        return {}
    session = setup_session(proxy, usetor)
    results = {}
    lock = threading.Lock()
    progress = tqdm(total=len(allmods), desc='checking', unit='mod', leave=False)
    def check_module(mod):
        nonlocal results
        servicename = mod.__name__.split('.')[-1]
        try:
            res = mod.check(email, timeout, session, verbose)
        except Exception as e:
            res = {'service': servicename, 'exists': None, 'url': '', 'error': str(e)}
        with lock:
            results[res.get('service', servicename)] = res
        if rate_limit > 0:
            time.sleep(rate_limit)
        progress.update(1)
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(check_module, m) for m in allmods]
        for fut in as_completed(futures):
            try:
                fut.result()
            except Exception:
                pass
    progress.close()
    return results
