
import requests

def scan(url):
    try:
        r = requests.get(url, timeout=5)
        headers = r.headers
        issues = []
        if "X-Frame-Options" not in headers:
            issues.append("X-Frame-Options missing")
        if "Content-Security-Policy" not in headers:
            issues.append("CSP missing")
        return issues if issues else False
    except:
        return False
