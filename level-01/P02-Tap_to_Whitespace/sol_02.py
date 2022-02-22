# (ref) https://codingdojang.com/scode/405#answer-filter-area

import os 
import re   # 정규식 표현 


filename = input("파일 위치와 경로 입력: ") 
ext      = input("확장자 입력: ") 


path = filename + '.' + ext 
print(path)



os.system(f"cp {path} {path+'.bak'}") # backup


with open(path, 'r') as f: 
    src = f.read() 
    with open(path, 'w') as writelist:
        writelist.write(src.replace("\t", "    ") # 
