# User model

> ### AUTH_USER_MODEL

- 프로젝트에서 User를 나타낼 때 사용하는 모델.

- 모델을 만들고 마이그레이션을 해버린 후에는 변경할 수 없음.

- 대체하기 == User Custom 준비.
  
  1.  models.py에 User 모델을 정의한다.
     
     ```python
     from django.db import models
     from django.contrib.auth.models import AbstractUser
     # models.py
     class User(AbstractUser):
         pass
     ```
  
  2. settings.py에 AUTH_USER_MODEL 지정
     
     ```python
     #settings.py
     AUTH_USER_MODEL = 'accounts.User'
     ```
  
  3- accounts/admin.py에 커스텀 User 모델을 등록 (선택사항)
     
     ```python
     from django.contrib import admin
     from django.contrib.auth.admin import UserAdmin
     from .models import User
     
     # accounts/admin.py
     admin.site.register(User, UserAdmin)
     ```

- AbstractUser = "관리자 권한과 함께 완전한 기능을 가지고 있는 User model을 구현하는 추상 기본클래스"

- Auth User Model은 중간 변경 권장 x **처음에 하자.**

- Django는 User모델을 설정하는 것을 강력하게 권장한다. 기본 User모델과 동일하게 작동하면서도 원하는대로 설정할 수 있기 때문.

****

> ### Cookies

- 요청과 응답에 의해 작동하는 기본적인 프로토콜

- **HTTP 특징**
1. 비 연결 지향.
   
   - 서버는 요청에 대한 응답을 보낸 후 연결을 끊음.

2. 무상태
   
   - 연결을 끊는 순간 클라이언트와 서버의 통신이 끝남.

3. 이러한 끊긴 연결 속에서 상태가 있느 세션을 만드는 것이 쿠키Cookies

> **Cookies**

- 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각이다.

- 사용자의 컴퓨터에 설치되는 작은 기록 정보 파일
  
  - key-value의 데어터 형식으로 저장.
  
  - 이렇게 저장해 놓았다가, 동일한 서버에 재요청 시 저장된 쿠키를 함께 전송

- 쿠키는 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때 주로 사용됨.
  
  - 이를 이용해 사용자의 로그인 상태를 유지할 수 있음.
  
  - 상태가 없는 HTTP프로토콜에서 상태 정보를 기억 시켜 주기 때문.

> **쿠키 사용 목적**

1. 세션 관리
   
   - 로그인, 아이디 자동완성, 공지 하루 안 보기, 팝업체크, 장바구니 등의 정보 관리

2. 개인화
   
   - 테마 등의 설정

3. 트래킹
   
   - 사용자 행동을 기록 및 분석

> **세션 Session**

- 클라이언트가 서버에 접속하면 session id를 쿠키에 저장.

- 세션이 살아있는한 쿠키를 계속 서버에 전달 할 수 있다. 때문에 state(상태)가 유지 됨.

> **쿠키의 수명**

- 현재 세션이 종료되면 삭제됨.

- 브라우저 종료와 함께 세션이 삭제됨. ex) swea

- Persistent cookie
  
  - 일정 기간이 지나야 사라지는 쿠키.

> **session in django**

- Django는 database-backed sessions 저장 방식을 기본 값으로 사용.
  
  - Django DB의 django_session 테이블에 저장
  
  - 설정을 통해 다른 저장방식으로 변경 가능.

- session 메커니즘에 대부분을 생각하지 않아도 되게 대부분 처리해준다.

----

### Authentication in Web requests

> ### 개요

- Django가 제공하는 인증 관련 built-in forms 익히기.

> ### AuthenticationForm

- 데이터가 유효한지 검증.

- request를 첫번째 인자로 취함.

> ### login()

- login(request, uset, backend=None)

- 인증된 사용자를 로그인 시키는 로직으로 view함수에서 사용됨.

- httpRequest 객체와 User 객체가 필요
  
  **views.py**
  
  ```python
  from django.shortcuts import render, redirect
  from django.contrib.auth.forms import AuthenticationForm
  from django.contrib.auth import login as auth_login
  
  
  def login(request):
      if request.method == 'POST':
          # 첫번째 인자 request, 두번째 인자 data=request.POST
          form = AuthenticationForm(request, request.POST)
          if form.is_valid():
              #로그인, 세션 아이디 만들어줌.
              auth_login(request, form.get_user)
              return redirect('articles:index')
      else:
          form = AuthenticationForm()
      context = {
          'form':form,
      }
      return render(request, 'accounts/login.html', context)
  ```

> ### get_user()

- 유효성 검사를 통과했을 경우 로그인 한 사용자 객체를 반환.

> ### logout()

- logout(request)

- HttpRequest 객체를 인자로 받고 **반환 값이 없음.**

- 로그인하지 않은 경우 오류를 발생시키지 않음.
  
  1. 현재 요청에 대한 session data를 DB에서 삭제
  
  2. 클라이언트의 쿠키에서도 sessionid를 삭제

# 회원가입

> ### 개요

> ### UserCreationForm

- 주어진 username과 password로 권한이 없는 새 user를 생성하는 ModelForm

- 3개의 필드를 가짐
  
  1. username
  
  2. password1
  
  3. password2

----

# Custom user & Built-in auth forms

> ### AbstractVaseUser의 모든 subclass와 호환되는 forms

- 아래 Form 클래스는 User 모델을 대체하더라도 커스텀 하지 않아도 사용가능
  
  1. AuthenticationForm
  
  2. SetPasswordForm
  
  3. PasswordChangeForm
  
  4. AdminPasswordChangeForm

- 기존 User 모델을 참조하는 Form이 아니기 때문

> ### 커스텀 유저 모델을 사용하려면 다시 작성하거나 확장해야 하는 forms

1. UserCreationForm

2. UserChangeForm
   
   - 둘 모두 Meta가 기존 유저를 베이스로 한다. 반드시 커스텀(확장)해야함.
     
     **form.py**
     
     ```python
     from django.contrib.auth import get_user_model
     from django.contrib.auth.forms import UserCreationForm, UserChangeForm
     
     class CustomUserCreationForm(UserCreationForm):
     
         class Meta(UserCreationForm.Meta):
             model = get_user_model()
     
     class CustomUserChangeForm(UserChangeForm):
         class Meta(UserChangeForm.Meta):
             model = get_user_model()
     ```

> ### get_user_model()

- "현재 프로젝트에서 활성화된 사용자 모델"을 반환

- 직접 참조하지 않는 이유
  
  - 예를 들어 : 기존 User모델이 아닌 User 모델을 커스텀 한 상황에서는 커스텀 User 모델을 자동으로 반환.

----

> ### 탈퇴 !

```python
#회원탈퇴
def delete(request):
    request.user.delete()
    #auth_logout(request)
    return redirect('articles:index')
```

---

> ### 회원정보 수정

- UserChangeForm 사용 시 문제점

- 일반 사용자가 접근해서는 안 될 것들까지 접근가능했다.
  
  - 때문에 fields를 재 정의 해주었다.
    
    ```python
    class CustomUserChangeForm(UserChangeForm):
        class Meta(UserChangeForm.Meta):
            model = get_user_model()
            fields = ('email', 'first_name', 'last_name',)
    ```

---

> ### 비밀번호 변경

- 
