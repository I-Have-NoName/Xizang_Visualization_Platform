<template>
  <div class="swiper">
    <div @mouseleave="leave" @mouseenter="enter">
      <swiper ref="mySwiper" :options="swiperOption">
        <swiper-slide v-for="(item) in clist"
          :key="item.imgUrl">
          <img :src="item.imgUrl" class="slide-img"/>
        </swiper-slide>
      </swiper>
    </div>
    <div @mouseenter="enter" @mouseleave="leave">
      <div class="swiper-button-prev"></div>
      <div class="swiper-button-next"></div>
    </div>
  </div>
</template>
<script>
import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
import 'swiper/css/swiper.css'
export default {
  components: {
    Swiper,
    SwiperSlide
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
        slidesPerView:4,
        // 居中幻灯片。设定为true时，当前的active slide 会居中，而不是默认状态下的居左。
        centeredSlides: true,
        // 设置为true则点击slide会过渡到这个slide。
        slideToClickedSlide: true,
        coverflowEffect: {
          // slide做3d旋转时Y轴的旋转角度
          rotate: 0,
          // 每个slide之间的拉伸值，越大slide靠得越紧。5.3.6 后可使用%百分比
          stretch: 0,
          // slide的位置深度。值越大z轴距离越远，看起来越小。
          depth: 60,
          // depth和rotate和stretch的倍率，相当于depth*modifier、rotate*modifier、stretch*modifier，值越大这三个参数的效果越明显。
          modifier: 5,
          // 是否开启slide阴影
          slideShadows: true
        },
        // 使用前进后退按钮来控制Swiper切换。
        navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev'
        }
      },
    }
  },
  computed: {
    mySwiper () {
      // mySwiper 是要绑定到标签中的ref属性
      return this.$refs.mySwiper.$swiper
    }
  },
  methods:{
    enter () {
      this.mySwiper.autoplay.stop()
    },
    leave () {
      this.mySwiper.autoplay.start()
    },
  }
}
</script>
<style >
.slide-img{
  width: 100%;
  height: 100%;
}
.swiper{
  width:1200px;
  height: 100%;
  margin: 0 auto;
  padding-top: 14%;
  padding-bottom: 40px;
}

</style>