<template>
  <div>
    <div class="dictheader" style="height: 60px">
      <button @click="backHome">
        <img class="arrow" src="/static/img/arrow.png">
      </button>
    </div>
    <span style="text-align: center; height: 40px;">
      <h1>藏百科</h1>
    </span>
    <div class="swiper">
    <div @mouseleave="leave" @mouseenter="enter">
      <swiper ref="mySwiper" :options="swiperOption">
        <swiper-slide v-for="(item, index) in entries" :key="index" class="slide">
          <router-link :to="{ name: 'BaikeDetail', params: { id: index } }">
            <BaikeEntry :entry="item" class="baike-list" />
          </router-link>
        </swiper-slide>
      </swiper>
    </div>
    <div @mouseenter="enter" @mouseleave="leave">
      <div class="swiper-button-prev"></div>
      <div class="swiper-button-next"></div>
    </div>
  </div>
  </div>
</template>
<script>
import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
import {useRouter} from "vue-router/composables";
import 'swiper/css/swiper.css'
import BaikeEntry from './/BaikeEntry.vue';
import baikeData from '../../src/assets/zangbaike.json';
export default {
  components: {
    Swiper,
    SwiperSlide,
    BaikeEntry
  },
  data () {
    return {
      clist: [
      {
            imgUrl: ("/static/img/Yaks-Kailash-Manasarovar.jpg")
          },
          {
            imgUrl: ("/static/img/NamTso_scene.jpg")
          },
          {
            imgUrl: ("/static/img/Mount_Everest_North_Face.jpg")
          },
          {
            imgUrl: ("/static/img/Potala_palace23.jpg")
          },
      ],
      swiperOption: {
        // 衔接滑动
        loop: true,
        // 自动滑动
        autoplay: {
          delay: 2000,
          // 如果设置为true，当切换到最后一个slide时停止自动切换。
          stopOnLastSlide: false,
          // 如果设置为false，用户操作swiper之后自动切换不会停止，每次都会重新启动autoplay
          disableOnInteraction: false
        },
        // 切换效果 "coverflow"（3d流）
        effect: 'coverflow',
        // 设置slider容器能够同时显示的slides数量
        slidesPerView:2,
        // 居中幻灯片。设定为true时，当前的active slide 会居中，而不是默认状态下的居左。
        centeredSlides: true,
        // 设置为true则点击slide会过渡到这个slide。
        slideToClickedSlide: true,
        coverflowEffect: {
          // slide做3d旋转时Y轴的旋转角度
          rotate: -1,
          // 每个slide之间的拉伸值，越大slide靠得越紧。5.3.6 后可使用%百分比
          stretch: 50,
          // slide的位置深度。值越大z轴距离越远，看起来越小。
          depth: 80,
          // depth和rotate和stretch的倍率，相当于depth*modifier、rotate*modifier、stretch*modifier，值越大这三个参数的效果越明显。
          modifier: 6,
          // 是否开启slide阴影
          slideShadows: true
        },
        // 使用前进后退按钮来控制Swiper切换。
        navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev'
        }
      },
      entries: baikeData
    }
  },
  computed: {
    mySwiper () {
      // mySwiper 是要绑定到标签中的ref属性
      return this.$refs.mySwiper.$swiper
    }
  },
  mounted(){
    this.router = useRouter()
  },
  methods:{
    enter () {
      this.mySwiper.autoplay.stop()
    },
    leave () {
      this.mySwiper.autoplay.start()
    },
    backHome(){
      this.router.push({name:'HomePage'})
    },
  //   goToBaike(index) {
  //   console.log("Card clicked!", index); // 检查点击事件是否触发
  //   this.$router.push({ name: 'BaikeDetail', params: { id: index } });
  // }
  }
}
</script>
<style scoped>

.swiper{
  width:90%;
  height: 100%;
  margin: 0 auto;
  padding-top: 0%;
  padding-bottom: 40px;
  
}
.baike-list {
  display: grid;
  grid-template-columns: 50% 50%; /* 左侧图片占据50%，右侧内容占据50% */
  padding: 16px;
  box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  background: linear-gradient(180deg, #79d8cd 0%, #e3eaf4 100%);
  height: 100%; /* 让卡片区域始终高度均匀 */
}



.slide{
  width: 1000px;  /* 卡片的宽度 */
  height: 450px;
  background: linear-gradient(180deg, #f7f8fc 0%, #e3eaf4 100%); /* 卡片背景柔和渐变 */
  border-radius: 12px; /* 圆角 */
  box-shadow: 1px 4px 10px rgba(0, 0, 0, 0.15); /* 添加阴影，使卡片更加立体 */
  overflow: hidden; /* 确保内容不会溢出卡片 */
  transition: transform 0.3s ease; /* 鼠标悬停效果的动画 */
}

a {
    text-decoration: none;
    color: inherit;
}


.dictheader {
  background-color: #f7f8fc;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1); /* 顶部按钮栏的阴影 */
}
.dictheader button {
  position: fixed;
  top: 1rem;
  right: 1rem;
  width: 48px;
  aspect-ratio: 1;
  padding: 0;
  border-radius: 12px;
  border: 0;
  background: transparent;
  display: grid;
  place-items: center;
  cursor: pointer;
}

.arrow{
  position: fixed;
  top: 1rem;
  left: 1rem;
  width: 48px;
  aspect-ratio: 1;
  padding: 0;
  border-radius: 12px;
  border: 0;
  background: transparent;
  display: grid;
  place-items: center;
  cursor: pointer;

}

img.arrow {
    width: 36px;
}
</style>