# Managing static files

- 개발자가 서버에 미리 준비한 혹은 사용자가 업로드한 **정적파일**을 클라이언트에게 제공하는 방법.

> ### 정적파일

- 별도의 처리없이 그대로 보여주는 파일.

- <mark>파일 자체가 고정</mark>되어 있고, 서비스 중에도 추가되거나 <mark>변경되지 않고 고정</mark>!
  
  - ex )  이미지, JS file, css file 등과 같이 미리 설정해두고 설정하지 않는 이상 가변적이지 않은 이미지들.

> ### 미디어파일

- 사용자가 웹에서 업로드하는 모든 파일

---

### Static files

> ### 웹 서버와 정적 파일

- 사진 파일을 얻기 위한 경로인 웹 주소(url)가 존재함.

- 즉, 요청 받은 URL로 서버에 존재하는 정적 자원을 제공해줘야한다.

> ### Media File

- 미디어 파일

- 사용자에 웹에서 업로드하는 정적 파일

- 유저가 업로드 한 모든 정적 파일

> ### Django에서 정적파일을 구성하고 사용하기 위한 단계.

1. settings.py의 INSTALLED_APPS에 contrib.staticfiles가 포함되어 있는지 확인하기.

2. settings.py에서 STATIC_URL 정의하기

3. 앱의 static폴더에 정적 파일을 위치하기
   
   - my_app/static/sample_img.jpg

4. 템플릿에서 static 템플릿 태그를 사용하여 지정된 경로에 있는 정적 파일의 URL 만들기.
   
   ```html
   {% load static %}
   <img src="{% static 'sample_img.jpg' %}"> alt="sample image">
   ```
   
   x ) 그냥은 못 쓰고 load 해주고 써야한다.

> ### Django template tag
> 
> ```html
> {% load static %} 
> {% static '' %}
> ```

- load tag = 특정 라이브러리, 패키지에 등록된 모든 템플릿 태그와 필터를 로드

- static tag = STATIC_ROOT에 저장된 정적 파일에 연결

> ### static files 관련 Core settings

1. STATIC_ROOT
   
   - Defailt : None
   
   - collectstatic이 배포를 위해 정적 파일을 수집하는 디렉토리의 절대 경로
   
   - **개발 과정에서 setting.py의 DEBUG 값이 True로 설정되어 있으면 해당 값은 작용되지 않음.**

2. STATICFILES_DIRS
   
   - 앱 폴더 외부에 템블릿이 존재할 때 base.html DIRS에 등록한 것처럼 STATICFILES_DIRS에 static을 등록하는 것.
   
   - **app/static/** 디렉토리 경로를 사용하는 것 외에 추가적인 정적 파일 경로 목록을 정의하는 리스트.

3. STATIC_URL
   
   - 웹 URL ! 
   
   - 로컬에서는 그냥 어떤 파일의 이미지 쓰면 되지만 웹에서는 그렇게 쓸 수 없으니까 웹 URL을 통해 파일에 접근하게 해주는 것 !
   
   - URL로만 존재하는 것 !!

> ### static img 가져오기

1. app\static\articles 경로에 .jpg or .png 같은 이미지 파일 배치하기!
   
   - 오타와 위치 주의

2. 사용할 경로에 tag 달기 !!

****

# Image Upload

> ## Image Field()

- 이미지 업로드에 사용되는 모듈

- 컬럼 값에 **문자열**이 저장이 된다!

> ### FileField()

- FileField(upload_to='', storage=None,)

- setting.py에 MEDIA_ROOT, MEDIA_URL 설정

> ### 위의 필드들을 쓰기 위한 단계들!

1. setting.py에 <mark>MEDIA_ROOT, MEDIA_URL</mark> 설정

2. <mark>upload_to</mark> 속성을 정의하여 업로드 된 파일에 사용할 MEDIA_ROOT의 하위 경로를 지정(선택사항)
   
   > **MEDIA_ROOT**
   
   - Django는 성능을 위해 업로드 파일은 데이터베이스에 저장하지 않는다. 
     
     - 대신, "**파일 경로**"를 저장한다.
   
   - STATIC_ROOT와 다른 경로로 지정해야한다 !
   
   > **MEDIA_URL**
   
   - 주소 / media / 미디어의 경로
   
   - ```py
     MEDIA_URL = '/media/'
     ```
   
   - 


