<template>
    <main>
        <div class="title">
            <h1>藏百科</h1>
        </div>
        <div class="slider">
            <div class="slideshow">
                <a href="javascript:void(0)" v-if="index!=0" @click="prev" class="left">
                    <img src="static\img\arrow.png" alt="" />
                </a>
                <img :src="imgArr[index]" alt="" class="dict"/>
            <!-- 左箭头 -->
                
                <!-- 右箭头 -->
                <a href="javascript:void(0)" v-show="index<imgArr.length-1" @click="next" class="right">
                    <img src="static\img\arrow2.png" alt="" />
                </a>
            </div>
        </div>
        
    </main>
    
</template>
<script>
export default {
     data(){
        return{
        imgArr: [
          "static/img/Mount_Everest_North_Face.jpg",
          "static/img/mountain.jpeg",
          "static/img/NamTso_scene.jpg",
          "static/img/namucuo.jpeg",
        ],
        index: 0}
      },
      methods: {
        fun:function(){
                //setInterval(函数体,时间)
                setInterval(this.next,2000)
        },
        prev:function(){
          this.index--;
        },
        next:function(){
          this.index++;
          const len = this.imgArr.length;
        //   console.log(len);
          if(this.index == this.imgArr.length){
             this.index = 0;
          }
        }
      },
      mounted:function(){    //生命周期  钩子函数   挂载完成
            this.fun()
      }
    }
</script>
<style>
  * {
    margin: 0;
    padding: 0;
    list-style: none;
  }
  body, html {
    height: 100%;
  }
  .title {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 50px;
    background-color: #f0f0f0;
  }
  h1 {
    font-size: 24px;
  }
  .slider {
    width: 100%;
    height: calc(100% - 50px);
    overflow: hidden;
    position: relative;
  }
  .slideshow {
    width: 100%;
    height: 100%;
    display: grid;
    grid-template-columns: 70px,auto 70px;
    justify-content: center;
  }
  .dict{
    width: 800px;
    height: 500px;
    padding: 10px
  }
  
  .left,.right {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    z-index: 1;
  }
  .left {
    left: 10px;
  }
  .right {
    right: 10px;
  }
</style>