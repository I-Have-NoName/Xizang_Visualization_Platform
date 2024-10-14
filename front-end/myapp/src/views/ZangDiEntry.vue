<template>
    <div class="entry">
      <div class="content">
        <div class="image">
          <img :src="getImageUrl(entry.pic_name)" :alt="entry.name" />
        </div>
        <div class="text">
          <h2>{{ entry.name }}</h2>
          <h4>{{ entry.translation }}</h4>
          <h4>{{ entry.location }}</h4>
          <p>{{ entry.introduction }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script scoped>
  export default {
    props: {
      entry: Object,
    },
    methods: {
      getImageUrl(picName) {
        return require(`../../public/static/img/${picName}`);
      },
    },
  };
  </script>
  
  <style scoped>
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
  </style>
  