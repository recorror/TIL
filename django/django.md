# django

> ### Framework

- 웹 서비스 개발을 쉽게 할 수 있게 도와준다.

> ### 클라이언트와 서버

- 클라이언트가 요청을 하면 서버는 요청에 따른 응답을 준다.
  
  - input = 요청, output = 응답. 

> **클라이언트**
> 
> - 웹 브라우저를 가지고 요청을 한다. Chrome or Firefox와 같은 웹 브라우저.
> 
> **서버**
> 
> - 웹 페이지, 사이트 또는 앱을 저장하고 있는 컴퓨터.
> 
> - 클라이언트가 웹 페이지에 **접근**하려고 할 때 클라이언트 컴퓨터가 해당 페이지를 **응답**해 표시해줌.

> ### 웹 브라우저란?

- 웹에서 페이지를 찾아 보여주고 사용자가 하이퍼 링크를 통해 타른 페이지로 이동할 수 있도록 하는 프로그램.

- 웹 페이지 파일을 우리가 보는 화면으로 바꿔주는 렌더링 프로그램

- 정적 페이지, 동적 페이지

> 정적 페이지 = 항상 같은 모습을 보여줌
> 
> - 있는 그대로를 보여준다.
> 
> 동적 페이지 = 예를들면 로그인 했을 때 다르게 보이는 느낌.
> 
> - 요청에 따라 추가적인 수정이 되어 클라이언트에게 전달된다.
>   
>   - ex) 장바구니
> 
> - 웹 페이지의 내용을 바꿔주는 주체 == **서버**
>   
>   - 서버를 쉽게 만들기 위해 프레임워크를 사용한다.

> ### MVC패턴

- 모델, 뷰, 컨트롤러
  
  - 모델         : DB와 관련.
  
  - 뷰             : 레이아웃과 같은 화면을 보여주는 부분.
  
  - 컨트롤러 : 모델과 뷰 영역을 컨트롤하는 주체.

> ### 장고 흐름

1. 요청

2. 요청확인        Url

3. 요청처리        View

4. 필요한 거 가지고 옴    Model

5. 서버에 응답 요청

6. 응답 받은걸 return

7. 1번 요청에 대한 응답

> ### MTV

- 모델, 템플릿, 뷰
  
  - MVC랑 같은 개념인데 이름만 다르게했다.

> ### DTL - Templats

- Tags
  
  -   {{   값   }}     값을 표현할 때
  
  -  {% 태그 %}   태그를 사용할 때
  
  - if 나 for 와 같은 들여쓰기가 있는 태그들은 닫는 쌍이 필요하다.
    
    - ex ) {% if %}{% endif %} 이런 식으로.

- comment
  
  - DTL 태그는 <!---->로 닫으면 안 되고 comment로 닫아야한다! 아니면 오류남.
  
  - {%comment%}{%endcomment%} 코멘트도 태그와 마찬가지로 닫는 쌍이 필요하다.

# 템플릿 상속

- **코드의 재사용성**에 중점을 둠.

- 모든 템플릿에 일일히 작성해주기 번거롭고 짜증나기 때문에 상속을 이용해 해결해보자.
  
  - {% extends '' %}
  
  - header와 footer와 같이 공통 사용되는 코드들에 대해



# Variable routing
- Url 주소를 변수로 사용하는 것을 의미.
- Url의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음.
- 주소 이동할 때 path의 일부분을 변수로 사용. (사용자의 입력 x)
- Query string parameter의 경우 사용자의 입력이 반드시 필요하다.
- 