#!C:\Users\zhoufan\Programs\VirtualEnv\python27\Scripts\python2.7.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'future==0.15.2','console_scripts','pasteurize'
__requires__ = 'future==0.15.2'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('future==0.15.2', 'console_scripts', 'pasteurize')()
    )
