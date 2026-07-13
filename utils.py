import json
import sys

def formatoutput(results, fmt):
    if fmt == 'json':
        print(json.dumps(results, indent=2))
    else:
        headers = ['service', 'exists', 'url']
        rows = []
        for s, r in results.items():
            rows.append([s, r.get('exists', 'unknown'), r.get('url', '')])
        colwidths = [max(len(h), max((len(str(row[i])) for row in rows), default=0)) for i,h in enumerate(headers)]
        fmtline = ' | '.join('{:<' + str(w) + '}' for w in colwidths)
        print(fmtline.format(*headers))
        print('-+-'.join('-'*w for w in colwidths))
        for row in rows:
            print(fmtline.format(*row))
