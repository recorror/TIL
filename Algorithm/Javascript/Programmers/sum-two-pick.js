function solution(numbers) {
  //=========================================
  //     let arr = numbers.sort((a, b)=>a-b)
  //     let result = []
  //     while (arr.length > 1){
  //         let lNum = arr.shift()
  //         for (let i=0; i<=arr.length; i++){
  //             if (arr[i] === undefined){

  //             } else {
  //                 if(!result.includes(lNum + arr[i])){
  //                     result.push(lNum + arr[i])
  //                 }
  //             }

  //         }
  //     }
  // return result
  //===================================================
  // for (let i=0; i<=arr.length; i++){
  //     for (let j=i+1; j<=arr.length; j++){
  //         if (!result.includes(arr[i]+arr[j])){
  //             result.push(arr[i]+arr[j])
  //         }
  //     }
  // }
  // return result
  //==================================================
  const temp = [];
  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      temp.push(numbers[i] + numbers[j]);
    }
  }
  const answer = [...new Set(temp)];
  return answer.sort((a, b) => a - b);
}
