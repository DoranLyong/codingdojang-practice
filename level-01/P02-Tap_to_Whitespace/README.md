# [탭을 공백 문자로 바꾸기](https://codingdojang.com/scode/405?answer_mode=hide)



**[문제]**

```
A씨는 개발된 소스코드를 특정업체에 납품하려고 한다. 개발된 소스코드들은 탭으로 들여쓰기가 된것, 공백으로 들여쓰기가 된 것들이 섞여 있다고 한다. A씨는 탭으로 들여쓰기가 된 모든 소스를 공백 4개로 수정한 후 납품할 예정이다.

A씨를 도와줄 수 있도록 소스코드내에 사용된 탭(Tab) 문자를 공백 4개(4 space)로 바꾸어 주는 프로그램을 작성하시오.
```



**[해법 스텝]**

* 코드 파일 읽어 들이기 
* Tap(`\t`) 인 부분을 공백 4개(`"    "`) 로 바꾸기 
* 바꾼 내용을 새로 저장하기 



**[학습 내용]**

* 파일 읽고 쓰기 ; 

  ```python
  with open(<file_name>, 'r') as f: 
      src = f.read()    # 읽기 
      with open(<save_name>, 'w') as wf: 
          wf.write(src.replace("\t", "    "))
  ```

* [string replace](https://ooyoung.tistory.com/77) 

  ```python
  a = "hello world"
  a.replace("hello", "hi")
  ```

  

