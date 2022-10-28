# DOM !!!

- Document Object Model ( 문서 객체 모델 )

- Document를 어떻게 조작할 것인가 !

- DOM 구조가 동적으로 페이지에 스타일을 추가하는 등, 조작하는 방법을 제공한다.
  
  ## DOM

- 웹 페이지는 결국 하나의 문서이고 브라우저로 인해 해석이 되는 것이다. 때문에 document (문서)라는 이름이 붙은 것이다.

- **DOM은 웹 페이지의 객체 지향 표현**이며, JavaSctipt와 같은 스크립트 언어를 사용하여 수정할 수 있다.

- 특별히 import 할 것은 없다. 기본적으로 설치되어 있기 때문에

- 대신, 특별한 객체를 이용해야한다.
  
  ### window

- DOM의 최상위 객체

- 탭 하나하나가 각각의 window이다.
  
  ### document

- 우리는 브라우저 조작보다는 문서를 조작할 것이다.

- 파싱(Parsing)
  
  - 문자로 된 HTML 문서를 해석하여 Tree구조로 만들고, 스타일을 입힌 후 배치를 하는 것이다.
  - 이 과정은 너무 빠르기 때문에 우리의 눈으로는 볼 수 없지만 이러한 과정을 거쳐서 만들어지는 것이다.

----

## DOM 조작

- 반드시 선택 후 조작
  
  ### 선택
1. 1개를 선택하는 경우
   - document<mark>.querySelector</mark>(selector)
   - 첫 번째 element 객체를 반환. 없다면 null 반환.
2. 여러개를 선택하는 경우
   - document<mark>.querySelectorAll</mark>(selector)
   - 여러 element를 선택
- NodeList
  
  - forEach를 통해 값에 접근할 수 있다.
  
  - querySelectorAll()에 의해 반환되는 NodeList는 DOM의 변경사항을 실시간으로 반영하지 않는다.
    
    ### 조작

- 생성
  
  - document<mark>.createElement</mark>(tagName)
  - 작성한 tagName의 요소를 반환해준다.

- 입력
  
  - Node<mark>.innerText()</mark>
  - 태그 안에 내용을 적는 부분이 innerText이다.

- 추가
  
  - Node<mark>.appendChild()</mark>
  - 부모 노드의 자식 NodeList 중 마지막 자식으로 삽입.
  - 한 번에 오직 하나의 Node만 추가 -> 반환까지

- 삭제
  
  - Node<mark>.removeChild()</mark>
  - DOM 에서 삭제.

- DOM 조작 예시
  
  ![Pasted image 20221024145102.png](C:\Users\saffy\ssafy8\TIL\JavaScript\첨부이미지\Pasted%20image%2020221024145102.png)

- 속성 조회 및 설정
  
  - Element<mark>.getAttribute</mark>(attributeName)
  
  - Element<mark>.setAttribute</mark>(name, value)
    
    - 이미 존재하면 값을 갱신, 존재하지 않으면 생성
      
      ![Pasted image 20221024151608.png](C:\Users\saffy\ssafy8\TIL\JavaScript\첨부이미지\Pasted%20image%2020221024151608.png)

******

# Event

- Event란 프로그래밍하고 있는 시스템에서 일어나는 사건 혹은 발생.
  
  - ex ) 클릭한다, 클릭에 대한 이벤트 발생
  
  - 키 입력, 마우스 갖다대기, 클릭 등등 여러가지 트리거가 존재한다.
    
    ### Event Object

- DOM이 Event를 받고 -> 처리 할 수 있다.
  
  - <mark>addEventListener()</mark>라는 Event 처리기(Event handler)를 다양한 html 요소에 "부착"해서 처리함.
  - "대상에 특정 Event가 발생하면, 할 일을 등록하자"
  - EventTarget.addEventListener(type, listener\[, options])
    - type : input, click, ...etc...
    - listener : 지정한 타입의 Event를 수신할 객체
      - 콜백 함수여야한다.
      - 콜백 합수는 발생한 Event의 데이터를 가진 Event 객체를 유일한 매개변수로 받음.

- [button Event](./js/03_js/event/01_button.html)

- input Event

- button_input

- [<mark>prevent</mark>](./js/03_js/event/04_prevent.html)
  
  - event.preventDefault()
  - 복사를 막아준다. 매주 중요!!

- [lotto](./js/03_js/event/05_lotto.html)

- [todo](./js/03_js/event/06_todo.html)

******

# this

- 이 경우에만 this다! 라는 걸 잘 기억할 것.
- python에서의 self << 인스턴스 자기 자신을 가리킴.
- 함수 호출 방식에 따라 this가 조금씩 달라진다.
- 전역에서
  - console.log(this) :: window를 가리킴.
- 지역에서
  - 단순 함수 호출
  - Method ( 객체의 메서드로서 )
    - object.method()
  - Nested
  - <mark>화살표 함수</mark>는 호출의 위치와 상관없이 상위 스코프를 가리킨다.
  - Lexical scope
    - 함수를 어디서 호출하는지가 아니라 어디에 선언하였는지에 따라 결정.
    - static scope (정적 스코프)라고도하며 대부분의 프로그래밍 언어에서 따르는 방식이다.
    - => <mark>함수 내의 함수 상황에서 화살표 함수를 쓰는 것을 권장.</mark>
- 예외 !!! 
  - addEventListener에서의 콜백 함수를 화살표함수로 쓰게된다면 한 단계 위의 결과가 window를 가리키게 되기 때문에 this를 화살표로 쓰는 이유가 없다.
  - 때문에 addEventListener에서는 그냥 일반적인 콜백함수를 써서 this를 컨트롤 하도록 하자.

> This가 호출되는 순간에 결정되는 것

- 장점 ::
  - 함수를 하나만 만들어서 여러 객체에서 재사용할 수 있다.
- 단점 ::
  - 다만 this의 유연함에의해 실수로 이어질 수 있다. (지역에서의 경우)
- JS this가 좋은지 나쁜지는 우리가 판단하는게 중요한 것이 아니다. **실수를 줄이면서 잘 쓸 생각을 하는 것이 중요한 것이다.**
