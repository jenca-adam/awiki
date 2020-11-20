#!/usr/bin/python
import os,re
pattern=re.compile('\D*\d{4}\D*')
basic=os.getcwd()
def main():
    for i in os.listdir('.'):   
        if re.search(pattern,i):
            if os.path.isdir(i):
                os.chdir(i)
                try:
                    file=open('bib.bib')
                    content=file.read()

                except FileNotFoundError:
                    pass
                listcontent=list(content)
                index=0
                for b in listcontent:
                    if b=='{':
                        if listcontent[index+1]==',':
                            print(i)
                    index+=1
                os.chdir(basic)
if __name__=='__main__':
    main()


