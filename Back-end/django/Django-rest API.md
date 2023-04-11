-----
- 우선 http에 대해 알 필요가 있다.
## HTTP
- Stateless (무상태)
	- 응답을 마치고 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나면 상태 정보가 유지되지 않는다.
	- 하지만 연결을 연속적으로 수행해야하는 상황이라면?
	- 예를 들어 e-commerce에서 장바구니를 사용하는 경우.
	- > 쿠키와 세션을 사용해 서버 상태를 요청해 연결한다.
- HTTP Request Methods
	- response status codes
	1. Successful response 200 - 299
	2. Redirection messages 300 - 399
	3. Client error response 400 - 499
	4. Server error response 500 - 599
---
### URI

- Uniform Resource Identifier (통합 자원 식별자)
- 가장 일반적인 URI는 웹 주소로 알려진 **URL**
- 리소스를 식별하는 URI는 **URN**
> **URL**
> - Uniform Resource Locator 통합 자원 위치
> - Schema : https (프로토콜)
> - Authority : domain 과 port (root주소 / main 주소)
> 	1. Domain Name = IP주소를 외우기 쉽게 나타낸 이름.
> 	2. Port = 접근하는데 사용되는 기술적인 문(Gate)
> 		- HTTP 프로토콜이 80 or 443 인 경우 자동으로 생략이 됨.
> - Path : article/ 머시기 이런 거
> - Parameters : & 기호로 구분되는 거, ?로 시작 = GET 요청일 때
> - Anchor : 하이퍼링크와 비슷한 기능을 하는 넷상의 다른 문서와 연결된 문자 혹은 그림.

> **URN**
> - URL의 단점을 극복하기 위해 등장했다.
> - 이름으로 쓰는거 (아마도 철면수심.com 이런거인듯)

***
# REST API
## API
- Application Programming Interface
- 애플리케이션과 프로그래밍으로 소통하는 방법
- API와 다른 소프트웨어 혹은 하드웨어와의 간단한 계약(인터페이스)
## Web Api
- 현재 웹 개발은 일일이 개발하기보다 여러 ==Open API==를 활용한다.
- 대표적으로는 'Youtube API', 'Naver Papago API', 'Kakao Map API' 등등
- API는 다양한 타입의 데이터를 응답.
	- HTML, XML, JSON 등등...
## REST
- Representational State Transfer
- 일종의 API server를 개발하기 위한 소프트웨어 설계 방법론
- REST 원리를 따르는 시스템을 RESTful 하다고 부른다.
- <mark>자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법을 서술.</mark>

### REST에서 자원을 정의하고 주소를 지정하는 방법.
1. 자원의 식별 :: URI
2. 자원의 행위 :: HTTP Method
3. 자원의 표현 :: JSON으로 표현된 데이터를 제공.
	- 이 양식을 갖추면 RESTful하다고 하는 것.
### JSON
- javaScript의 표기법을 따른 단순 문자열.
- 파이썬의 dict 형태처럼 C계열의 언어가 갖고 있는 자료구조로 쉽게 변환할 수 있는 <mark>key - value 형태의 구조</mark>를 갖고있다.
****
## Response JSON
> 서버가 응답하는 것
	![[Pasted image 20221017122125.png]]
### Serialization
- "직렬화"
- "나중에 다시 쉽게 사용할 수 있는 포맷으로 변환하는 과정"
- 변환 포맷 종류 :: json, xml, yaml ... json이 가장 보편적임!
- ![[Pasted image 20221017141459.png]]
### <mark>DRF</mark> (Django REST framework)
- Django에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리.
- Django의 serializer는 form, modelForm 클래스와 매우 유사하게 작동한다.
>**ModelSerializer** 
 =='api_view'== decorator 반드시 작성할것!