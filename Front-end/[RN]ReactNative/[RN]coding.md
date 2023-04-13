### kakao-friend-list

- SafeAreaView
  
  - 안전한 영역에 보장받기 위해 쓰는 것.

- **[react-native-iphone-x-helper](https://github.com/ptelad/react-native-iphone-x-helper)**
  
  - 화면 여백을 맞추기 위한 라이브러리

- react-native-safe-area-context
  
  - x-helper의 개발이 중단이 되어 사용하기 시작한 대체 라이브러리

> **구조분해할당을 사용해서 극한까지 재사용성을 추구하자.**

- ScrollView와 FlatList의 차이
  - 만약 많은 양의 데이터를 가진 리스트를 렌더링할 때는 FlatList를 사용하는 것이 좋다. 그러나 ScrollView는 데이터가 적은 경우나 스크롤링 중첩된 컨텐츠(뷰)를 다룰 때 사용할 수 있다.

### calculator

- SafeAreaView
  
  - 안전한 영역에 보장받기 위해 쓰는 것
  - kakao friend list와 마찬가지로 일단 영역이 상단 바와 하단바 등을 침범하지 않아야 한다.

- 알고리즘 적 로직을 이용해 기능을 구현하면 되서 딱히 필기 안 했음.

### todo

- **dayjs**를 이용해서 날짜 계산.
  
  - 달력을 만들 때 어떤 경우에 어떻게 값이 나올지

- **JSON pretty print** : json date pprint 이용한 것 처럼 정렬 할 때 쓰는 것. (웹)

- 달력 만들 때는 총 35개의 데이터가 들어와야함.
  
  - FlatList에 numColumns를 입력하면 x개만큼 출력하고 다음줄로 넘김. numColumns={7}로 주면 한 줄에 7개씩 출력되는 것.
  
  - 
