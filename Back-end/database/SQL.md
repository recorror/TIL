- SELECT 도출해낼 거
- FROM 어디껄 기준으로
- WHERE 조건이나 연산식 같은거 쓸 때
- ORDER BY (기준이 될 줄 선택) ASC/DESC (오름차순 내림차순)

- 보통 WHERE 뒤에 씀
![[Pasted image 20231211132700.png]]
- value 기술 방법
- 문자열은 '(싱글쿼트)로 둘러싸는 'sample'
- 날짜는 TO_DATE로 서식을 명시한다 TO_DATE('2012/03/31', 'yyyy/mm/dd')
  
  문제 F) 全従業員の名前、給与、手当、総給与（給与+手当）
  - select ename 名前, sal 給与, COALESCE(comm, 0) 手当, (sal + COALESCE(comm, 0)) 総給与 from emp order by 総給与 desc
  문제G）全従業員の職業、名前を１項目に結合して表示 （例えば　 "PRESIDENT - SCOTT" ）
  - select concat(concat(job, ' - '), ename) "職務 ＋ 名前" from emp order by empno asc

  A) 部署番号ごとの従業員数
  - a

  B) 社長以外の職種ごとの給与の平均
  - select job, round(avg(sal), 2) 給与の平均 from emp where job != 'PRESIDENT' group by job order by 給与の平均

  C) 職種、職種ごとの最高給与額、その職種の人数を、最高給与額の高い順に表示
最高給与額が同じ場合は、職種を名称の昇順とすること
  - select job 職種, max(sal) 最高給与額, count (*) 職種の人数 from emp group by job order by 最高給与額 desc

  D) 職種ごとの給与平均、但し給与平均が3000以上を除く
  - select job 職務, round(avg(sal)) 給与平均 from emp group by job having avg(sal) < 3000 order by 職務 asc

---
A) 従業員全員の、氏名、所属部署番号、部署名を表示
- select emp.ename 氏名, emp.deptno 所属部署番号, dept.dname 部署名 
	from emp 
	inner join dept 
	on emp.deptno = dept.deptno 
	order by empno asc
- select e.ename 氏名, e.deptno 所属部署番号, d.dname 部署名 
	from emp e 
	inner join dept d 
	on e.deptno = d.deptno 
	order by empno asc;
B) 部署名、所属部署番号、氏名を、部署名昇順、氏名昇順に表示。従業員がいない部署も表示すること
- select d.dname 部署名, d.deptno 所属部署番号, e.ename 氏名 
	from dept d 
	left join emp e 
	on e.deptno = d.deptno 
	order by 部署名 asc, 氏名 asc;
C) シカゴに勤務している従業員を、部署名、部署番号、氏名で表示する
- select d.dname 部署名, d.deptno 部署番号, e.ename 氏名 
	from dept d 
	left join emp e 
	on e.deptno = d.deptno 
	where d.loc = 'CHICAGO' 
	order by 氏名 asc;
D) 従業員全員の従業員番号と名前、その上司の従業員番号と名前を表示する
- select e.empno 従業員番号, e.ename 名前, e.mgr 上司の従業員番号, m.ename 上司の名前 
	from emp e 
	left join emp m
	on e.mgr = m.empno
	order by e.mgr asc;
- *EMP에서 또 다른 사람의 EMP가 필요한 거니까 새로운 emp를 참조하도록 하면 된다.

①従業員の従業員番号、氏名、給与、同額の給与を得ている従業員数
- select e.empno 従業員番号, e.ename 名前, e.sal 給与, (select count(*) from emp p where e.sal = p.sal) 
	from emp e 
	order by empno asc;

②全従業員の平均給与以上を支給されている従業員
- select * from emp e
	where e.sal >= (select avg(m.sal) from emp m)
	order by e.sal asc;

### ストアド（PL/pgSQL）
- posgreSQL 데이터베이스상의 프로그래밍
- DB상에서 실행하는 데이터 처리에 특화된 프로그램, SQL에서는 실현할 수 없는 프로그래밍을 할 수 있다(고속화)
- 업무 로직을 DB상에 실장함으로써 UI와 분리가 용이함(모듈화)
- UI가 어떤 언어, 어떤 OS, 실행 환경에서도 영향을 받지 않는다(이식성)

#### 트리거
- 테이블 레코드에 '편집' '추가' '삭제' 등 지정한 처리가 있을 때 자동으로 호출되는 PL/pgSQL
<용도 예>
- 데이터의 변경 이력을 자동으로 로그 테이블에 추가하도록, 「편집」 「추가」 「삭제」트리거를 작성.
- 레코드에 갱신 일시나 갱신자 IP 필드가 있지만, 이것들은 본래의 데이터 처리(비즈니스 로직)에는 불필요한 정보이다. 갱신 일시나 갱신자 IP의 갱신은 비즈니스 로직에서는 고려하지 않고, 「추가」 「편집」트리거를 작성하여 DB로 자동 세팅시킨다.
- 부모 테이블 레코드 삭제 시 관련 아이 테이블의 아이 레코드를 삭제한다.
- ex) 12시가 되면 데이터가 초기화되어 다음 날 쉽게 작업하는 것이 가능하게 된다거나 하는 것.


