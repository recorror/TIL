# Framework

- 서비스 개발에 필요한 기능들을 미리 구현해서 모아 놓은 것.

- Frame(뼈대, 틀) + Work(일하다)

---

# Web이란?

- www : World Wide Web

- 전 세계에 퍼져있는 거미줄 같은 연결망

---

# 클라이언트와 서버

![](Django%20Base_assets/2022-09-19-05-22-57-image.png)

- 클라이언트가 요청을 보내면 서버가 응답해준다.

- 클라이언트(사용자) / 서버(제공자)

# Web browser와 Web page

> ### 웹 브라우저란?

- 하이퍼 링크를 통해 다른 페이지로 이동할 수 있도록 하는 프로그램.

> ### 웹 페이지란?

- 우리가 보는 한 장 한 장이 웹 페이지.

---

# Django's Disign Pattern, DDP

> ### Django의 디자인 패턴

- MTV 패턴. ( MVC의 변형 )

- MVC : Model, View, Controller ( 데이터 로직, 레이아웃 화면, 모델과 view를 연결 )

- MTV : Model, Template, View ( 데이터 로직, 레이아웃 화면, 모델과 Template를 연결 )

---

> # 요청과 응답

- **URL - VIEW - TEMPLATE** 순의 작성 순서로 코드를 작성하는 편이 흐름 이해하기 편하다.

---

# URL namespace

- 서로 같은 URL 이름을 쓰는 페이지들도  namespace가 다르면 구분이 쉽다.

- 김개똥, 박개똥 같은 느낌.

- urls.py에 **app_name** attribute를 작성해 설정.

- app_name을 지정한 후에는 반드시 **{% url app_name:url_name %}** 형태를 지켜주어야한다.

---

# Database

- 조직화된 데이터를 수집하는 저장 시스템.
  
  1. 스키마( Schema )
     
     - 뼈대
  
  2. 테이블( Table )
     
     - 필드와 레코드, 열과 행

- PK - 각 레코드는 고유의 단일 값을 가진다. 이 값은 절대로 중복되어 나타날 수 없다.

- Query - 데이터를 추출하거나 조작하는 명령어.

---

# Model

![](Django%20Base_assets/2022-09-19-07-14-13-image.png)

- 장고는 Model을 통해 Database에 접근한다.

- 모델 클래스를 작성하는 것은 데이터베이스 테이블의 스키마를 정의 하는 것.
  
  ![](Django%20Base_assets/2022-09-19-07-16-27-image.png)
  
  - models.py에 model class Article을 정의. 
  
  - 이 때 Article은 테이블이고 title과 content라는 뼈대(스키마)를 가지고 있는 것이다.
  
  - 정확하게는 DB 필드 !
  
  - DB 필드의 유형 [보러가기](http://docs.djangoproject.com/en/3.2/ref/models/fields/)

---

### Migrations

- 장고가 모델에 생긴 변화를 DB에 반영하는 방법 !

- 주요 명령어
  
  1. makemigrations
  
  2. migrate - (모델과 DB의 동기화)

---

# ORM

- 객체 지향 // Object - Relational - Mapping

- 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 프로그래밍 기술.
  
  ![](Django%20Base_assets/2022-09-19-07-31-04-image.png)

---

# Query Set

> ### QuerySet API

- database API
  
  - django가 기본적으로 ORM을 제공함에 따른 것으로 DB를 편하게 조작할 수 있도록 도움.
  
  - 모델을 만들면 자동으로 DB API를 만듦.
    
    ![](Django%20Base_assets/2022-09-19-07-55-35-image.png)
    
    ![](Django%20Base_assets/2022-09-19-08-09-01-image.png)

> ### CRUD

- 생성, 조회, 수정, 삭제 create, read, update, dalete !
