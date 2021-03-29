#!D:\Teleg_bot\new_test\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'country-converter==0.6.7','console_scripts','coco'
__requires__ = 'country-converter==0.6.7'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('country-converter==0.6.7', 'console_scripts', 'coco')()
    )
