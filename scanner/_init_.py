
#scanners/_init_.py*

from cms_detector import detect as detect_cms
from sqli_scanner import scan as scan_sqli
from xss_scanner import scan as scan_xss
from lfi_scanner import scan as scan_lfi
from header_checker import scan as check_headers
from sensitive_files_checker import scan as check_sensitive_files


_all_ = [
    "detect_cms",
    "scan_sqli",
    "scan_xss",
    "scan_lfi",
    "check_headers",
    "check_sensitive_files"
]
