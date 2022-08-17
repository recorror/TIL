# 패턴 매칭

- 4가지 알고리즘이 있다.
  
  1. 고지식한 패턴 검색 알고리즘
     
     - [Brute Force 웹으로 보기.](http://whocouldthat.be/visualizing-string-matching/)
     
     - naive 가 brute force.
     
     - [tc_1](./String/BruteForce)        [tc_2](./String/BruteForce2)
     
     - 최악의 시간 복잡도 : O(MN)  #  모든 경우의 수를 비교하기 때문!
  
  2. 카프-라빈 알고리즘
  
  3. KMP 알고리즘
     
     - K, M, P 3명의 개발자가 만들었기 때문에 KMP 알고리즘!
     
     - [KMP 웹으로 보기.](http://whocouldthat.be/visualizing-string-matching/)
       
       - KMP 선택해서 봐야함!
     
     - [KMP 알고리즘](./String/KMP_algorithm.py)
     
     - 시간 복잡도 : O(M+N)
  
  4. 보이어-무어 알고리즘
     
     - 오른쪽에서(뒤에서) 왼쪽으로 비교
       
       - 보통 상황에서 문자열은 앞부분보다는 **뒷부분에서 불일치가 일어날 확률이 높다는 성질을 활용**
     
     - 대부분의상용 소프트웨어에서 채택하고 있는 알고리즘
     
     - 보이어-무어 알고리즘은 패턴에 **오른쪽 끝에있는 문자가 불일치**하고 **이 문자가 패턴 내에 존재하지 않는 경우**, **이동 거리는 무려 패턴의 길이만큼이 된다.**

![](String%20-%20패턴매칭_assets/2022-08-12-14-47-21-image.png)

- - - [보이어-무어 알고리즘](./String/boyer_moore.py)

![](String%20-%20패턴매칭_assets/2022-08-12-15-15-23-image.png)



-----

****

### 카이사르 암호

- 시저암호라고도 함.

- 이런게 있다는 것만 알아두면 될 듯
