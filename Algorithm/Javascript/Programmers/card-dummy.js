function solution(cards1, cards2, goal) {
  // let cnt = 0
  // for (let i=0; i<goal.length; i++) {
  //     if (cards1.includes(goal[i])) {
  //         cnt++
  //         // cards1.replace(goal[i], '')
  //     } else {
  //         if (cards2.includes(goal[i])) {
  //             cnt++
  //             // cards2.replace(goal[i], '')
  //         }
  //     }
  // }
  // return cnt == goal.length ? 'Yes' : 'No';
  let cnt = 0;
  for (let i = 0; i < goal.length; i++) {
    if (cards1.length > 0 && cards1[0] === goal[i]) {
      cnt++;
      cards1.shift();
    } else {
      if (cards2.length > 0 && cards2[0] === goal[i]) {
        cnt++;
        cards2.shift();
      }
    }
  }
  return cnt == goal.length ? 'Yes' : 'No';
}
