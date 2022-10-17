# Django Form

HTML form, input 태그를 통해서 **사용자**로부터 데이터를 받을 때 **비정상적인 혹은 악의적인** 요청이 있을 수 있다.

데이터 형식이 맞는지에 대한 <mark>유효성 검증</mark>이 반드시 필요하다.

Django Form은 이 과정에서 과중한 작업과 반복 코드를 줄여줌으로써 훨씬 쉽게 유효성 검증을 진행할 수 있도록 만들어 줌.

---

### Django는 Form에관련된 작업의 세 부분을 처리.

1. 렌더링을 위한 데이터 준비 및 재구성

2. 데이터에 대한 HTML forms 생성

3. 클라이언트로부터 받은 데이터 수신 및 처리

### Form Class 선언

- form에는 model field와 달리 TextField가 존재하지 않음.
- 'CharField()'를 정의해주고 

>  'New' view 참고.
> 
> - 4일차 파일 참고

> Django의 2가지 html input  요소 표현

1. Form fields
   
   1. 유효성 검사 로직을 처리.

2. Widgets
   
   1. input요소의 단순한 출력 부분을 담당.
   - 뭔 소리인가 > 텍스트 에어리어로 보이게 하는 느낌 ㅇㅋ?

> ### ModelForm

- model.py와 forms.py에 중복이 너무 많다.

- Model을 통해 Form Class를 만들 수 있는 helper class.

> ### ModelForm 선언

- class 내부에 class meta선언.

> ### ModelForm에서의 Meta Class

<img src="Django%20Form_assets/2022-09-06-11-41-45-image.png" title="" alt="" data-align="left">

인스턴스를 **호출하지 않고** 클래스 자체를 넣는 방식을 사용하고 있다.

- "필요한 시점에 " 호출을 하기 위한 방식이다.

![](Django%20Form_assets/2022-09-06-11-45-57-image.png)

- views.index와 같이 이미 자체를 호출하는 방식을 쓰고 있었다.

- views.index() 가 아님. 이 경우 반환 값이 나온다.
+ + ModelForm의 문법이 class 안에 class를 쓰는 것이기 때문에 패턴 자체를 외울것!

# 유효성 검사

> ### Create

![](Django%20Form_assets/2022-09-06-11-57-54-image.png)

- is_valid 하나면 끝이다.

![](Django%20Form_assets/2022-09-06-12-01-56-image.png)

> ### The "save()" method

- save()는 지정된 모델의 새 인스턴스를 만듦. (CREATE)

- 제공되면 save()는 해당 인스턴스를 수정       (UPDATE)

> ### Edit

![](Django%20Form_assets/2022-09-06-12-19-39-image.png)

> ### update

![](Django%20Form_assets/2022-09-06-12-21-48-image.png)

> ### modelform

BaseModelForm을 살펴보자.

![](Django%20Form_assets/2022-09-06-12-25-00-image.png)

data는 첫번째 값에 담겨 있기 때문에 date=request.POST를 쓸 필요 없다.

### Handling HTTP requests

> ### 개요

- "HTTP requests 처리에 따른 view 함수 구조 변화"

- new-create, edit-update의 view 함수 역할을 잘 살펴보면 하나의 공통점과 하나의 차이점이 있음.

- 공통점
  
  - new - create는 모두 생성을 위함.
  
  - edit - updeat는 모두 업데이트를 위함.

- 차이점
  
  - new와 edit 은 GET 요청만 처리함.
  
  - create와 update는 POST 요청만 처리함.

- 이 공통점과 차이점을 바탕으로 views.py를 처리.
1. **new + create**
   
   ![](Django%20Form_assets/2022-09-06-15-30-14-image.png)

2. **update + edit**
   
   ![](Django%20Form_assets/2022-09-06-15-42-14-image.png)

> ### 데코레이터 / Allowed HTTP methods
