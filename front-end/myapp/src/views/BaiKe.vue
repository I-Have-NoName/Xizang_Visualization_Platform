<template>
    <div class="baike-list">
      <BaikeEntry v-for="(item, index) in entries" :key="index" :entry="item" />
    </div>
  </template>
  
  <script>
  import BaikeEntry from './/BaikeEntry.vue';
  import baikeData from '../../src/assets/zangdijingzhi.json';
  
  export default {
    components: {
      BaikeEntry
    },
    data() {
      return {
        entries: baikeData
      };
    }
  };
  
  </script>
  
  <style scoped>
.entry {
  display: flex;
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

@media (min-width: 768px) {
  .entry {
    flex-direction: row;
  }
}

.entry-content {
  flex: 1;
  padding-right: 20px;
}

.entry-title {
  font-size: 24px;
  font-weight: bold;
  color: #333;
  margin-bottom: 10px;
}

.entry-translation {
  font-size: 18px;
  color: #888;
  margin-bottom: 15px;
}

.entry-intro {
  font-size: 16px;
  line-height: 1.6;
  color: #555;
}

.entry-image {
  flex-shrink: 0;
  width: 300px;
}

.entry-image img {
  width: 100%;
  height: auto;
  border-radius: 5px;
}
</style>
  