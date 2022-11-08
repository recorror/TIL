# Vuex

- 상태관리 툴

> ### State management
> 
> - 상태란 ? `현재에 대한 정보 (data)`
> 
> - 현재 `App이 가지고 있는 data`로 표현할 수 있음!
> 
> - 여러 개의 component로 하나의 app을 만들고 있다. 즉, `여러 개의 component를 같은 상태로 유지할 필요`가 있음.
> 
> - props, emit event로 상태 관리를 할 수 있지만 깊이가 깊을 수록 데이터 전달이 쉽지 않다. 이 때 모든 컴포넌트에서 공통적으로 쓸 수 있는 `중앙 저장소에 데이터를 모아서 상태를 관리`할 수 있다.

> ### Vuex
> 
> - 상태관리 + 라이브러리
> 
> - 규칙을 설정하며, `Vue의 반응성을 효율적으로 사용하는 상태 관리 기능`을 제공.

****

## Vuex 시작하기

```cmd
//vue 프로젝트 생
$ vue create vuex-app

//디렉토리 이동하
$ cd vuex-app

// vue CLI를 통해 vuex plugin 적용
$ vue add vuex
```

### Project with vuex

- src / store / index.js가 생성됨.

- vuex의 핵심 컨셉 4가지
  
  - **state**
    
    - `중앙에서 관리하는 모든 상태 정보`. vue의 data와 같은 역할.
    
    - `$store.state`로 state데이터에 접근
    
    - state의 데이터가 변화하면 해당 데이터를 사용(공유)하는 component도 자동으로 다시 렌더링 된다.
  
  - **mutations**
    
    - `실제로 state를 변경하는 유일한 방법`
    
    - mutations에서 호출되는 핸들러(handler)함수는 반드시 `동기적`이어야한다.
      
      비동시 로직으로 mutations를 사용해서 state를 변경하는 경우, state의 변화 시기를 특정할 수 없기 때문이다.
    
    - (state, data) 첫번째 인자로 state를 받고 data는 내 입력값.
      
      component 혹은 actions에서 `commit()메서드로 호출`됨.
  
  - **actions**
    
    - 비동기 작업이 포함될 수 있는 methods
    
    - state를 직접 변경하지 않고 commit()메서드로 mutations를 호출해서 state를 변경한다.
    
    - component에서 `dispatch()메서드에 의해 호출`됨.
  
  - **getters** (새로운 변수 값)
    
    - computed처럼 동작한다.
    
    - `계산된 값을 얻기위해 쓴다`. 즉, return 필수.
    
    - 첫번째 인자로 state, 두번째 인자로 getter를 받는다.

****

> component에서 데이터를 조작하기 위한 데이터의 흐름
> 
> - component => (actions) => mutations => state
> 
> component에서 데이터를 사용하기 위한 데이터의 흐름
> 
> - state => (getters) => component

****

### Vue와 vuex 인스턴스 비교

![](vue%203.%20vuex_assets/2022-11-08-09-35-18-image.png)

### Mutations & Actions

![](vue%203.%20vuex_assets/2022-11-08-09-47-46-image.png)

****

## Lifecycle Hooks

- 각 인스턴스의 생성과 소멸의 과정 중 단계별 초기화 과정이 있음.
  
  - vue 인스턴스가 생성된 경우
  
  - 인스턴스를 dom에 마운트하는 경우
  
  - 데이터가 변경되어 dom을 업데이트하는 경우 (update, delete 등)

- 각 단계가 트리거가 되어 특정 로직을 실행할 수 있음.

![Component lifecycle diagram](https://vuejs.org/assets/lifecycle.16e4c08e.png)

- lifecycle의 순서도

- method로 정의해서 사용하면 된다.

### created

- Vue instance가 생성된 후 ! 막 사용할 준비가 된 느낌.

- data, computed등의 설정이 완료된 상태.

- 서버의 값을 받아서 초기화하고 싶을 때

- mount되지 않아 dom 관련 동작은 할 수 없음. (class 변경, setAttribute로 html의 속성을 바꾸고 싶다거나 이러한 부분.)

### mounted

- dom과 연결이 마무리 된 부분.

- class 변경, setAttribute로 html의 속성을 바꿀 수 있다.

### updated

- 데이터가 변경되어 DOM에 변화를 줄 때 호출됨.

- ~~화면 수정을 하고 싶다고 updated에 준다면 update => updated => update 등의 무한루프에 빠질 수도 있다.~~
