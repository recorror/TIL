# JavaScript.

> DFS 가 아니라 BFS 형식으로 넓게 볼거임!

-----

### javaScript란?

1. Web 기술의 기반이 되는 언어.
   
   - HTML 문서의 콘텐츠를 `동적으로 변경`할 수 있는 언어

2. 웹브라우저는 HTML/CSS/JavaScript를 해석해서 사용자에게 하나의 화면으로 보여줌.   
   
   **세미콜론**
- ';' 한 줄, 혹은 한 문법이 끝날 때 ; 써야한다.
  **소괄호와 중괄호 사용**
- (), {}
  **코드 스타일 가이드**
- 자바 스크립트 공부할 때는 
- ssafy에선 스타일 가이드 중 "Airbnb Style Guide"를 기반으로 함.
  **주석**
  (//)사용
  "// 어쩌고 저쩌고" 이런 식으로 사용.
  
  **두 글자 들여쓰기 사용**

### JavaScript 코드 스타일 가이드

- Airbnb JavaScript Style Guide

- Google JavaScript Style Guide

- JavaScript Standard Style

***

### 식별자 정의와 특징

- 문자, $, _ 으로 시작한다. 클래스 명 외에는 모두 소문자.

- 예약어 사용 불가능. (ex : for, if, function)
  
  ```
  카멜 케이스
    - 변수, 객체, 함수에 사용
  
  파스칼 케이스
   - 클래스, 생성자에 사용
  
  대문자 스네이크 케이스
   - 상수에 사용
   - 상수 : 개발자의 의도와 상관없이 변경될 가능성이 없는 값.
  ```

- <mark>변수 선언 키워드</mark>
  
  - <mark>let</mark>
    - 블록 스코프 지역 변수를 선언 ( 추가로 동시에 값을 초기화 )
    - 재할당 가능 & 재선언 불가능
  - <mark>const</mark>
    - 블록 스코프 읽기 전용 상수를 선언 (추가로 동시에 값을 초기화)
    - 재할당 불가능 & 재선언 불가능
    - 읽기 전용
    - 초기값을 반드시 설정해야한다. (선언, 할당 다 해줘야함.)
  - <mark>var</mark>
    - 변수를 선언
    - 재할당, 재선언 둘 다 가능.
    - "**호이스팅**" 때문에 예기치 못한 문제 발생한다.
    - 호이스팅이란 : 아래에서 선언한 변수를 선언하기 이전에 참조하는 현상.
    - var는 최대한 쓰면 안 되는 코드이지만 과거에 너무나도 많은 문장들이 var로 작성되어 와서 실질적으로 바로 없애기는 불가능하다.

- 선언, 할당, 초기화
  
  - 선언 : 변수를 생성하는 행위 또는 시점
  - 할당 : 선언된 변수에 값을 저장하는 행위 또는 시점
  - 초기화 : 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점

- 블록 스코프
  
  - if, for, 함수 등의 중괄호 내부 {} 를 가리킴.
  - 블록 스코프 내부의 변수는 내부에서만 쓸 수 있다.

- 정리![[Pa![sted image 20221019152859.png]]](./JavaScript%20기초문법.img/Pasted%20image%2020221019152859.png)

- Airbnb 스타일 가이드에서는 기본적으로 const 사용을 권장.
  
  - 재할당 해야하는 경우에만 let을 쓰도록 한다.

---

# 데이터 타입

## 원시타입 / 참조타입

### 원시타입

- Number : 파이썬이랑 비슷함, NaN 이라는 경우가 있다.
  - .isNaN()을 사용하면 주어진 값이 numver이고 값이 NaN이면 true, 아니면 false
- String : 덧셈만 사용 가능하다.
  - 줄바꿈 시 파이썬처럼 해야함. 아니면 줄 바꾸지 말것.
  - \`백틱 사용시 줄바꿈 마음대로 해도 된다. \`{$}`이런 식으로 f-string 처럼 쓸 수 있다.
- Empty Value
  - 빈 값으로 null 과 undefined가 존재한다.
    - null : 값이 없음을 의도적으로 표현
    - undefined : 직접 값을 할당하지 않으면 자동으로 할당됨.
- Boolean : True와 false
  - 조건문, 반복문에서 boolean이 아닌 데이터 타입은 자동 형변환 규칙에 따라 true, false로 변환된다.![![[Pasted image 20221019154013.png]]](./JavaScript%20기초문법.img/Pasted%20image%2020221019154013.png)

***

- 연산자
  
  - 동등 연산자 (==)
  - 일치 연산자 (===) : 타입과 값이 모두 같아야 같은 것이다.
  - 논리 연산자 : and &&, or ||, not !
  - 삼항 연산자 "조건식 ? A : B"
    - 조건식이 참이면 A를, 거짓이면 B를 반환한다.

- 조건문
  
  - if
  
  - switch : 일반적으로 else if문 보다 유지보수 시에 가독성이 좋아서 편하다.
  
  - while
  
  - for
    
    - C나 java처럼 써주면 된다.
    - for (할당(?); 조건; 증감식;) { 출력 내용 }
  
  - for ... in
    
    - <mark>객체</mark>의 속성을 순회할 때 사용
    - 배열도 순회 가능하지만 인덱스 순으로 순회한다는 보장이 없으므로 권장하지 않는다.
    - 속성 이름을 통해 반복
  
  - for ... of
    
    - <mark>객체 말고 나머지는 기본적으로 of</mark>
    - 반복 가능한 객체를 순회할 때 사용
    - array 등등 반복 가능한 애들
    - 속성 값을 통해 반복
  
  - 정리
  
  - ![![[Pasted image 20221019161139.png]]](./JavaScript%20기초문법.img/Pasted%20image%2020221019161139.png)
    
    ### 참조타입

- 함수
  
  - 함수 선언식 : 일반적인 프로그래밍 언어의 함수 정의 방식과 같다.
    - ![![[Pasted image 20221019162646.png]]](./JavaScript%20기초문법.img/Pasted%20image%2020221019162646.png)
  - 함수 표현식 : 표현식 내에서 함수를 정의하는 방식
    - ![![[Pasted image 20221019162842.png]]](./JavaScript%20기초문법.img/Pasted%20image%2020221019162842.png)
    - 이름을 사용할 수도 있지만 안 써도 된다.
    - 쓰는 경우는 디버깅이 필요할 때
    - <mark>매개변수와 인자의 개수 불일치를 허용한다.</mark>
  - Spread syntax (...)
    - ![![[Pasted image 20221019163305.png]]](./JavaScript%20기초문법.img/Pasted%20image%2020221019163305.png)
    - ![![[Pasted image 20221019163317.png]]](./JavaScript%20기초문법.img/Pasted%20image%2020221019163317.png)
    - 곳곳에서 많이 쓴다.
  - 표현식은 변수를 따라가기 때문에 호이스팅이 없다. 때문에 표현식을 쓰려고 노력해야한다!
  - ![![[Pasted image 20221019233650.png]]](./JavaScript%20기초문법.img/Pasted%20image%2020221019163317.png)

- 화살표 함수
  
  - 함수를 비교적 간결하게 정의할 수 있는 문법.
    1. funtion 키워드 생략 가능
    2. 매개변수가 하나라면 () 도 생략 가능
    3. 함수의 내용이 
  - 즉시 실행 함수
    - 함수 끝에 ()

## Array와 object

### 배열

- 파이썬 list 비슷함.
  - 배열 기초![![[Pasted image 20221020000745.png]]](./JavaScript%20기초문법.img/Pasted%20image%2020221020000745.png)
  - 배열 심화![![[Pasted image 20221020001145.png]]](./JavaScript%20기초문법.img/Pasted%20image%2020221020001145.png)
    - callback함수를 인자로 받는자.
    - callback함수란? 어떤 함수의 내부에서 실행될 목적으로 인자로 넘겨받는 함수.
      - 3가지 매개변수로 구성된다.
        1. element : 배열의 요소
        2. index : 배열 요소의 인덱스
        3. array : 배열 자체
      - 반환값은 없음.
    - **forEach** : 파이썬 map 같은거
      - return 안 써줘도 됨.
    - **map** : forEach+반환 ///배열 메서드 심화 2 38 46 / 15 정도?
      - 리턴 값이 뭐든 사용한다.
    - **filter** : map과는 다르게
      - 리턴 값이 참인 요소만 사용한다.
      - 필터링할 때 주로 사용한다.
      - 중요함. 참인 것을 이용해서 return 참인 경우에만 css 적용 이런 문법이 가능하다.
    - **reduce** : 0번째 매개변수로 acc를 넣어준다.
      - reduce(callback, first_value)
    - **find** :
      - 리턴 값이 참인 경우에 해당 요소 반환.
    - **some**
    - **every**
    - **forEach 말고는 return 을 꼭 써주자!!!**

### 객체

- 딕셔너리라고 생각하면 편하게 접근이 가능하다.

- key - value 쌍으로 표현된다.

- 객체 요소에 접근할 때 . 과 []로 가능하다.

- ES6 문법
  
  1. 속성명 축약
     
     - key와 할당하는 변수 명이 같으면 축약 가능.
  
  2. 메서드명 축약
     
     - 메서드 선언 시 function 키워드 생략 가능
  
  3. 계산된 속성명 사용하기
     
     - 객체를 정의할 때 key의 이름을 표현식을 이용하여 동적으로 생성가능
  
  4. 구조 분해 할당
     
     - 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당할 수 있는 문법
  
  5. 객체 전개 구문(Spread Operator)
     
     - 파이썬의 *과 비슷하다!

- JSON
  
  - JSON을 Object로 사용하기 위해서 문자열로 변환 작업이 필요하다.
    
    ```js
    const jsObject = {
        coffee: 'Americano',
        iceCream: 'Cookie and cream',
    }
    ```
  
  - Object를 JSON으로
    
    ```js
    const objToJson = JSON.stringify(jsObject)
    ```
  
  - JSON을 Object로
    
    ```js
    const jsonToObj = JSON.parse(objToJson)
    ```