# String



### 컴퓨터에서의 **문자표현**

- 메모리는 숫자만을 저장할 수 있기 때문에 
  
  -                 **글자에 대응하는 숫자를 정해놓고 사용된다.**



- issue  :  **초기**에 네트워크가 발전되기 전 지역 별로 코드체계를 정해놓았다. 때문에 인터넷이 발달하면서 서로 정보를 주고 받을 때 정보를 달리 해석하는 문제가 발생하였다.
  
  > **ASCII 코드**라는 **문자 인코딩 표준**이 제정됨.
  > 
  > American Standard Code for Information Interchange
  > 
  > ASCII(32) = ' ' < 공백은 문자열.
  > 
  > A = ASCII(65), a = ASCII(97)
  > 
  > **확장 ASCII라는게 있긴함.**

- issue 2  :  각 나라에서도 자국의 문자를 표현하기 위하여 코드체계를 만들어서 사용하게 되었다. 때문에 국가간의 정보를 주고 받을 때 또 문제가 생기게 되었다.
  
  > 그래서 생긴것이 다국어 표준 처리 **'유니코드'** 이다.
  > 
  > UCS-2, UCS-4

- issue 3 : 유니코드도 바이트 순서에 대해서 표준화 하지 못했다. 때문에 적당한 외부 인코딩이 필요하게 되었다.
  
  > **유니코드 인코딩 (UTF : Unicode Transformation Format)**
  > 
  > - UTF-8 / min 8bit, max 32bit
  > 
  > - UTF-16 / min 16bit, max 32bit
  > 
  > - UTF-32 / min 32bit, max 32bit
  > 
  > **Python 인코딩**
  > 
  > - 2.x 버전 - ASCII -> 이런식으로 첫 줄에 적어줬어야함.
  > 
  > - 3.x 버전 생략 가능
  > 
  > - 다른 인코딩 방식을 사용 할 때는 첫 줄에 원하는 인코딩 방식 지정.



### 문자열

- char 타입 없다.

- 텍스트 데이터의 취급방법이 통일되어 있다.

- +연결, 문자열을 이어붙여줌

- *반복, 수만큼 문자열이 반복된다.

- **시퀀스 자료형이다.**
  
  - 인덱싱, 슬라이싱 연산 사용가능.

- replace(), split(), isalpha(), find() 사용 가능

- **immutable**하다. (요소값을 변경 할 수 없다.)

- [문자열 뒤짚는 방법.](./String/string_reverse.py)



### 문자열 비교

- ['==', 'is'의 차이점!](./String/string_empty.py)

- [itoa 구현](./String/string_reverse.py)


