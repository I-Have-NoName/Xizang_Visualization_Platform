<template>
  <div class="com-container">
    <transition name="fade">
      <div class="province-selector">
      <button @click="switchProvince('xizang')">西藏</button>
      <button @click="switchProvince('sichuan')">四川</button>
      <button @click="switchProvince('qinghai')">青海</button>
      <button @click="switchProvince('gansu')">甘肃</button>
      <button @click="switchProvince('yunnan')">云南</button>
      <!-- 其它省份按钮 -->
    </div>
      <div class="popup" v-if="$store.state.showPopup">
        <!-- 这里可以放置您的弹出页面内容 -->
        <Lasa v-if="$store.state.selectedProvince === '拉萨市'"></Lasa>
        <Ali v-if="$store.state.selectedProvince === '阿里地区'"></Ali>
        <Changdu v-if="$store.state.selectedProvince === '昌都市'"></Changdu>
        <Linzhi v-if="$store.state.selectedProvince === '林芝市'"></Linzhi>
        <Naqu v-if="$store.state.selectedProvince === '那曲地区'"></Naqu>
        <Rike v-if="$store.state.selectedProvince === '日喀则市'"></Rike>
        <Shannan v-if="$store.state.selectedProvince === '山南市'"></Shannan>

      </div>
      
    </transition>
    
    <div class="com-chart" ref="map_ref">

    </div>
    
  </div>
  
</template>

<script>
import axios from 'axios'
import GdpRank from "@/components/map/GdpRank.vue";
import Ali from "@/components/map/MapChildren/Ali.vue";
import Shannan from "@/components/map/MapChildren/Shannan.vue";
import Rike from "@/components/map/MapChildren/Rike.vue";
import Naqu from "@/components/map/MapChildren/Naqu.vue";
import Linzhi from "@/components/map/MapChildren/Linzhi.vue";
import Lasa from "@/components/map/MapChildren/Lasa.vue";
import Changdu from "@/components/map/MapChildren/Changdu.vue";

export default {
  data () {
    return {
      chartInstance: null,
      allData: null,
      showPopup: null,
      selectedProvince: ''
    }
  },
  components:{
    Ali,
    Changdu,
    Lasa,
    Linzhi,
    Naqu,
    Rike,
    Shannan
  },
  created() {
    this.showPopup = this.$popUp;
  },
  mounted () {
    this.initChart()
    this.getData()
    window.addEventListener('resize', this.screenAdapter)
    this.screenAdapter()
  },
  destroyed () {
    window.removeEventListener('resize', this.screenAdapter)
  },
  methods: {
    async initChart(provinceName = 'xizang') { // 传入省份名称，默认为 'xizang'
    this.chartInstance = this.$echarts.init(this.$refs.map_ref, 'chalk')
    
    // 根据传入的省份名称，动态加载相应的地图 JSON 文件
    const map = await axios.get(`http://localhost:8999/static/map/province/${provinceName}.json`)
    
    // 注册并使用该省份的地图
    this.$echarts.registerMap(provinceName, map.data)
    const name = {'xizang':'西藏','sichuan':'四川','qinghai':'青海','gansu':'甘肃','yunnan':'云南'}
    const initOption = {
      title: {
        text: `丨 ${name[provinceName]}地图`,
        left: 20,
        top: 20,
        textStyle: {
          color: 'white'
        }
      },
      series: [{
        type: 'map',
        map: provinceName,  // 使用动态的省份名称
        layoutCenter: ['50%', '50%'],
        layoutSize: '90%',
        data: this.getProvinceData(provinceName),  // 获取省份的模拟数据
        itemStyle: {
          borderColor: '#333'
        }
      }]
    }
    this.chartInstance.setOption(initOption)
  },
  getProvinceData(provinceName) {
    const provinceData = {
      'xizang': [
      {name: '拉萨市', value: 100, itemStyle: {areaColor: '#3077a3'}},
      {name: '阿里地区', value: 200, itemStyle: {areaColor: '#f59353'}},
      {name: '昌都市', value: 300, itemStyle: {areaColor: '#cebc56'}},
      {name: '林芝市', value: 400, itemStyle: {areaColor: '#1e90ff'}},
      {name: '那曲地区', value: 500, itemStyle: {areaColor: '#41810d'}},
      {name: '日喀则市', value: 600, itemStyle: {areaColor: '#5fce70'}},
      {name: '山南市', value: 700, itemStyle: {areaColor: '#ffa07a'}}
      ],
      "sichuan": [
    { "name": "成都市", "value": 500, "itemStyle": { "areaColor": "#ff6347" }},
    { "name": "绵阳市", "value": 300, "itemStyle": { "areaColor": "#4682b4" }},
    { "name": "自贡市", "value": 300, "itemStyle": { "areaColor": "#32cd32" }},
    { "name": "攀枝花市", "value": 300, "itemStyle": { "areaColor": "#ffa500" }},
    { "name": "泸州市", "value": 300, "itemStyle": { "areaColor": "#9370db" }},
    { "name": "德阳市", "value": 300, "itemStyle": { "areaColor": "#ff69b4" }},
    { "name": "广元市", "value": 300, "itemStyle": { "areaColor": "#20b2aa" }},
    { "name": "遂宁市", "value": 300, "itemStyle": { "areaColor": "#8a2be2" }},
    { "name": "内江市", "value": 300, "itemStyle": { "areaColor": "#dc143c" }},
    { "name": "乐山市", "value": 300, "itemStyle": { "areaColor": "#00bfff" }},
    { "name": "南充市", "value": 300, "itemStyle": { "areaColor": "#ff7f50" }},
    { "name": "眉山市", "value": 300, "itemStyle": { "areaColor": "#cd5c5c" }},
    { "name": "宜宾市", "value": 300, "itemStyle": { "areaColor": "#3cb371" }},
    { "name": "广安市", "value": 300, "itemStyle": { "areaColor": "#ff4500" }},
    { "name": "达州市", "value": 300, "itemStyle": { "areaColor": "#1e90ff" }},
    { "name": "雅安市", "value": 300, "itemStyle": { "areaColor": "#f0e68c" }},
    { "name": "巴中市", "value": 300, "itemStyle": { "areaColor": "#adff2f" }},
    { "name": "资阳市", "value": 300, "itemStyle": { "areaColor": "#778899" }},
    { "name": "阿坝藏族羌族自治州", "value": 300, "itemStyle": { "areaColor": "#ffdab9" }},
    { "name": "甘孜藏族自治州", "value": 300, "itemStyle": { "areaColor": "#d2691e" }},
    { "name": "凉山彝族自治州", "value": 300, "itemStyle": { "areaColor": "#6495ed" }}
    ],
    "yunnan": [
    { "name": "昆明市", "value": 500, "itemStyle": { "areaColor": "#ff4500" }},
    { "name": "曲靖市", "value": 300, "itemStyle": { "areaColor": "#1e90ff" }},
    { "name": "玉溪市", "value": 300, "itemStyle": { "areaColor": "#32cd32" }},
    { "name": "保山市", "value": 300, "itemStyle": { "areaColor": "#ffa500" }},
    { "name": "昭通市", "value": 300, "itemStyle": { "areaColor": "#9370db" }},
    { "name": "丽江市", "value": 300, "itemStyle": { "areaColor": "#ff69b4" }},
    { "name": "普洱市", "value": 300, "itemStyle": { "areaColor": "#20b2aa" }},
    { "name": "临沧市", "value": 300, "itemStyle": { "areaColor": "#8a2be2" }},
    { "name": "楚雄彝族自治州", "value": 300, "itemStyle": { "areaColor": "#dc143c" }},
    { "name": "红河哈尼族彝族自治州", "value": 300, "itemStyle": { "areaColor": "#00bfff" }},
    { "name": "文山壮族苗族自治州", "value": 300, "itemStyle": { "areaColor": "#ff7f50" }},
    { "name": "西双版纳傣族自治州", "value": 300, "itemStyle": { "areaColor": "#cd5c5c" }},
    { "name": "大理白族自治州", "value": 300, "itemStyle": { "areaColor": "#3cb371" }},
    { "name": "德宏傣族景颇族自治州", "value": 300, "itemStyle": { "areaColor": "#ff4500" }},
    { "name": "怒江傈僳族自治州", "value": 300, "itemStyle": { "areaColor": "#1e90ff" }},
    { "name": "迪庆藏族自治州", "value": 300, "itemStyle": { "areaColor": "#f0e68c" }}
  ],
  "qinghai": [
    { "name": "西宁市", "value": 500, "itemStyle": { "areaColor": "#ff6347" }},
    { "name": "海东市", "value": 300, "itemStyle": { "areaColor": "#4682b4" }},
    { "name": "海北藏族自治州", "value": 300, "itemStyle": { "areaColor": "#7fff00" }},
    { "name": "黄南藏族自治州", "value": 300, "itemStyle": { "areaColor": "#ff69b4" }},
    { "name": "海南藏族自治州", "value": 300, "itemStyle": { "areaColor": "#9370db" }},
    { "name": "果洛藏族自治州", "value": 300, "itemStyle": { "areaColor": "#b8860b" }},
    { "name": "玉树藏族自治州", "value": 300, "itemStyle": { "areaColor": "#8a2be2" }},
    { "name": "海西蒙古族藏族自治州", "value": 300, "itemStyle": { "areaColor": "#d2691e" }}
  ],
  "gansu": [
    { "name": "兰州市", "value": 500, "itemStyle": { "areaColor": "#ffa07a" }},
    { "name": "嘉峪关市", "value": 300, "itemStyle": { "areaColor": "#7b68ee" }},
    { "name": "金昌市", "value": 300, "itemStyle": { "areaColor": "#cd5c5c" }},
    { "name": "白银市", "value": 300, "itemStyle": { "areaColor": "#f08080" }},
    { "name": "天水市", "value": 300, "itemStyle": { "areaColor": "#add8e6" }},
    { "name": "武威市", "value": 300, "itemStyle": { "areaColor": "#ff8c00" }},
    { "name": "张掖市", "value": 300, "itemStyle": { "areaColor": "#ff1493" }},
    { "name": "平凉市", "value": 300, "itemStyle": { "areaColor": "#ff4500" }},
    { "name": "酒泉市", "value": 300, "itemStyle": { "areaColor": "#32cd32" }},
    { "name": "庆阳市", "value": 300, "itemStyle": { "areaColor": "#1e90ff" }},
    { "name": "定西市", "value": 300, "itemStyle": { "areaColor": "#ffa500" }},
    { "name": "陇南市", "value": 300, "itemStyle": { "areaColor": "#4682b4" }},
    { "name": "临夏回族自治州", "value": 300, "itemStyle": { "areaColor": "#8b4513" }},
    { "name": "甘南藏族自治州", "value": 300, "itemStyle": { "areaColor": "#ffdab9" }}
  ]
      // 继续添加其它省份数据
    };
    return provinceData[provinceName] || [];
  },
    async getData() {
      this.updateChart()
    },
  updateChart() {
  const dataOption = {};
  this.chartInstance.setOption(dataOption);
  this.chartInstance.on('click', arg => {
    console.log(arg.name);
    this.openPopup(arg.name);

    // 跳转到 /baike 页面
      this.$router.push('/baike');
    });
  },

    async switchProvince(provinceName) {
    // 每次切换省份时，重新加载该省份的地图
    await this.initChart(provinceName);
  },
    screenAdapter() {
      const titleFontSize = this.$refs.map_ref.offsetWidth / 100 * 5
      const adapterOption = {
        title: {
          textStyle: {
            fontSize: titleFontSize
          }
        },
      }
      this.chartInstance.setOption(adapterOption)
      this.chartInstance.resize()
    },
    openPopup(provinceName) {
      // 调用 Vuex action 来更新状态
      this.$store.dispatch('changeProvince', provinceName);
      this.$store.dispatch('togglePopup', true);
    },
    closePopup() {
      this.$store.dispatch('togglePopup', false);
    }
  }
}
</script>

<style scoped lang="less">

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s, transform 0.5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active 在2.1.8版本及以上 */ {
  opacity: 0;
  transform: scale(0.5);
}

.popup {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 50vw; /* 百分比视口宽度，以适应不同屏幕大小 */
  height: 50vh; /* 百分比视口高度 */
  background: white;
  padding: 20px;
  box-shadow: 0 0 10px rgba(0,0,0,0.5);
  z-index: 10000;
  overflow: auto; /* 如果内容溢出，则显示滚动条 */
  border-radius: 10px; /* 可选的圆角边框 */
}

.popup > * {
  width: 100%; /* 子元素宽度设置为100% */
  height: 100%; /* 子元素高度设置为100% */
  box-sizing: border-box; /* 确保内边距和边框不会增加元素尺寸 */
}
.province-selector button {
  margin: 0 10px;
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 5px;
}

.province-selector button:hover {
  background-color: #0056b3;
}
</style>
