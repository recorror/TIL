# 동기와 비동기

### 동기

- 모든 일을 순서대로 하나씩 처리하는 것.

- Python 코드가 동기식 처리이다. (위에서부터 순서대로)

- 요청과 응답을 동기식으로 처리한다면?
  
  - 응답을 계속 기다려야함...!

## 비동기

- 작업을 시작한 후 결과를 기다리지 않고 다음 작업을 처리. (병렬적 수행)

- ex) 메일전송을 누르면 사용자는 목록 탭으로 돌아가 다른 것을 바로 할 수 있지만 뒤에선 메일 전송을 위한 프로그램이 돌아가고 있는 것이다.

### JavaScript의 비동기 처리

- Single Thread 언어, JavaScript

- JS는 한 번에 하나의 일만 수행할 수 있는 Single Thread 언어라 동시에 여러 작업을 처리할 수 없음.

- 어떻게 JS가 Single Thread를 해결했을 까.
  
  - 특정 언어가 동작할 수 있는 환경 = "Runtime"

> 비동기 처리 동작 방식

1.  Call Stack

2. Call Stack -> Web API

3. Web API 처리 끝나면 Call Stack이 아니라 Task Queue 에 순서대로 들어간다.

4. Event Loop가 Call Stack이 빈다면 Task Queue에서 Call Stack으로 넣는다.
   
   - setTimeout으로 0으로 지정을 한다고 치면 0초 뒤에 출력하는 것이 아니라 다른 것들을 처리 한 후 지연된 setTimeout으로 지정한 코드가 실행되는 것이다.

### Axios

- cdn이 필요하다.

- request.get()처럼 axios.get() 이런 식으로 쓰면 됨.
  
  ```html
  <script>
      axios.get('요청할 url')
          .then(성공하면 수행할 콜백함수)
          .catch(실패하면 수행할 콜백함)
  </script>
  ```

![](JavaScript%20심화비동기와동기_assets/2022-10-26-09-48-03-image.png)

### 비동기 처리의 단점.

- 작업이 완료되는 순서에 따라 처리

- 즉, 실행결과를 예상하면서 코드를 작성할 수 없게 함.
  
  - 해결 방법 : 콜백 함수를 쓰자.

### 콜백함수

- 다른 함수의 인자로 전달되는 함수

- 비동기 작업이 완료된 후 실행할 작업을 명시하는데 사용 됨.
  
  - ex) addEventListener, views 등등등

- 특정한 조건 혹은 행동에 의해 호출되도록 작성할 수 있음.

- 즉, 비동기 처리를 순차적으로 동작할 수 있게 함.

> 다만, 비동기 작업이 여러개일 경우

### 콜백지옥

- 콜백함수로 순서를 정하다가 너무 많은 것의 순서를 정하려다가 생기게 되는 문제점.

### 프로미스

- 비동기 작업의 완료 또는 실패를 나타내는 객체

> then과 catch

- then(callback)
  
  - 요청한 작업이 성공하면 callback 실행
  
  - 이전 작업의 성공 결과를 인자로 전달 받음.

- catch(callback)
  
  - then()이 하나라도 실패하면 callback 실행
  
  - 이전 작업의 실패 객체를 인자로 전달 받음.
  
  - 왜 실패에대한 정보!

- then과catch모두 항상 promise 객체를 반환
  
  - 즉, 계속 chaining을 할 수 있다.
  
  - 기존 콜백(콜백 지옥) vs promise 방식의 차이
  
  ![](JavaScript%20심화비동기와동기_assets/2022-10-26-10-22-44-image.png)


