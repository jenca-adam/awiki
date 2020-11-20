#!/usr/bin/env python3
import os,re
dirnamepattern=r'^[^R][^E][^F]\D*\d{4}\D*$'
for d in os.listdir('.'):
    if re.search(dirnamepattern,d):
        os.chdir('myown')
        filepattern=f'\[{d}\]\({d}\)'
        with open('page.md')as file:
            string=file.read()
        if not re.search(filepattern,string):
            os.chdir('..')
            os.chdir('notmyown')
            with open('page.md')as file:
                string=file.read()
            if not re.search(filepattern,string):
                print(f'[{d}]({d})')
        os.chdir('..')
