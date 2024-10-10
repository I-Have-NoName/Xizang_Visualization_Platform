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
  

  <script>
  import {useRouter} from "vue-router/composables";
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
    },
    mounted(){
      this.router = useRouter()
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
  width: 500px;
  height: 300px;
  border-radius: 5px;
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
  