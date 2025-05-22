from scanner import crawler, sqli_scanner, xss_scanner, lfi_scanner, header_checker, cms_detector, \
    sensitive_files_checker
from reports import report_generator


def main():
    target_url = input("Entrez l'URL cible : ")
    print(f"[+] URLs saisie:{target_url}")
    urls = crawler.crawl(target_url)
    print(f"[+] URLs trouvées:{urls}")
    vulnerabilities = []

    for url in urls:
        if sqli_scanner.scan(url):
            vulnerabilities.append(f"Injection SQL détectée sur {url}")
        if xss_scanner.scan(url):
            vulnerabilities.append(f"XSS détecté sur {url}")
        if lfi_scanner.scan(url):
            vulnerabilities.append(f"Inclusion de fichier détectée sur {url}")
            if sensitive_files_checker.scan(url):
                vulnerabilities.append(f"Fichier sensible exposé sur {url}")
        if header_checker.scan(target_url):
            vulnerabilities.append(f"En-têtes HTTP mal configurés sur {target_url}")
        cms = cms_detector.detect(target_url)
        if cms:
            vulnerabilities.append(f"CMS détecté : {cms}")

    report_generator.generate_report(vulnerabilities)

    if name == "main":
        main()
