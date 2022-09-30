# Namespace

- app 을 여러개를 만들었을 때 같은 이름의 주소를 입력하면 구분이 안 되어 하나의 주소로만 연결되기 때문에 Namespace를 만들어 구분을 둔다.
- 보통 Namespace의 경우 상위 폴더의 이름과 똑같이 만든다.

****

# Model

- ORM을 통해 간단한 부분은 조작할 수 있다.
- db라고 생각하면 됨.
- 테이블
  - 필드 - 콜럼col
  - 데이터 - 로우row, 튜플
- PK 중복되면 안 되는 값 idx 값 같은거.

### Migration

- 모델에 생긴 변화를 DB에 반영하는 방법.
  - python manage.py makemigrations
  - 만든 앱을 기반으로 새로운 migration 만들 때 사용
  - python manage.py migrate
  - DB에 실질적으로 반영.(동기화)
- 기타 명령어도 공부해야함!
  - showmigrations
  - sqlmigrate

****

# ORM

- object- relational-mapping
- django <-> SQL 데이터를 변환하는 기술
  - 장점 : sql을 잘 몰라도 DB 조작이 가능
  -   : 객체 지향적 접근으로 인한 높은 생산성
  - 단점 : ORM만으로 완전한 서비스를 구현하기 어려운 경우가 있음
    
       즉, SQL을 따로 공부해야함.
    
    > **DateTimeField()**
    1. auto_now_add
       - 아나? 모르지? 최초 생성일자
    2. auto_now
       - 안. 안다. 최종 수정일자

****

# QuertSet API

> **database API**
>     - ORM !
>     - Model을 만들면 자동으로 DB API 만들어 줌.
>       - django는 객체들을 만들고 읽고 수정하고 지울 수 있다.
>       <img src="Django%20Model_assets/2022-09-01-11-48-38-image.png" title="" alt="" width="325">
> 
> **"objects"manager**
> 
> - Django 모델이 데이터베이스 쿼리 작업을 가능하게 하는 인터페이스
> 
> - 이 Manager를 통해 특정 데이터를 조작할 수 있음.
> 
> - <mark>"DB를 python class로 조작할 수 있도록 여러 메서드를 제공하는 manager"</mark>

### Query

- 데이터베이스에 특정한 데이터를 보여 달라는 요청

- ORM에 의해 SQL로 변환되어 데이터베이스에 전달되며, 데이터베이스의 응답 데이터를 ORM이 <mark>QuerySet</mark>이라는 자료 형태로 변환하여 우리에게 전달.

### QuerySet

- 데이터베이스에게서 전달 받은 객체 목록(데이터 모음)

- 데이터베이스가 단일한 객체를 반환 할 때는 QuerySet이 아닌 모델의 인스턴스로 반환됨.

![](Django%20Model_assets/2022-09-01-12-01-09-image.png)

                    querySet과 상호작용하기 위해 사용하는 도구

### CRUD

        - Create / Read / Update / Delete

        - 생성    /  조회   /   수정    /   삭제

- 대부분의 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능 4가지를 묶어서 일컫는 말.

### Create

- Models.py 작성 예시

```python
class Post(models.Model):
    # CharField, TextField 둘 다 문자를 저장하기 위한 필드
    # CharField = 길이 제한 有 / TextField = 길이 제한 無
    title = models.CharField(max_length=255)
    content = models.TextField()
```

- views에 DB 저장하는 거 적어주기.

```python
# 사용자가 작성한 데이터를 받아서 DB에 저장하는 역할
def create(request):
    # 데이터를 저장하기 위해서는 사용자의 데이터를 확보
    # print(request.GET)
    title = request.GET.get(title)
    content = request.GET.get(content)
    # 확보한 데이터를 DB에 저장

    # 데이터를 DB에 저장하는 방법은 3가지가 존재
    # 1번 방법 (POST 클래스의 인스턴스를 생성)
    post = Post()
    post.title = title
    post.content = content
    post.save() # DB에 저장
    # 2번 방법
    post = Post(title = title, content = content,)
    post.save()
    # 3번 방법 Queryset API create 메서드를 이용한다.
    # 반환되는 인스턴스는 이미 DB에 저장된 데이터
    post = Post.objects.create(title=title,content=content)
```



### GET