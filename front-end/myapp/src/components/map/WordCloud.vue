<template>
  <div class="com-container">
    <div class="chart-title">丨 最热词云</div>
    <div class="com-chart" ref="wordcloudChart" ></div>
  </div>
</template>

<script>
import * as echarts from 'echarts';
import baikeData from '../../assets/zangbaike.json';
export default {data() {
    return {
      chartInstance: null,
      allData: null,
      entry:baikeData
    };
  },
  created () {
    this.$socket.registerCallBack('wordData', this.getData)
  },
  mounted() {
    // 在 mounted 钩子中绘制词云图
    this.drawWordCloud();
    this.$socket.send({
      action: 'getData',
      socketType: 'wordData',
      chartName: 'characteristic',
      value: ''
    })
  },
  beforeDestroy() {
    if (this.chartInstance != null) {
      this.chartInstance.dispose();
    }
    window.removeEventListener('resize', this.handleResize);
  },
  destroyed () {
    window.removeEventListener('resize', this.screenAdaptor)
    this.$socket.unRegisterCallBack('wordData')
  },
  methods: {
    getData(ret){
      this.allData = ret
    },
    drawWordCloud() {
      const wordCloudData = this.entry.map(item => ({
        name: item.name,
        value: Math.floor(Math.random() * 9000) + 1000 // 随机生成 1000 到 10000 之间的值
      }));
      // 基于准备好的dom，初始化echarts实例
      this.chartInstance = echarts.init(this.$refs.wordcloudChart,'chalk');
      // 配置项
      const option = {
        series: [{
          type: 'wordCloud',
          shape: 'circle',
          left: 'center',
          top: 'center',
          width: '70%',
          height: '90%',
          right: null,
          bottom: null,
          sizeRange: [12, 70],
          rotationRange: [-90, 90],
          rotationStep: 45,
          gridSize: 8,
          drawOutOfBound: false,
          textStyle: {
            fontWeight: 'bold',
            fontFamily: 'sans-serif',
            // Color可以是一个回调函数
            color: function () {
              return 'hsl(' + Math.round(Math.random() * 360) + ', 80%, 50%)';
            }
          },
          emphasis: {
            focus: 'self',
            textStyle: {
              textShadowBlur: 10,
              textShadowColor: '#333'
            }
          },
          data: wordCloudData
        }]
      };
      this.chartInstance.setOption(option);
      
      this.chartInstance.on('click', params => {
        const name = params.name; // 获取点击的词条的 name
        this.navigateToPage(name); // 跳转到对应的页面
      });
    },
    navigateToPage(name) {
      // 假设路由中的页面路径和词条名相同
      this.$router.push({ name: 'entryPage', params: { entryName: name } });
    },
    handleResize() {
      if (this.chartInstance != null) {
        this.chartInstance.resize();
      }
    },
  }
}
</script>

<style scoped>
.chart-title{
    position: absolute;
    top: 0;
    left: 0;
    padding: 10px;
    color: #fff;
    z-index: 10;

}
</style>
