from flask import Flask, request, render_template_string, jsonify
import sys
import json
from core import runchecks

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>AXOGINT Web</title>
    <style>
        body { font-family: sans-serif; margin: 40px; background: #f4f4f4; }
        .container { max-width: 800px; margin: auto; background: white; padding: 20px; border-radius: 8px; }
        input, select, button { padding: 8px; margin: 5px; }
        .result-table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        .result-table th { background: #333; color: white; padding: 8px; text-align: left; }
        .result-table td { border: 1px solid #ddd; padding: 8px; }
        .result-table tr:nth-child(even) { background: #f9f9f9; }
        .true { color: green; font-weight: bold; }
        .unknown { color: orange; }
        .error { color: red; }
        .form-group { margin: 10px 0; }
        .form-group label { display: inline-block; width: 100px; }
        .btn { background: #007bff; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; }
        .btn:hover { background: #0056b3; }
        .footer { margin-top: 20px; font-size: 0.8em; color: #666; }
    </style>
</head>
<body>
    <div class="container">
        <h1>AXOGINT</h1>
        <form method="post">
            <div class="form-group">
                <label>Email:</label>
                <input type="email" name="email" required value="{{ email or '' }}" size="30">
            </div>
            <div class="form-group">
                <label>Threads:</label>
                <input type="number" name="threads" value="{{ threads or 20 }}" min="1" max="100">
            </div>
            <div class="form-group">
                <label>Timeout (s):</label>
                <input type="number" name="timeout" value="{{ timeout or 10 }}" min="1" max="60">
            </div>
            <div class="form-group">
                <label>Modules:</label>
                <input type="text" name="modules" placeholder="space separated, e.g. google facebook" value="{{ modules or '' }}">
            </div>
            <div class="form-group">
                <label>Proxy:</label>
                <input type="text" name="proxy" placeholder="socks5://127.0.0.1:9050" value="{{ proxy or '' }}">
            </div>
            <div class="form-group">
                <label>Rate limit (s):</label>
                <input type="number" name="rate_limit" value="{{ rate_limit or 0 }}" step="0.1" min="0">
            </div>
            <div class="form-group">
                <label><input type="checkbox" name="tor" {% if tor %}checked{% endif %}> Use Tor</label>
                <label><input type="checkbox" name="dns" {% if dns %}checked{% endif %}> DNS check</label>
                <label><input type="checkbox" name="verbose" {% if verbose %}checked{% endif %}> Verbose</label>
            </div>
            <button type="submit" class="btn">Scan</button>
        </form>

        {% if results is defined %}
        <h2>Results for {{ email }}</h2>
        {% if results %}
        <table class="result-table">
            <tr><th>Service</th><th>Exists</th><th>URL</th></tr>
            {% for service, data in results.items() if data.exists == True %}
            <tr>
                <td>{{ service }}</td>
                <td class="true">True</td>
                <td><a href="{{ data.url }}" target="_blank">{{ data.url }}</a></td>
            </tr>
            {% endfor %}
            {% if results|selectattr('exists', 'equalto', True)|list|length == 0 %}
            <tr><td colspan="3">No registered accounts found.</td></tr>
            {% endif %}
        </table>
        <div class="footer">lookup registered platforms</div>
        {% endif %}
        {% endif %}
    </div>
</body>
</html>
'''

def start_web():
    app.run(host='0.0.0.0', port=5000, debug=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        if not email:
            return render_template_string(HTML, error='Email required')
        threads = int(request.form.get('threads', 20))
        timeout = int(request.form.get('timeout', 10))
        modules_str = request.form.get('modules', '')
        modules = modules_str.split() if modules_str else None
        proxy = request.form.get('proxy', '') or None
        tor = 'tor' in request.form
        dns = 'dns' in request.form
        verbose = 'verbose' in request.form
        rate_limit = float(request.form.get('rate_limit', 0))

        results = runchecks(email, threads, timeout, modules, proxy, tor, dns, rate_limit, verbose, progress=False)
        registered = {s: r for s, r in results.items() if r.get('exists') is True}
        return render_template_string(HTML, email=email, results=registered,
                                      threads=threads, timeout=timeout, modules=modules_str,
                                      proxy=proxy, tor=tor, dns=dns, verbose=verbose, rate_limit=rate_limit)
    return render_template_string(HTML)

if __name__ == '__main__':
    start_web()
