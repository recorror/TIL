### Weather app

> ### The Rules of Native

- `app은 웹이 아니다 html이 아니다. div를 쓸 수 없다.`



1. div 대신 View를 쓴다. View는 container다.

2. 모든 text는 `Text component 안에 들어가야 한다.`

3. 웹에서 가지고 올 수 없는 property가 있다.
   
   - ex) border 

4. StyleSheet.create 는 단순한 오브젝트 명령어에 지나지 않는다.
   
   - 다만 super cool한 자동완성 기능을 제공해준다.
