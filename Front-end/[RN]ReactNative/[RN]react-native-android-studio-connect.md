### react native - android studio 연동하기

1. 둘 다 설치해준다.
   
   - react native (in vscode)
   
   - android studio

2. 버전에 맞는 jdk 설치. (나는 java se 11)

3. 환경변수 편집 해준다.
   
   - ANDROID_PATH 설정 (안드 스튜디오에서 SDK 편집 부분에서 주소 복사해서 붙여줌)
   - JAVA_PATH 설정 (c://programfile/java/[자신의 jdk 버전 폴더])

4. 안드 스튜디오에서 VDM 혹은 DM 클릭 후 재생해준다.

5. 안드 스튜디오에서 배쉬창 두 개를 띄워 각각의 배쉬창에 아래의 명령어를 입력해준다.
   
   - npx react-native start
   - npx react-native run-android

6. 안드로이드 기기가 화면상에 나타나면 성공.

7. 그 후 react native를 실행해준다. start를 해주면 자동으로 연결됨.

**ps.** react-native-cli가 아니라 expo-cli로 만든 것도 연결이 됐는데 왜 그런건지는 잘 모르겠음. 이 때 react-native-cli로 만든 프로젝트를 먼저 실행해서 연동이 된 후에 expo-cli를 실행해서 된 것 같기도 함. 후에 expo-cli로만 실행해볼 필요성이 있음.