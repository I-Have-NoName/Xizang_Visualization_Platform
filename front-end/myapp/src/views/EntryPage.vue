<template>
    <div>
      <button @click="backHome">
        <img class="arrow" src="/static/img/arrow.png">
      </button>
      <main>
        <div v-if="entry" class="entry">
        <section>
        <div class="content">
          <div class="text">
        <h2>{{entry.name}}</h2>
        <h3>{{ entry.translation }}</h3>
        <!-- <h3>{{ entry.location }}</h3> -->
        <mark data-author="JT"><span><p>{{ entry.introduction }}</p></span></mark>
          </div>
          <div class="image">
            <img :src="getImageUrl(entry.pic_name)" :alt="entry.name" />
          </div>
        </div>
      </section>
      </div>
      <div v-else>
        <p>百科条目未找到。</p>
      </div>
      </main>
    </div>
  </template>
  
  <script>
import baikeData from '../../src/assets/zangbaike.json';
import {useRouter} from "vue-router/composables";
export default {
  data() {
    return {
      entry: baikeData
    };
  },
  mounted() {
    
    const entryId = this.$route.params.entryName; // 获取 URL 中的 id 参数
    console.log("名字:"+entryId);
    this.entry = baikeData.find(item => item.name == entryId); // 根据 name 查找对应的词条
    this.router = useRouter();
  },
  methods:{
    getImageUrl(picName) {
        return require(`../assets/${picName}`);
      },
    backHome(){
      this.router.push({name:'HomePage'})
    }
  }
};
</script>


<style scoped>
main {
  padding: 0 1rem;
  width: 60vw;
  max-width: 80%;
  margin: 0 auto;
  font-size: 1.25rem;
  /* top: 30%; */
  padding: 0 0 50vmin 0;
  overflow-y: auto; /* Enable scrolling */
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

/* section {
    top: 30%;
} */

button svg {
  width: 65%;
}

mark {
  --highlighted: 1;
  background: transparent;
}

.dark mark {
  --lightness: 35%;
}

mark span {
  background: linear-gradient(120deg, lightblue 50%, transparent 50%) 110% 0 / 200% 100% no-repeat;
  background-position: calc((1 - var(--highlighted)) * 110%) 0;
  transition: background-position 1s;
}

p, li {
  position: relative;
}

a {
  color: hsl(212 100% 50%);
  text-decoration: none;
}

a:is(:hover, :focus-visible) {
  text-decoration: underline;
  text-underline-offset: 6px;
}

hr {
  margin: 2rem auto;
}

hr + p {
  text-align: center;
}

mark::after {
  content: attr(data-author);
  display: grid;
  place-items: center;
  font-variant-numeric: tabular-nums;
  font-weight: bold;
  position: absolute;
  width: 32px;
  aspect-ratio: 1;
  border-radius: 12px;
  background: lightblue;
  font-weight: 80;
  top: 0;
  left: 100%;
  translate: 50% 0;
  font-size: 0.875rem;
  scale: var(--highlighted);
  transition: scale 0.2s;
}
section {
  margin-bottom: 2rem;
}

:where(h1, h2) {
  font-weight: 120;
}
.content {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.content .text {
  flex: 1;
  padding: 1rem;
}

.content .image {
  flex: 1;
  padding: 1rem;
  display: flex;
  justify-content: center;
  align-items: center;
}

.content img {
  max-width: 100%;
  height: auto;
  max-height: 100%;
  object-fit: cover;
}

</style>
