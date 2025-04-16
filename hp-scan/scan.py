import os

from hpscancli.main import HPScanner


def do_scan():
    scanner = HPScanner(ip=os.getenv("HP_SCANNER_IP"))
    print(scanner.get_capabilities())
