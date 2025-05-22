
import requests

def scan(url):
    xss_payload = "<script>alert('XSS')</script>"
    try:
        r = requests.get(url, params={"q": xss_payload}, timeout=5)
        if xss_payload in r.text:
            return True
    except:
        pass
    return False
