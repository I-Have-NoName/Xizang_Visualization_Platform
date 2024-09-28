<template>
	
	<main>
        <div class="swiper-list-card swiper-list">	
		<div class="swiper-main-card swiper-main"></div>
		<img id="prev-card" class="btn leftBtn" src="static\img\arrow.png" alt="">
		<img id="next-card" class="btn rightBtn" src="static\img\arrow2.png" alt="">
	</div>
	<div class="swiper-list-stack swiper-list">	
		<div class="swiper-main-stack swiper-main"></div>
		<img id="prev-stack" class="btn leftBtn" src="static\img\arrow.png" alt="">
		<img id="next-stack" class="btn rightBtn" src="static\img\arrow2.png" alt="">
	</div>
    </main>

</template>
<script >
    import  '../utils/slide_card.js';
	let imgArr = [{
			url: '#',
			imgPath: 'static/img/background-home.jpg'
		},
		{
			url: '#',
			imgPath: 'static/img/Potala_palace23.jpg'
		},
		{
			url: '#',
			imgPath: 'static/img/mountain.jpg'
		},
		{
			url: '#',
			imgPath: 'static/img/dazhaosi.jpg'
		},
		{
			url: '#',
			imgPath: 'static/img/background-travel.webp'
		}
	];
	// let imgArr = ['i.jpg', 'o.jpg', 'q.jpeg'];
	// let imgArr = ['i.jpg', 'o.jpg'];
	// let imgArr = ['i.jpg'];
	new Swiper({
		imgArr: imgArr, 
		imgWidth: 320, 
		aniTime: 1000, 
		intervalTime: 1500, 
		scale: 0.8, 
		autoplay: false,
		gap: 0,
      	clsSuffix: '-card'
	}).init();


	new Swiper({
		imgArr: imgArr, 
		imgWidth: 320, 
		aniTime: 1000, 
		intervalTime: 1500, 
		scale: 0.8, 
		autoplay: false,
		gap: -200,
      	clsSuffix: '-stack'
	}).init();
</script>
