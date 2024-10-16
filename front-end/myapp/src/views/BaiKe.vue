<template>
    <div >
      <button @click="backHome">
        <img class="arrow" src="/static/img/arrow.png">
      </button>
      <h1 style="display: flex;text-align: center;font-family: 楷体, Tahoma, Geneva, Verdana, sans-serif;font-size: 350%;margin: 0%;align-content: center;justify-content: center;padding-top: 30px;">藏地景致</h1>
      <div class="baike-list">
      <BaikeEntry v-for="(item, index) in entry" :key="index" :entry="item" />
      </div>
      <button class="scroll-top" @click="scrollToTop">
      ↑ 回到顶部
      </button>
    </div>
  </template>
  

  <script scoped>
  import {useRouter} from "vue-router/composables";
  import BaikeEntry from './ZangDiEntry.vue';
  import baikeData from '../../src/assets/zangdijingzhi.json';
  
  export default {
    components: {
      BaikeEntry
    },
    data() {
      return {
        entry: baikeData
      };
    },
    mounted(){
      // this.router = useRouter()
      // console.log(this.entries)
      const entryId = this.$route.params.BaikeName; // 获取 URL 中的 id 参数
    console.log("名字:"+entryId);
    // this.entry = baikeData.find(item => item.location == entryId); // 根据 name 查找对应的词条
    this.entry = (baikeData.filter(item => item.location == entryId));
    if(entryId == null){
      this.entry = baikeData;

    }
    console.log(this.entry)
    this.router = useRouter();
    },
    beforeDestroy() {
      window.removeEventListener('scroll', this.handleScroll); // 清理事件监听
    },
    methods:{
    backHome(){
      this.router.push({name:'HomePage'})
    },
    scrollToTop() {
      window.scrollTo({ top: 0, behavior: 'smooth' }); // 平滑滚动到顶部
    },
    handleScroll() {
        const scrollTopButton = document.querySelector('.scroll-top');
        const scrollTop = document.documentElement.scrollTop; // 获取滚动高度
        console.log('滚动高度:', scrollTop); // 打印当前滚动高度
        if (scrollTop > 300) {
          scrollTopButton.classList.add('visible'); // 添加visible类
        } else {
          scrollTopButton.classList.remove('visible'); // 移除visible类
        }
    }
  },
    
  };
  
  </script>
  
  <style scoped>

  *{
    background-image: url(../../public/static/img/zangbaike.png);
    background-attachment: fixed;
  }
.baike-list {
  display: flex; /* 使用Flexbox布局 */
  flex-direction: column; /* 纵向排列 */
  align-items: center; /* 水平居中对齐 */
  justify-content: center; /* 垂直居中对齐（在有高度限制的情况下） */
  margin-top: 80px; /* 可选：给上方留出空间，以避免按钮遮挡 */
}

.entry {
  display: flex; /* 修改为flex布局以便于内容对齐 */
  flex-direction: column; /* 纵向排列内容 */
  align-items: center; /* 内容水平居中对齐 */
  background-color: #fff;
  border: 1px solid #e5e5e5;
  border-radius: 20px;
  box-shadow: 10px 2px 8px rgba(0, 0, 0, 0.1);
  padding: 20px;
  margin: 20px 0;
  width: 100%;
  max-width: 1000px; /* 最大宽度 */
  box-shadow: #000;
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
}

/* 添加响应式设计，使在小屏幕上仍能良好显示 */
@media (max-width: 500px) {
  .entry {
    flex-direction: column;
  }
} 


button {
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

[aria-pressed=true] svg path:last-of-type,
[aria-pressed=false] svg path:first-of-type {
  display: none;
}

button svg {
  width: 65%;
}

.scroll-top {
  position: fixed; /* 固定在页面右下角 */
  bottom: 20px; /* 距离底部20像素 */
  right: 20px; /* 距离右边20像素 */
  padding: 10px 15px; /* 内边距 */
  background-color: #007BFF; /* 按钮背景颜色 */
  color: white; /* 按钮文字颜色 */
  border: none; /* 去掉边框 */
  border-radius: 5px; /* 圆角 */
  cursor: pointer; /* 鼠标指针样式 */
  font-size: 16px; /* 字体大小 */
  opacity: 0; /* 初始透明度为0 */
  visibility: hidden; /* 初始不可见 */
  transition: opacity 0.3s ease, visibility 0.3s ease; /* 添加过渡效果 */
}

.scroll-top.visible {
  opacity: 1; /* 设置透明度为1 */
  visibility: visible; /* 设置可见 */
}
</style>
  