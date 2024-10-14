<template>
    <div class="entry">
      <img :src="getImageUrl(entry.pic_name)" :alt="entry.name" />
      <div class="content">
        <h2>{{ entry.name }}</h2>
      <h4>{{ entry.translation }}</h4>
      <!-- <h4>{{ entry.location }}</h4> -->
      
      <p>{{ entry.introduction }}</p>
      </div>
    </div>
  </template>
  
  <script scoped>
  export default {
    props: {
      entry: Object
    },
    methods: {
      getImageUrl(picName) {
        return require(`../assets/${picName}`);
      }
    }
  };
  </script>
  
  <style scoped>
  .entry img {
  width: 330px; /* 图片占满左半部分 */
  height: 400px; /* 图片高度撑满整个区域 */
  object-fit: cover; /* 图片按比例裁剪 */
  border-radius: 10px 10px 10px 10px; /* 左侧图片圆角 */
}

.content {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 20px;
}

.content h2,
.content h4 {
  text-align: center;
  margin: 0;
  text-transform: uppercase; /* 标题大写 */
}

.content h2 {
  font-size: 28px;
  font-weight: bold;
  margin-bottom: 8px;
}

.content h4 {
  font-size: 20px;
  color: #666;
  margin-bottom: 16px;
}

.content p {
  font-size: 16px;
  line-height: 1.5;
  text-align: justify; /* 使段落内容两端对齐 */
  margin-top: auto; /* 将段落推到右侧下部 */
}

  </style>
  