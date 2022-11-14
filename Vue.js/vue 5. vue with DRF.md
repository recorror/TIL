# DRF

****

### server, client

- server와 client간의 요청과 응답.
  - ex) django REST => POSTMAN

- Server
  - 클라이언트에게 `정보`와 `서비스`를 제공하는 컴퓨터 시스템
  - 서비스 전체를 제공 == Django Web Service
  - 정보를 제공 == DFG API Service

- Client
  - `Server가 제공하는 서비스에 적절한 요청`을 통해 `Server로부터 반환 받은 응답을 사용자에게 표현`하는 기능을 가진 프로그램 혹은 시스템

- 적절한 요청을 보내면 JSON 파일과 같은 적절한 응답을 해준다.
  - 잘못된 요청의 예 ) 모델 title 정의 해놓고 요청을 name 이런식으로 하면 안 된다.

****

## Cross-Origin Resource Sharing

### SOP ( Same - Origin Policy)

- "동일 출처 정책"

### Origin

- `URL의 Protocol, Host, Port를 모두 포함`하여 출처라고 부른다.

### CORS - 교차 출처 리소스 공유

- 추가 `HTTP Header`를 사용하여, 특정 출처에서 샐행 중인 웹 어플레 케이션이 `다른 출처의 자원에 접근할 수 있는 권한`을 부여하도록 브라우저에 알려주는 체제.

- 다른 출처지만 접근해도 된다는 사실을 알려야 한다.

- "교차 출처 리소스 공유 정책"

### CORS policy - 교차 출처 리소스 공유 정책

- 다른 출처의 리소스를 불러오려면 그 출처에서 `올바른 CORS header`를 포함한 응답을 반환해야 한다.

- HOW TO SET `CORS`
  - Access-Control-Allow-Origin

- django-cors-headers library 사용하기.

****

# DRF Auth System

## Authentication - 인증, 입증

- 모든 보안 프로세스의 첫 번째 단계, 사용자가 누구인지 확인하는 과정.

- 401 Unauthorized
  - 사용자 인증이 되지 않았음.

### Authorization - 권한 부여, 허가

- 사용자에게 특정 리소스 또는 기능에 대한 액세스 권한을 부여하는 과정

- 보안 환경에서 권한 부여는 항상 인증이 먼저 필요함.
  - 엑세스 권한 부여 이전에 자신의 ID를 먼저 확인 하는 것.

- 인증이 되었어도 모든 권한을 부여 받는 것은 아님.

- 403 Forbidden
  - 401과 다른 점은 서버는 클라이언트가 누구인지 알고 있음.

### Authentication and authorization

- 세션, 토근, 제 3자를 활용하는 등의 다양한 인증 방식이 존재한다.

### DRF 기본 제공 인증방식

> <mark>TokenAuthentication</mark>

- settings.py에 작성하여야 할 설정!!

### 다양한 인증방식

- BasicAuthentication
  - 가장 기본적인 수준의 인증방식
  - 테스트에 적합

- SessionAuthentication
  - Django에서 사용하였던 session 기반의 인증 시스템
  - DRF와 Django의 session인증 방식은 보안적 측면을 구성하는 방법에 차이가 있음

- RemoteUserAuthentication
  - Django의 Remote user 방식을 사용할 때 활용하는 인증 방식

- TokenAuthentication
  - 매우 간단하게 구현 할 수 있음
  - 기본적인 보안 기능 제공
  - 다양한 외부 패키지가 있음