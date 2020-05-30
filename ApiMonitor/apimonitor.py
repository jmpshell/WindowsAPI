'''
This small tool was developed in partnership with Van Souza - idHreusen. 
Its goal is to extract suspicious APIs from Windows binaries.

pip install r2pipe
'''


#!/usr/bin/python
# -*- coding: UTF-8 -*-
import r2pipe
import re
import sys
import os


#Get files
def radare():
    r"""
    Extract the APIS's from the EXE files.
    """
    result = {}
    for i, _file in enumerate(os.listdir('.')):
        if _file.endswith('.exe'):
            r = r2pipe.open(_file)
            apI = str(r.cmd('ii')).split("\n")
            apiSanit = []
            for ap in apI:
                r = re.findall('_\w+',ap)
                if len(r) != 0:
                    apiSanit.append(str(r[0]).replace("_",""))

            result.update({_file: apiSanit})
            print("")
    print("")
    return result


def output(fileName, apis):
    r"""
    Compare result with blacklist of malicious API's
    """

    blacklist = []
    with open('blacklistapi.txt', 'r') as file1:
        rrr = file1.readlines()

        for rr in rrr:
            apI = rr.replace("\n","")
            blacklist.append(apI)



    apisFinal = []
    for api in apis:
        for black in blacklist:
            if api == black:
                apisFinal.append(api+"\n")

    with open('apimalicious.txt', 'a+') as file_out:
        file_out.write("--> "+fileName+"\n")
        file_out.writelines(apisFinal)
        file_out.write("\n")

def run():
    main = []
    apis = radare()

    for fileName in apis:
        output(fileName=fileName ,apis = apis[fileName])
    print("OK!")


if __name__ == '__main__':
        run()

