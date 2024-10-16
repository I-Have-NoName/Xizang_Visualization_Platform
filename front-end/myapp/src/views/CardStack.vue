<template>
  <main>
    <!-- <div class="building"> -->
      <div class="content">
        <h1 >
          <img src="../../public/static/img/xizangwenzi.png" alt="" style="width: 300px; height: 280px;">
        </h1>
        <p>
          在那遥远的天边，有一片神秘而圣洁的土地，它叫做西藏。踏上西藏的征程，就仿佛踏入了一个梦幻的世界。雄伟的雪山高耸入云，洁白的雪顶闪耀着圣洁的光芒，神秘的湖泊如同大地的眼睛，深邃而宁静。
          沿着古老的道路前行，我们能感受到岁月的沉淀和历史的厚重。寺庙中传来阵阵诵经声，那是信仰的力量在流淌。西藏的每一处风景都蕴含着无尽的故事，在这里，你可以抛开世俗与自己的内心对话。让我们一起走进西藏，去揭开那神秘的面纱，探寻那属于我们心灵的栖息地，在这片圣土上留下我们最深刻的足迹和最难忘的回忆。
        </p>
        <button class="btn" @click="goToHomePage">探索更多</button>
      </div>

      <div class="stack" ref="stack">
        <div class="card" v-for="(card, index) in cardImages" :key="index">
          <img :src="card" alt="" />
        </div>
      </div>
    <!-- </div> -->
  </main>
</template>

<script>
import { ref, onMounted, onUnmounted } from 'vue';
import router from "@/router";
import {useRouter} from "vue-router/composables";

export default {
  setup() {
    const stack = ref(null);
    const cardImages = ref([
      "/static/img/Yaks-Kailash-Manasarovar.jpg",
      "/static/img/NamTso_scene.jpg",
      "/static/img/Mount_Everest_North_Face.jpg",
      "/static/img/Potala_palace23.jpg",

    ]);

    let autoplayInterval = null;

    const router = useRouter();

    const goToHomePage = () => {
      router.push({ name: 'HomePage' });
    };


    const moveCard = () => {
      const lastCard = stack.value.lastElementChild;
      if (lastCard.classList.contains('card')) {
        lastCard.classList.add('swap');

        setTimeout(() => {
          lastCard.classList.remove('swap');
          if(stack.value){
            stack.value.insertBefore(lastCard, stack.value.firstElementChild);
          }
        }, 1200);
      }
    };

    const handleClick = (e) => {
      const card = e.target.closest('.card');
      // const lastCard = stack.value.lastElementChild;
      if (card && card === stack.value.lastElementChild) {
        card.classList.add('swap');

        setTimeout(() => {
          card.classList.remove('swap');
          if(stack.value){
            stack.value.insertBefore(lastCard, stack.value.firstElementChild);
          }
          resetAutoplay();
        }, 1200);
      }
    };

    const resetAutoplay = () => {
      clearInterval(autoplayInterval);
      autoplayInterval = setInterval(moveCard, 4000);
    };

    onMounted(() => {
      if (stack.value) {
        autoplayInterval = window.setInterval(moveCard, 4000);
        stack.value.addEventListener('click', handleClick);
      }
    });


    onUnmounted(() => {
      clearInterval(autoplayInterval);
      stack.value.removeEventListener('click', handleClick);
    });

    return {
      stack,
      cardImages,
      goToHomePage
    };
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400..700&family=Quicksand:wght@300..700&display=swap");

*,
*:before,
*:after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Quicksand", sans-serif;
}

body {
  /* Adjust the gradient to brighter or more saturated colors */
  background-color: #ad9393; /* Consider changing the base color to something lighter */
  background: linear-gradient(145deg, #6677aa 0%, #334455 76%); /* Brighter gradient */
}

main {
  background-image: url('../../public/static/img/background.png'); /* 替换为图片的实际路径 */
  background-size: cover; /* 确保背景图片覆盖整个区域 */
  background-position: center; /* 图片居中显示 */
  background-attachment: fixed; /* 背景图固定，不随页面滚动 */
  background-repeat: no-repeat; /* 禁止背景图重复 */
  width: 100%;
  height: 100%;
  display: grid;
  grid-template-columns: 5fr 4fr;
  grid-template-rows: 1fr;
  place-items: center;
  min-height: 100vh;
  /* background-color: #263a39; */
}

/* Content */

/* #building{
  background:url("../../../src/renwu.png");
  /* width:100%; */
  /* height:100%; */
  /* position:fixed; */
  /* background-size:100% 100%; */
  /* position: absolute;
  right: 0%;
  background-repeat: no-repeat;
 }   */
.content {
  display: flex;
  flex-direction: column;  /* Ensures that children are stacked vertically */
  align-items: flex-start; /* Aligns items to the left */
  padding-left:240px;
  color: #c7c7c7c9;
}
.content p{
  font-family: 'Courier New', Courier, monospace;
}
.content h1, .content p, .btn {
  width: 100%; /* Ensures they take full width of the .content div */
}

.content h1 {
  background-image: url(../../public/static/img/xizangwenzi.png);
  z-index: 0;
  font-family: "Dancing Script", cursive;
  font-size: clamp(2.5rem, 4vw, 6rem);
  font-weight: 700;
  /* background: -webkit-linear-gradient(0deg, #ff8c91, #ffcc6f); */
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  line-height: 1.1;
  margin-bottom: -40px;
  padding-left: 10px;
}

.content p {
  font-size: clamp(0.9rem, 4vw, 1.2rem);
  color: rgb(23, 8, 8);
  line-height: 1.6;
  font-weight: bolder;
  padding-right: 50px;
}

h2, p {
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); /* 添加文字阴影 */
}

.btn {
  background-color: #ff6575; /* A more vivid pink */
  background-image: linear-gradient(-180deg, #ffcc6f, #ff6575);
  font-size: clamp(0.8rem, 8vw, 0.9rem);
  font-weight: 600;
  color: #fff;
  width: max-content;
  outline: 0;
  border: 0;
  border-radius: 6px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 10px 20px;
  margin-top: 26px;
  text-align: center;
  transform: scale(1);
  transition: all 0.2s ease-in;
  cursor: pointer;
  touch-action: manipulation;
  user-select: none;
  -webkit-user-select: none;
  pointer-events: auto;
  position: relative
}

.btn:hover {
  box-shadow: 0 4px 10px rgba(255, 101, 145, 0.6);
  transform: scale(0.98);
}

/* Stacked Cards */

.stack {
  position: relative;
  right:0%;
  top: 10%;
}

.card {
  position: absolute;
  transform: translate(-50%, -50%);
  top: 50%;
  left: 70%;
  width: 350px;
  height: 500px;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 2rem;
  font-family: sans-serif;
  font-size: 10rem;
  background-color: transparent;
  box-shadow: 0 5px 10px 0 rgba(0, 0, 0, 0.25),
  0 15px 20px 0 rgba(0, 0, 0, 0.125);
  transition: transform 0.6s;
  user-select: none;
}

.card img {
  width: 100%;
  height: 100%;
  border-radius: inherit;
  object-fit: cover;
  transition: transform 0.4s;
}

.card:nth-last-child(n + 5) {
  --x: calc(-50% + 90px);
  transform: translate(var(--x), -50%) scale(0.85);
  box-shadow: 0 0 1px 1px rgba(0, 0, 0, 0.01);
}

.card:nth-last-child(4) {
  --x: calc(-50% + 60px);
  transform: translate(var(--x), -50%) scale(0.9);
}

.card:nth-last-child(3) {
  --x: calc(-50% + 30px);
  transform: translate(var(--x), -50%) scale(0.95);
}

.c:nth-last-child(2) {
  --x: calc(-50%);
  transform: translate(var(--x), -50%) scale(1);
}

.card:nth-last-child(1) {
  --x: calc(-50% - 30px);
  transform: translate(var(--x), -50%) scale(1.05);
}

.card:nth-last-child(1) img {
  box-shadow: 0 1px 5px 5px rgba(255, 193, 111, 0.5);
}

.swap {
  animation: swap 1.3s ease-out forwards;
}


@keyframes swap {
  30% {
    transform: translate(calc(var(--x) - 250px), -50%) scale(0.85) rotate(-5deg)
    rotateY(65deg);
    animation-timing-function: ease-in;
  }
  100% {
    transform: translate(calc(var(--x) - 30px), -50%) scale(0.5);
    z-index: -1;
  }
}

/* Media queries for keyframes */

@media (max-width: 1200px) {
  @keyframes swap {
    30% {
      transform: translate(calc(var(--x) - 200px ), -50%) scale(0.85) rotate(-5deg) rotateY(65deg);
    }

    100% {
      transform: translate(calc(var(--x) - 30px), -50%) scale(0.5);
      z-index: -1;
    }
  }
}

@media (max-width: 1050px) {
  @keyframes swap {
    30% {
      transform: translate(calc(var(--x) - 150px), -50%) scale(0.85) rotate(-5deg) rotateY(65deg);
    }

    100% {
      transform: translate(calc(var(--x) - 30px), -50%) scale(0.5);
      z-index: -1;
    }
  }
}

/* Media queries for other classes */

@media (max-width: 1200px) {
  .content {
    padding-left: 80px;
  }

  .content p {
    padding-right: 40px;
  }

  .card {
    width: 250px;
    height: 380px;
  }
}

@media (max-width: 1050px) {
  .content {
    padding-left: 60px;
  }

  .content p {
    line-height: 1.5;
  }

  .card {
    width: 220px;
    height: 350px;
  }
}

@media (max-width: 990px) {
  .content p {
    padding-right: 0;
  }

  .card {
    width: 200px;
    height: 300px;
  }
}

@media (max-width: 950px) {
  main {
    grid-template-columns: 1fr;
    grid-template-rows: 4fr 3fr;
    grid-template-areas:
      "stacked"
      "content";
  }

  .content {
    grid-area: content;
    text-align: center;
    padding: 0 90px;
  }

  .btn {
    margin-bottom: 30px;
  }

  .stack {
    grid-area: stacked;
  }
}

@media (max-width: 650px) {
  main {
    grid-template-rows: 1fr 1fr;
  }

  .content {
    padding: 0 50px;
  }

  .content h1 {
    padding-left: 0;
  }

  .btn {
    padding: 8px 16px;
  }

  .card {
    width: 180px;
    height: 260px;
  }
}
</style>

