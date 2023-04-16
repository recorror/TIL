### kakao-friend-list

- SafeAreaView
  
  - 안전한 영역에 보장받기 위해 쓰는 것.

- **[react-native-iphone-x-helper](https://github.com/ptelad/react-native-iphone-x-helper)**
  
  - 화면 여백을 맞추기 위한 라이브러리

- react-native-safe-area-context
  
  - x-helper의 개발이 중단이 되어 사용하기 시작한 대체 라이브러리

> ### **구조분해할당을 사용해서 극한까지 재사용성을 추구하자.**

- ScrollView와 FlatList의 차이
  - 만약 많은 양의 데이터를 가진 리스트를 렌더링할 때는 FlatList를 사용하는 것이 좋다. 그러나 ScrollView는 데이터가 적은 경우나 스크롤링 중첩된 컨텐츠(뷰)를 다룰 때 사용할 수 있다.

---

### calculator

- SafeAreaView
  
  - 안전한 영역에 보장받기 위해 쓰는 것
  - kakao friend list와 마찬가지로 일단 영역이 상단 바와 하단바 등을 침범하지 않아야 한다.

- 알고리즘 적 로직을 이용해 기능을 구현하면 되서 딱히 필기 안 했음.

---

### todo

- **JSON pretty print** : json date pprint 이용한 것 처럼 정렬 할 때 쓰는 것. (웹)

- 달력 만들 때는 총 35개의 데이터가 들어와야함.
  
  - FlatList에 numColumns를 입력하면 x개만큼 출력하고 다음줄로 넘김. numColumns={7}로 주면 한 줄에 7개씩 출력되는 것.

> ### onPress입장에서 하나 메서드 입장에서 하나를 작성해서 타고타고 실행되게 하면 가독성 측면에서 좋다.

```jsx
<View onPress={rightButtonClick}>대충 우측 클릭 버튼</View>

const rightButtonClick = () => openModal()
const openModal = () => {
    // 모달 오픈되는 어떤 내용 추가 
}
```

---

### my-gallery

- 광고를 띄우는게 주 목표!
- expo-image-picker를 이용해 내 갤러리에 접근해서  특정 사진 고르기, 빼기 가능.

---

### [NomadWeather](./[RN]Nomad-weather.md)