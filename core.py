import importlib
import pkgutil
import modules
from concurrent.futures import ThreadPoolExecutor, as_completed
import sys

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
            try:
                res = fut.result()
            except Exception as e:
                res = {'service': mod.__name__.split('.')[-1], 'exists': None, 'error': str(e)}
            results[res.get('service', mod.__name__.split('.')[-1])] = res
    return results
