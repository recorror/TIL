## Weather app

> ### The Rules of Native

- `app은 웹이 아니다 html이 아니다. div를 쓸 수 없다.`
1. div 대신 View를 쓴다. View는 container다.

2. 모든 text는 `Text component 안에 들어가야 한다.`

3. 웹에서 가지고 올 수 없는 property가 있다.
   
   - ex) border

4. StyleSheet.create 는 단순한 오브젝트 명령어에 지나지 않는다.
   
   - 다만 super cool한 자동완성 기능을 제공해준다.

---

> ### Layout System

- mobile에서 flexDirection의 기본 값은 column이다.
  
  - web에서는 기본 값이 row이다.

- mobile은 스크린 사이즈가 천차만별이라 responsive 한 디자인을 해야한다.
  
  - 아바타나 캐릭터와 같은 경우는 pixel을 기반으로 강제로 사이즈를 줄 수도 있다.
  
  - 부모 컴포넌트에 flex 사이즈를 1로 준다.
    
    - 해당 컴포넌트 이외의 다른 컴포넌트가 없다면 해당 컴포넌트의 크기가 화면에 꽉 찰 것.
    
    - 하위 컴포넌트 3개에 각각 flex 1을 준다면 상위 컴포넌트의 1의 크기를 3분의 1씩 가져간다. 즉, 하위 컴포넌트에서의 flex는 비율을 뜻한다.
    
    ```jsx
    import { StatusBar } from "expo-status-bar";
    import React from "react";
    import { StyleSheet, Text, View } from "react-native";
    import { View } from "react-native";
    
    export default function App() {
      return (
        <View style={styles.container}>
          <Text style={styles.text}>Hello</Text>
          <StatusBar style="dark" />
        <View style={{ flex: 1, flexDirection: "row" }}>
          <View style={{ flex: 1, backgroundColor: "tomato" }}></View>
          <View style={{ flex: 1, backgroundColor: "teal" }}></View>
          <View style={{ flex: 1, backgroundColor: "orange" }}></View>
        </View>
      );
    }
    
    const styles = StyleSheet.create({
      container: {
        flex: 1,
        backgroundColor: "white",
        alignItems: "center",
        justifyContent: "center",
      },
      text: {
        fontSize: 28,
        color: "black",
      },
    });
    ```
    
    - 이 경우 tomato, teal, orange가 33.33%p 씩 즉 1:1:1의 비율로 영역을 차지한다.

> # 
