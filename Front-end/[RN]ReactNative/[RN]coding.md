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

---

### chopchop's study

### component 구성

1. 최상단 태그를 `SafeAreaView`로 작성하여 top이나 bottom에 지정한 영역을 침범하지 못하게 한다.

2. 반복되는 component는 map함수를 통해 돌리고 최상단에 key 값을 적어주고 컴포넌트 디자인을 한다.

3. 어떤 양식이 올지 모르기 때문에 일단 가장 기본적은 component인 `View`와 `Text`를 통해 디자인해준다.

4. img의 경우 웹이라면 그냥 img 태그를 썼겠지만 모바일의 경우 `Image` 태그를 react-native에서 import를 해서 써준다.
   
   ```jsx
   <Image
    style="height:50, width:50"
    source={require("../../../../assets/bottom-tab/icon_contact.png")}
   />
   ```
   
   - Image 태그 예시
   - source는 다양한 양식으로 쓸 수 있으니 상황 따라 다르게 쓰거나 convention에 맡게 사용하면 된다.

5. StyleSheet.create에 관하여
   
   ```jsx
   import { StyleSheet } from "react-native";
   export const styles = StyleSheet.create({ container: { flex: 1 } },);
   
   export const styles1 = { container: { flex: 1 } };
   ```
   
   - react-native에서는 styles1처럼 그냥 const styles를 정의하고 바로 사용하는 것도 지원을 한다.
   - 하지만 `StyleSheet.create`를 쓰면 자동 완성이 엄청 짱짱하게 지원된다.
