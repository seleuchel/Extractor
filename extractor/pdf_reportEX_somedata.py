# -*- coding: utf-8 -*-

import pdfplumber

file = pdfplumber.open("./IBM2021.pdf")

page_size = len(file.pages)
print("page length is ", len(file.pages))
exf = open("./result33.txt","w",-1, "utf-8")

for i in range(0,page_size):
    first_page = file.pages[i]
    out = first_page.extract_text()
    
    if "CVE-" in out:
        idx = 0
        print("===== page " + str(i) + " data ======")
        exf.write("===== page " + str(i) + " data ======\n")
        
        while True:
            idx = out.find("CVE-",idx+1)
            if idx == -1:
                break
            else:
                startidx = idx
                endidx = out.find(".",idx+1)
              
                if endidx != -1:
                    pass
                else:
                    endidx = len(out)
                print("staridx", startidx, ", endidx", endidx)
                print(out[startidx:endidx+1])
                exf.write(out[startidx:endidx+1])
                exf.write("\n")
                print("find : ", idx)
            
    else:
        pass

file.close()
exf.close()