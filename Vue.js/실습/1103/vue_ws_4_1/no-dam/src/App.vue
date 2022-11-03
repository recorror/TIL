<template>
  <div id="app" class="container">
    <h1 class="m-4 p-0">버튼 박스 제작</h1>
    <div class="row" id="box">
      <h2 class="m-0 p-3">예약 페이지</h2>
      <h3 class="mb-2 p-2">시간 선택</h3>
      <ul v-for="(time, idx) in times" :key="idx" class="mapa col-2">
        <li :class="{'text-color': isSelected(time)}" @click="selectTime(time)">{{time}}</li>
      </ul>
      <div>
        <hr class="border-solid-2 mapa ">
        <div class="row">
          <div class="col-1"></div>
          <p class="col">선택사항: </p>
          <ul v-for="(stime, idx) in sTime.sort()" :key="idx" class="col">
            <li>{{stime}}</li>
          </ul>
          <div class="col-1"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'App',
  data () {
    return {
      times: [
        "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
        "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
        "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
      ],
      sTime: [],
    }
  },
  methods: {
    selectTime (timeData) {
      // 안에 같은 값이 있을 경우(즉, 클릭 된 경우)
      // 해당 값을 배열에서 제거해준다.
      if (this.sTime.includes(timeData) === true) {
        let pos = this.sTime.indexOf(timeData)
        this.sTime.splice(pos, 1)
      // 클릭 안 되어있는 경우
      } else {
        // 클릭 하는 경우 data가 sTime에 넘어가야한다.
        if (this.sTime.length < 5) {
        this.sTime.push(timeData)
        } else {
        alert('5타임 까지만 신청할 수 있습니다.')
        }
      }
    },
    isSelected (timeData) {
      return this.sTime.includes(timeData)
    }
  },
}
</script>

<style>
#app {
  font-family: 'Noto Sans KR', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #424242;
  margin-top: 60px;
}
ul {
  list-style: none;
  padding-left: 0;
}
#box {
  box-shadow: 1px 5px 10px gray;
}
.mapa {
  margin: 0px;
  padding: 0px;
}
.paddingSide {
  padding: 0px 20px;
}
.text-color{
  color: #0F4C81;
  background-color: #658dc63d;
}
</style>
