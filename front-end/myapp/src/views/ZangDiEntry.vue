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
  display: flex; /* 使用Flexbox布局 */
  align-items: flex-start; /* 垂直对齐到顶部 */
  padding: 20px; /* 内边距 */
}

.content {
  display: flex; /* 嵌套的Flexbox布局 */
  width: 100%; /* 设置宽度为100% */
}

.image {
  flex: 1; /* 左侧图像占据一半空间 */
  max-width: 50%; /* 最多占用50%宽度 */
}

.image img {
  width: 100%; /* 图像自适应宽度 */
  height: auto; /* 高度自动 */
  border-radius: 8px; /* 添加圆角效果（可选） */
}

.text {
  flex: 1; /* 右侧文本占据一半空间 */
  padding-left: 20px; /* 左边距，给图像留出空间 */
}

h2 {
  margin: 0; /* 去掉默认的外边距 */
  font-size: 24px; /* 标题大小 */
}

h4 {
  margin: 5px 0; /* 设置上下外边距 */
  font-size: 18px; /* 副标题大小 */
  color: #555; /* 设置副标题颜色 */
}

p {
  line-height: 1.6; /* 行高，增加可读性 */
  color: #333; /* 设置段落颜色 */
}

  </style>
  