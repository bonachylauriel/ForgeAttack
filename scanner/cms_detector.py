
import requests

def detect(url):
    try:
        r = requests.get(url, timeout=5)
        if "wp-content" in r.text:
            return "WordPress"
        elif "Joomla" in r.text:
            return "Joomla"
        elif "Drupal" in r.text:
            return "Drupal"
    except:
        pass
    return None
