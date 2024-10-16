<template>
  
  <main>
    <div class="wave">
        <div class="wave-item wave1"></div>
        <div class="wave-item wave2"></div>
        <div class="wave-item wave3"></div>
    </div>
    <section>
    
    <button class="backbutton" >
      <img @click="backHome" class="arrow" src="/static/img/arrow.png">
    </button>
    
    <h2>云上藏境</h2>
    <p>一体化的，帮助你了解藏族地区发展，了解景点、经济、发展的一站式平台。</p>
    <div class="cards">
      <div class="card" v-for="member in teamMembers" :key="member.name">
        <div class="card-img-wrapper">
          <a :href="member.url"><img :src="member.image" :alt="member.name"></a>
        </div>
<!--        <a href="#" class="social-icon">-->
<!--&lt;!&ndash;          <i :class="member.socialIcon"></i>&ndash;&gt;-->
<!--          <img :src="member.socialIcon">-->
<!--        </a>-->
        <div class="card-content-wrapper">
          <a href="#" class="card-content">
            <h3>{{ member.name }}</h3>
            <p>{{ member.role }}</p>
            <div>
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M17.25 8.25 21 12m0 0-3.75 3.75M21 12H3" />
              </svg>
            </div>
          </a>
        </div>
      </div>
    </div>
  </section>
  </main>
</template>

<script>
import {useRouter} from "vue-router/composables";

export default {
  data() {
    return {
      teamMembers: [
        {
          name: '藏地景致',
          role: '旅游胜地',
          image: '/static/img/mountain.jpeg',
          socialIcon: 'fa-brands fa-facebook-f',
          // url: '/#/travel'
          url:'/#/baike'
        },
        // Add more members as needed
        {
          name: '藏百科',
          role: '预测发展',
          image: '/static/img/background-home.jpg',
          socialIcon: 'fa-brands fa-facebook-f',
          // url: '/#/eco',
          url:'/#/dict'
          // url:'/#/baike'
        },
        {
          name: '可视化大屏',
          role: '纵览发展',
          image: '/static/img/zx1.png',
          socialIcon: '/static/img/_map.png',
          url: '/#/screenPage'
        },
        {
          name: 'AI',
          role: '智能交互',
          image: '/static/img/AI.png',
          socialIcon: 'fa-brands fa-facebook-f',
          url: '/#/ai'
        },

      ]
    }
  },
  mounted() {
    this.router = useRouter()
  },
  methods:{
    backHome() {
      this.router.push({ name: 'Welcome' });
    }
  }
}
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;800&display=swap");
/* Include the rest of your CSS here */
@mixin mQ($rem) {
  @media screen and (min-width: $rem) {
    @content;
  }
}

.backbutton {
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


* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  background: #e8eaef;
  min-height: 100vh;
}

a {
  text-decoration: none;
}

img {
  max-width: 100%;
  display: block;
  aspect-ratio: 1/1;
  object-fit: cover;
  object-position: top;
}

body {

}


section {
  
  font-family: "Poppins", sans-serif;
  font-weight: 300;
  font-style: normal;
  padding-block: min(20vh, 5rem);
  text-align: center;
  width: calc(min(90rem, 90%));
  margin-inline: auto;

  p,h2,h3 {
    letter-spacing: 0.035rem;
  }

  p {
    line-height: 1.7;
    color: #FF6347;
    max-width: 70rem;
    margin: 0 auto;
    font-size: clamp(0.9rem, 0.825rem + 0.3vw, 1.2rem);
  }

  h2 {
    font-size: clamp(3rem, 2.4286rem + 2.2857vw, 5rem);
    color: #274472; /* 藏蓝色 */
    text-transform: capitalize;
    font-weight: 600;
    line-height: 1;
    margin-bottom: 1rem;
  }

  .cards {
    margin-top: 4rem;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(min(16rem, 100%), 1fr));
    gap: 2rem;

    @include mQ(51rem) {
      gap: 3.5rem;
    }

    .card {
      position: relative;
      text-align: left;

      .social-icon {
        //background: #111;
        padding: 1rem 1.75rem;
        display: inline-block;
        position: absolute;
        left: 0;

        i {
          color: #fff;
          font-size: 1.4rem;
        }

        &:hover i {
          color: #003ef5;
        }
      }

      img {
        filter: grayscale(50%);
        transition: 0.5s ease;

        &:hover {
          filter: grayscale(0%);
          transform: scale(1.2,1.2);
          box-shadow: 20px,20px,0px
          /* margin-top: 90px; */
        }
      }

      .card-content-wrapper {
        margin-left: auto;
        max-width: 90%;

        .card-content {
          display: block;
          background: white;
          transition: 0.5s ease;
          padding: 4.5rem 2rem 0 3.2rem;

          > div {
            text-align: right;
          }

          h3,
          p {
            text-transform: capitalize;
          }

          h3 {
            font-size: clamp(1.15rem, 1.1071rem + 0.1714vw, 1.3rem);
            font-weight: 800;
            color: #111;
          }

          p {
            color: #454545;
            font-size: 0.9rem;
          }

          svg {
            display: inline-block;
            text-align: right;
            width: 60px;
            color: #003ef5;
          }
        }
      }

      /*hover states*/

      .card-img-wrapper:hover ~ .card-content-wrapper .card-content {
        background: #003ef5;

        h3,
        p,
        svg {
          color: #fff;
        }
      }

      .card-content-wrapper:hover .card-content {
        background: #003ef5;

        h3,
        p,
        svg {
          color: #fff;
        }
      }
    }
  }
}

* {
    padding: 0px;
    margin: 0px;

}

.wave {
    position: fixed;
    bottom: 0px;
    height: 110px;
    width: 100%;
    overflow: hidden;
    background:
        repeating-linear-gradient(to bottom, #fff, #90cef1);
}

.wave .wave-item {
    position: absolute;
    width: 200%;
    height: 100%;
    background-size: 50% 100%;
    opacity: 0.4;

}

.wave .wave1 {
    top: 20px;
    left: -100%;
    opacity: 0.2;
    animation: to-right 15s infinite linear;
    background-image: url(../assets/css/images/wave1.png);
}

.wave .wave2 {
    top: 30px;
    left: 0;
    opacity: 0.3;
    animation: to-left 25s infinite linear;
    background-image: url(../assets/css/images/wave2.png);
}

.wave .wave3 {
    top: 45px;
    left: -100%;
    animation: to-right 35s infinite linear;
    background-image: url(../assets/css/images/wave3.png);
}


@keyframes to-right {
    0% {
        transform: translateX(0) translateZ(0) scaleY(1)
    }

    50% {
        transform: translateX(25%) translateZ(0) scaleY(0.7)
    }

    100% {
        transform: translateX(50%) translateZ(0) scaleY(1)
    }
}

@keyframes to-left {
    from {
        transform: translate(0%, 0px);
    }

    to {
        transform: translate(-50%, 0px);
    }
}
</style>
