
import requests

def scan(base_url):
    files = [".env", "config.php", "backup.zip", "db.sql"]
    for file in files:
        try:
            r = requests.get(base_url + "/" + file, timeout=5)
            if r.status_code == 200 and len(r.text) > 20:
                return True
        except:
            continue
    return False
