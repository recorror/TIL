# Vue Router

> ### Routing

- 네트워크에서 경로를 선택하는 프로세스

- url에 대해 적절한 결과를 응답하는 것.

- Routing in SSR
  
  - server가 모든 라우팅을 통제.

- Routing in SPA/CSR
  
  - 서버는 하나의 HTML만을 제공.
  
  - 비동기로 하면 URL에 대한 이동이 없다. 즉, <mark>하나의 URL</mark>만 가진다.

- 단, 유저의 사용점 관점에서는 서로 다른 URL이 필요하다.

- 또한, URL의 변화가 없다면 브라우저 뒤로 가기 기능을 사용할 수 없음.

> ### Vue Router

- 라우트에 컴포넌트를 매핑한 후 어떤 URL에서 렌더링 할 지 알려줌.

- SPA를 MPA처럼 URL을 이동하면서 사용 가능.

- SPA의 단점 중 하나인 `"URL이 변경되지 않는다."를 해결`

- Vue CLI를 통해 router plugin 반영
  
  - vue add router

- History mode 사용 y - 체크

> ### History mode

- 브라우저의 History API를 활용한 방식 ('/' 이런 식으로 url 찍히게 설정하는 부분.)
  
  - 새로고침 없이 URL 이동 기록을 남길 수 있음.

- [History mode]를 안 쓰면 default 값이 hash mode로 설정된다.

> ### <mark>router-link</mark>

- a 태그와 비슷한 기능 -> URL을 이동시킴.
  
  - router에 등록된 컴포넌트와 매핑됨.
  
  - 히스토리 모드에서 router-link는 클릭 이벤트를 차단하여 a태그와 달리 브라우저가 페이지를 다시 로드하지 않게 한다.

- 목표 경로는 `'to'`속성으로 지정됨.

> ### <mark>router-view</mark>

- url에 대해 일치하는 컴포넌트를 렌더링하는 컴포넌트

- router-link를 클릭하면 routes에 매핑된 컴포넌트를 렌더링.

- router에 emit event를 쓸 때 여기에 써주면 된다. << ???

***

### 선언적 방식 네비게이션

- router-link의 'to' 속성으로 주소 전달.

- 이 때 to에 binding을 통해 url의 name 설정 해둔 것을 바인딩해준다.
  
  ```html
  <router-link :to="{name : '설정해둔 이름'}">이름</router-link>
  ```

### 프로그래밍 방식 네비게이션

- vue 인스턴스 내부에서 라우터 인스턴스에 `$router`로 접근 할 수 있음.

- 다른 URL로 이동하려면 `this.$router.push`를 사용.
  
  - history stack에 이동할 url을 넣는 방식
  
  - history stack에 기록이 남기 때문에 뒤로 가기 버튼을 클릭하면 이전 URL로 이동 가능.

****

### Dynamic Route

- 동적 인자 전달
  
  - URL의 특정 값을 변수처럼 사용할 수 있음.
  
  - `$route.params`로 변수에 접근 가능
    
    ```js
    {
      path: '/url/:variable',
      name: 'boom',
      component: SameBoom
    }
    ```

### lazy-loading (지연 로딩)

- 미리 로딩하는 방식이 아니라 나중에 로딩하는 방식

- 사용자 경험에 따라 첫 화면의 로딩이 너무 오래 걸릴 경우 lazy-loading을 걸어서 첫 로딩을 빠르게 만들어 준다. 그 후 해당 컴포넌트를 불러 올 때 lazy-loading이 되면서 그 때 로딩을 하는 것이다.

****

## Navigation Guard

- vue router를 통해 특정 url에 접근할 때 다른 url로 redirect하거나 해당 url로의 접근을 막는 방법.
  
  - django에서 사용자 인증 없으면 페이지 접근 못하게하거나 로그인 페이지 띄워줬던 거.
1. **전역 가드 (Global Before Guard)**
   
   - 애플리케이션 전역에서 동작
   
   - index.js 에 `router.beforeEach()`를 써줌으로 사용할 수 있다.
   
   - 인자로 (to, from, next)를 받는다.
     
     - to : 이동할 url 정보가 담긴 router 객체
     
     - from : 현재 url 정보가 담긴 router 객체
     
     - next : 지정한 url로 이동하기 위해 호출하는 함수.
       
       콜백 함수 내부에서 반드시 한 번만 호출 되어야 함. 

2. **라우터 가드**
   
   - 특정 url에서만 동작
   
   - 해당 라우터 메서드에서 `beforeEnter()`를 써준다.
   
   - 인자로 (to, from, next)를 받는다.

3. **컴포넌트 가드**
   
   - 라우터 컴포넌트 안에서 동작
   
   - 해당 컴포넌트를 변경하고자 `beforeRouteUpdate()`를 사용해서 처리.
     
     - 컴포넌트 경로만 변경되었을 경우 params 의 변경을 감지하고 처리.

   - 인자로 (to, from, next)를 받는다.

## Articles with Vue

- django에서 만들었던 게시판 만들기

- 구현 기능 : index, create, detail, delete, 404

### [참고]Optional Chaining

- Optional Chaining(?.) 앞의 평가 대상이 undefined나 null이면 에러가 발생하지 않고 undefined를 반환.

### 404 NOT FOUND

- const routes 내부. 즉, 최하단 부에 모든 라우터를 돌고 해당하는 라우터가 없는 경우에 404 not found 페이지를 호출시키자.

- 이 때 형식은 유효한데 특정 리소스를 찾을 수 없는 경우가 있다.
  - 데이터가 없음을 명시하거나
  - 404 not found page로 호출해준다.

****

## UX & UI

- 이용자 측면에서 사용하기 편해야하며, 보기 이뻐야하고, 데이터의 정리가 깔끔하게 되어 있어야한다.

- UI 디자인에 있어 가장 중요한 것은 협업이다.

- UX는 기획자, UI는 디자이너의 역할로 채용하기도 한다.

- 기술은 점점 발전하지만 반대로 유저에 대한 경험은 점점 단순해지고 대중화 되어야한다.

## Software prototyping

- 애플리케이션의 프로토타입을 만드는 것

- 이전까지는 Sketch라는 툴이 굉장히 많이 사용되었지만 지금은 <mark>Figma</mark>가 엄청 쓰여지고 있다.

- 개발만큼이나 충분히 기획과정이 필요하다.

### Figma

- `협업`에 중점을 두면서 ux/ui 설계에 초점을 맞춤.

****

? 협업을 잘 하기위해 어떠한 툴(도구)을 사용해서 할 수 있을까?

****

# 
