from scanner import crawler, sqli_scanner, xss_scanner, lfi_scanner, header_checker, cms_detector, \
    sensitive_files_checker
from reports import report_generator
from urllib.parse import urlparse
import logging


def validate_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception:
        return False


def main():
    try:
        target_url = input("Entrez l'URL cible : ").strip()
        if not validate_url(target_url):
            raise ValueError("URL invalide")

        print(f"[+] URL saisie : {target_url}")

        # Vérifications globales
        vulnerabilities = []
        if header_checker.scan(target_url):
            vulnerabilities.append(f"En-têtes HTTP mal configurés sur {target_url}")

        cms = cms_detector.detect(target_url)
        if cms:
            vulnerabilities.append(f"CMS détecté : {cms}")

        # Crawling et scan des URLs
        try:
            urls = crawler.crawl(target_url)
            print(f"[+] URLs trouvées : {len(urls)}")

            for url in urls:
                try:
                    if sqli_scanner.scan(url):
                        vulnerabilities.append(f"Injection SQL détectée sur {url}")
                    if xss_scanner.scan(url):
                        vulnerabilities.append(f"XSS détecté sur {url}")
                    if lfi_scanner.scan(url):
                        vulnerabilities.append(f"Inclusion de fichier détectée sur {url}")
                        if sensitive_files_checker.scan(url):
                            vulnerabilities.append(f"Fichier sensible exposé sur {url}")
                except Exception as e:
                    logging.error(f"Erreur lors du scan de {url}: {str(e)}")

            report_generator.generate(vulnerabilities)

        except Exception as e:
            logging.error(f"Erreur lors du crawling : {str(e)}")

    except KeyboardInterrupt:
        print("\nScan interrompu par l'utilisateur")
    except Exception as e:
        print(f"Une erreur est survenue : {str(e)}")


if __name__ == "__main__":
    main()

