
import requests

def scan(url):
    test_url = url + "'"
    try:
        r = requests.get(test_url, timeout=5)
        errors = ["sql syntax", "mysql", "unclosed quotation", "quoted string not properly terminated"]
        for error in errors:
            if error in r.text.lower():
                return True
    except:
        pass
    return False
