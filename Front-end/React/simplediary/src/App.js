import { useEffect, useMemo, useRef, useState } from "react";
import "./App.css";
import DiaryEditor from "./DiaryEditor";
import DiaryList from "./DiaryList";
// import LifeCycle from "./LifeCycle";

const App = () => {
  const [data, setData] = useState([]);

  const dataId = useRef(0);

  const getData = async()=>{
    const res = await fetch(
      'https://jsonplaceholder.typicode.com/comments'
      ).then((res)=>res.json())
    
    const initData = res.slice(0,20).map((it)=>{
      return {
        author : it.email,
        content : it.body,
        emotion : Math.floor(Math.random() * 5)+1,
        //Math.random() * 5 = 0~4의 숫자. 실수가 나올 수도 있다.
        //floor를 사용해서 정수로 바꾸어주고 + 1
        created_date : new Date().getTime(),
        id : dataId.current++
      }
    })

    setData(initData)
  }

  useEffect(()=>{
    getData();
  },[])

  const onCreate = (author, content, emotion) => {
    const created_date = new Date().getTime();
    const newItem = {
      author,
      content,
      emotion,
      created_date,
      id: dataId.current
    }
    dataId.current += 1;
    setData([newItem, ...data])
  }

  const onRemove = (targetId) => {
    const newDiaryList = data.filter((it) => it.id !== targetId);
    setData(newDiaryList)
  }

  const onEdit = (targetId, newContent) => {
    setData(
      data.map((it) =>
        it.id === targetId ? { ...it, content: newContent } : it
      )
    )
  }

  const getDiaryAnalysis = useMemo(()=>{
    console.log('일기 분석 시작')

    const goodCount = data.filter((it)=>it.emotion>=3).length
    const badCount = data.length - goodCount
    const goodRatio = (goodCount / data.length) * 100
    return {goodCount, badCount, goodRatio}
  }, [data.length])

  const {goodCount, badCount, goodRatio} = getDiaryAnalysis

  return (
    <div className="App">
      {/* <LifeCycle /> */}
      <DiaryEditor onCreate={onCreate} />
      <div> 전체 일기 : {data.length}</div>
      <div> 기분 좋은 일기 개수 : {goodCount}</div>
      <div> 기분 나쁜 일기 개수 : {badCount}</div>
      <div> 기분 좋은 일기 비율 : {goodRatio}</div>
      <DiaryList onEdit={onEdit} onRemove={onRemove} diaryList={data} />
    </div>
  )
}
export default App;
