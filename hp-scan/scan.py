import os
from time import sleep

from hpscancli.main import HPScanner


def _test_connectivity(scanner_ip: str):
    retries = 5
    attempt = 0
    scanner = None
    print(f"Connecting to {scanner_ip}")
    while scanner is None and attempt < retries:
        print(f" - Attempt {attempt}")
        scanner = HPScanner(ip=scanner_ip)
        sleep(1)
    if scanner is None:
        print(f"Failed to connect to to scanner at {scanner_ip}")
        exit(1)
    return scanner


def do_scan(filename: str = None):
    scanner = _test_connectivity(scanner_ip=os.getenv("HP_SCANNER_IP"))
    scanner.perform_scan(pdf=True, out_file_name=filename)
