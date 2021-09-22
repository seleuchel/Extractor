# -*- coding: utf-8 -*-

import pdfplumber
import re

file = pdfplumber.open("./IBM2021.pdf")

page_size = len(file.pages)
print("page length is ", len(file.pages))

cve_result = []

for i in range(0,page_size):
    first_page = file.pages[i]
    out = first_page.extract_text()
    
    
    result = re.findall("CVE-[0-9]{4}-[0-9]{4,5}", out)
    
    if len(result) != 0: 
        print("===== page " + str(i) + " data ======")
        exf.write("===== page " + str(i) + " data ======\n")
        
        cve_result.append(result)
        print(result)
            
    else:
        pass

# final
print("cve count is ", len(cve_result))
print(cve_result)


file.close()
