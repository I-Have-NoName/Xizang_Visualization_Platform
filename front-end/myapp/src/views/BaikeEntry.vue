<template>
    <div class="entry">
      <h2>{{ entry.name }}</h2>
      <h4>{{ entry.translation }}</h4>
      <h4>{{ entry.location }}</h4>
      <img :src="getImageUrl(entry.pic_name)" :alt="entry.name" />
      <p>{{ entry.introduction }}</p>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      entry: Object
    },
    methods: {
      getImageUrl(picName) {
        return require(`../../public/static/img/${picName}`);
      }
    }
  };
  </script>
  
  <style scoped>
  .entry {
    margin: 20px;
  }
  img {
    max-width: 100%;
    height: auto;
  }
  </style>
  