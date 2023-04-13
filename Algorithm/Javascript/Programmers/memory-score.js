function solution(name, yearning, photo) {
  const res = [];

  for (let i = 0; i < photo.length; i++) {
    let key = 0;
    for (let j = 0; j < photo[i].length; j++) {
      if (name.indexOf(photo[i][j]) !== -1) {
        key = key + yearning[name.indexOf(photo[i][j])];
      }
    }
    res.push(key);
  }

  return res;
}

// https://school.programmers.co.kr/learn/courses/30/lessons/176963
