# CSS Layout techniques

- display, position, **Float, Flexbox, Grid**, etc...



### CSS 원칙 : NORMAL FLOW 인라인, 블록 - 우측, 밑으로 쌓여간다.

- 쌓여간다 = 공간을 차지한다.

> ### Float
> 
> - 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인 요소들이 주변을 wrapping 하도록 함.
> 
> - Float속성
>   
>   - none : 기본값
>   
>   - left
>   
>   - right
> 
> - Normal flow를 지키는 것처럼 보이지만, 노멀 플로우를 벗어난다!
> 
> - clear  : none; <!--플롯 상태-->

> ### Flexbox
> 
> - 행과 열 형태로 아이템들을 배치하는1차원 레이아웃 모델
> 
> - 축
>   
>   - main axis 메인 축
>   
>   - cross axis 교차 축
> 
> - flex-container 는 부모요소에 적용시켜야 한다.
> 
> ### Flex 속성
> 
> - 배치 설정
>   
>   - flex-direction
>     
>     - main 축은 row가 기본 정렬
>     
>     - cross축은 column
>   
>   - flex-weap
> 
> - 공간 나누기
>   
>   - justify-content(main axis)
>     
>     - main axis를 기준으로 공간 배분.
>   
>   - align-content(cross axis)
> 
> - 정렬
>   
>   - align-items(모든 아이템을 cross axis 기준으로)
>   
>   - align-self
> 
> ### Flex에 배치되는 순서
> 