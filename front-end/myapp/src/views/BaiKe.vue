<template>
    <div>
      <button @click="backHome">
        <img class="arrow" src="/static/img/arrow.png">
      </button>
      <div class="baike-list">
      <BaikeEntry v-for="(item, index) in entries" :key="index" :entry="item" />
      </div>
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
        entries: baikeData
      };
    },
    mounted(){
      this.router = useRouter()
      console.log(this.entries)
    },
    methods:{
    backHome(){
      this.router.push({name:'HomePage'})
    }
  },
    
  };
  
  </script>
  
  <style scoped>

  
.entry {
  display: inline-flex;
  flex-direction: column;
  background-color: #fff;
  border: 1px solid #e5e5e5;
  border-radius: 5px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  padding: 20px;
  margin: 20px 0;
  width: 100%;
  max-width: 1000px;
}

@media (min-width: 500px) {
  .entry {
    flex-direction: column;
  }
}

.entry {
    margin-bottom: 2rem; /* 为每个条目添加间隔 */
  }
  
  .content {
    display: flex;
    align-items: center; /* 垂直居中对齐 */
    justify-content: space-between; /* 水平间隔 */
  }
  
  .image {
    flex: 1; /* 图片占据的空间 */
    padding: 1rem; /* 内边距 */
    display: flex; /* 使用flex布局 */
    justify-content: center; /* 水平居中图片 */
    align-items: center; /* 垂直居中图片 */
  }
  
  .image img {
    width: 100%; /* 图片宽度占满容器 */
    height: auto; /* 自适应高度 */
    max-height: 400px; /* 最大高度 */
    object-fit: cover; /* 按比例裁剪图片 */
    border-radius: 10px; /* 圆角 */
  }
  
  .text {
    flex: 1; /* 文本占据的空间 */
    padding: 1rem; /* 内边距 */
  }
  
  .text h2,
  .text h4 {
    text-align: center; /* 标题居中 */
    margin: 0;
    text-transform: uppercase; /* 标题大写 */
  }
  
  .text h2 {
    font-size: 28px;
    font-weight: bold;
    margin-bottom: 8px;
  }
  
  .text h4 {
    font-size: 20px;
    color: #666;
    margin-bottom: 16px;
  }
  
  .text p {
    font-size: 16px;
    line-height: 1.5;
    text-align: justify; /* 段落内容两端对齐 */
    margin-top: auto; /* 将段落推到右侧下部 */
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
</style>
  