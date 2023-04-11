# Vue CLI

***

## ❄Node.js

- 자바스크립트를 구현하기 위한 런타임 환경 Node.js

### NPM

- node js의 기본 패키지 관리자.

- python의 pip 같은 존재.

****

## ♻Vue CLI

- vue개발을 위한 표준 도구.

- 프로젝트의 구성을 도와주는 역할. (다양한 tool 제공)

```cmd
# 전역에 설치하여야 함 
$ npm install -g @vue/cli
```

```
vscode gitbash
$ vue create vue-cli
=> vue2 선택!
```

- git bash는 인터렉티브 쉘이 아니기 때문에 vscode에서 쳐줘야한다!

****

## ❄node_modules

- 환경을 담당하는 모듈.

- python의 venv와 비슷한 역할을 함.
  
  - 즉, gitignore 필요. ( 프로젝트 생성시 자동 추가 된다. )

- 의존성 깊이가 매우 깊다. => left-pad라는 사건이 발생하게 된다.

### node_modules-Babel

- `JavaScript compiler`

- 최신 코드를 구버전으로 변환 해주는 도구.

- 파편화 표준화의 영향으로 과거 버전들의 스펙트럼이 매우 다양하다.
  
  - 버전에 따른 같은 의미의 다른 코드를 작성해야하는 것을 해결하기 위한 도구.

### node_modules-Webpack

- `static module bundle`

- 모듈 간의 의존성 문제를 해결하기 위한 도구.

- 내부적으로 종속성 그래프를 디자인한다.

> Module
> 
> - 애플리케이션의 크기가 커지고 복잡해지면서 파일 하나에 모든 기능을 담기가 어려워짐.
> 
> - 이때 파일을 여러개로 나누어 관리하기 시작하면서 모듈로 분화.
> 
> - 그런데? 모듈의 수도 많아지며 모듈 간의 의존성이 깊어졌다.
> 
> Bundler
> 
> - Webpack은 Bundler 중에 하나.
> 
> - 다양한 Module의 의존성 문제를 해결해주기 위한 것.

****

### 🦕deno

- Node.js 설계자인 라이언 달이 새로 만든 Js Ts용 런타임 서비스.

- `but, 기존의 시장에 끼어드는 것은 아직 멀었다.`

****

## ❄Vue CLI 프로젝트 구조

- public/index.html
  
  - vue앱의 뼈대가 되는 html

- src/
  
  - src/assets : 정적 파일을 저장하는 디렉토리
  
  - src/components : 하위 컴포넌트들이 위치
  
  - src/app.vue : 최상위 컴포넌트. index.html과 연결된다.
  
  - src/main.js : 시작할 때 app과 index 연결하는 부분.

### 🔥Component

- 기능별로 분화한 코드 조각

- CS에서는 다시 사용할 수 있는 범용성을 위해 개발된 소프트웨어 구성 요소

- app을 구성할 때 중첩된 컴포넌트들의 tree로 구성하는 것이 보편 적이다.

- 컴포넌트는 유지보수를 쉽게 만들어준다.

### SFC (Single File Component)

- component in Vue
  
  - new Vue() << 이거 자체가 컴포넌트라고 불 수있다.

- 컴포넌트는 기능 단위로 작성하는 것이 핵심이다.

### Vue component 구조 정리.

- 컴포넌트들이 tree 구조를 이루어 하나의 페이지를 만듦  

- root에 해당하는 최상단의 component가 App.vue

- 이 App.vue를 indenx.html과 연결

- 결국 index.html 파일 하나만을 rendering
  
  - 이게 바로 SPA(Single Page Application)

### 1️⃣Component 만드는 순서

1. component.vue 파일 만들기
   
   - component 안에 vue 파일 생성

2. script에 name 등록하기
   
   - script 내부의 export default (new Vue()역할)
   
   - name에 등록 이 때 파일 이름과 달라도 상관없으나 굳이 다를 이유가
     없기 때문에 파일 이름과 같게 생성해준다.

3. template에 최상위 태그 하나 달아주기.
   
   - template의 경우 태그가 있는걸로 취급이 되지 않기 때문에 다른 태그를 하나 달아주어야 오류가 나지 않는다.

### 2️⃣Component 등록 3단계

1. 불러오기

2. 등록하기

3. 보여주기

****

## 🔥Data in components

- 동적 웹페이지에서 같은 페이지 내에서 오만 데이터를 공유 한다.
  
  - but, 여러 component로 구분이 되어있다.

- MyComponent에 정의된 data를 MyChild에서 사용하려면 어떻게 해야할까.

- 완전히 동일한 data를 서로 다른 component에서 보여주려면 어떻게 해야 할까?

- 컴포넌트는 부모-자식 관계를 가지고 있으므로 부모, 자식 관계에서만 데이터를 주고받게 하자.
  
  - 데이터의 흐름을 파악하기 용이
  
  - 유지 보수하기 쉬워짐.

> **pass props & emit event**
> 
> 부모 => 자식으로의 데이터의 흐름
> 
>     pass props 방식
> 
> 자식 => 부모로의 데이터의 흐름
> 
>     emit event의 방식

### pass props

- 속성을 사용하여 데이터 전달.

- props는 부모 컴포넌트의 정보를 전달하기 위한 사용자 지정 특성.

- 부모에서 넘겨주는 props
  
  - kebab-case

- 자식에서 받는 props
  
  - camelCase

- 부모 템플릿에서 넘긴 변수를 자동으로 kebab => camel으로 변환해준다.

### dynamic props

- 변수를 props로 전달할 수 있음.

- v-bind directive를 사용해 데이터를 동적으로 바인딩.

- 부모 컴포넌트의 데이터가 업데이트 되면, 자식 컴포넌트로 전달되는 데이터 또한 업데이트 됨.

### 단방향 데이터 흐름

- 모든 props는 부모에서 자식으로 즉, 아래로 `단방향 바인딩`을 형성.

- 부모 속성이 업데이트 되면 자식도 업데이트 되지만 반대 방향은 아니다.

- 목적
  
  - 원본 데이터를 바꾸지 않게하기 위함.
  
  - 앱의 데이터 흐름을 이해하기 쉽다. (무조건 위에서 아래로 흐르기 때문이다.)

- 하위 컴포넌트에서 prop을 변경하려고 시도하면 vue는 콘솔에서 경고를 출력한다.

### Emit Event

- 부모 컴포넌트에서 자식 컴포넌트로 데이터를 전달할 때는 `이벤트를 발생 시킴.`
  
  1. 데이터를 이벤트 리스너의 콜백함수의 인자로 전달.
  
  2. 상위 컴포넌트는 해당 이벤트를 통해 데이터를 받음.

- 기본 흐름 정리
  
  ```html
  <!--정적 데이터 전달 흐름-->
  methods: {
      XD: function () {
      this.$emit('x-d', '정적 데이터')
  }
  }
  ```
  
  1. 자식 컴포넌트에 있는 버튼 클릭 이벤트를 청취하여 연결된 핸들러 함수(childToParent )호출
  
  2. 호출된 함수에서 $emit 을 통해 상위 컴포넌트에 이벤트(child-to-parent) 발생
  
  3. 상위 컴포넌트는 자식 컴포넌트가 발생시킨 이벤트를 청취하여 연결된 핸들러 함수(parentGetEvent)를 호출.

- emit with data 흐름 정리
  
  ```html
  <!--동적 데이터 전달 흐름-->
  methods: {
      XD: function () {
      this.$emit('x-d', this.dataValue)
  }
  }
  ```
  
  1. 자식 컴포넌트에 있는 버튼 클릭 이벤트를 청취
  
  2. 호출된 함수에서 emit을 통해 데이터를 전달
  
  3. 청취, 행들러 함수 호출, 함수의 인자로 전달된 데이터
  
  4. 호출된 함수에서 \`${인자}` 형태로 csl 찍어보자.

> - 자식 => 부모 전달 === 이벤트 발생
>   
>   - 이벤트에 데이터를 담아 전달
> 
> - 부모 => 자식 청취 === @
>   
>   - 전달받은 데이터는 이벤트 핸들러 함수의 인자로 사용

> HTML에서 쓴다 kebab-case
> 
> JavaScript에서  camelCase
> 
> - props
>   
>   - 상위 => 하위 = kebab-case
>   
>   - 받을 때는 camelCase
> 
> - emit
>   
>   - HTML 요소가 이벤트를 청취함 : kebab-case
>   
>   - 메서드, 변수명 등은 JavaScript에서 사용함 : camelCase