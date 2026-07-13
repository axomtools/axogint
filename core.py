import importlib
import pkgutil
import modules
from concurrent.futures import ThreadPoolExecutor, as_completed
import sys
from utils import retryrequest

def loadmodules():
    mods = []
    for _, name, _ in pkgutil.iter_modules(modules.__path__):
        mod = importlib.import_module('modules.' + name)
        if hasattr(mod, 'check'):
            mods.append(mod)
    return mods

def runchecks(email, threads, timeout, whitelist):
    allmods = loadmodules()
    if whitelist:
        allmods = [m for m in allmods if m.__name__.split('.')[-1] in whitelist]
    results = {}
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(m.check, email, timeout): m for m in allmods}
        for fut in as_completed(futures):
            mod = futures[fut]
            servicename = mod.__name__.split('.')[-1]
            try:
                res = fut.result()
            except Exception as e:
                res = {'service': servicename, 'exists': None, 'url': '', 'error': str(e)}
            results[res.get('service', servicename)] = res
    return results
