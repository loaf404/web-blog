var slideshows = document.querySelectorAll('[data-component="slideshow"]'); // call slidshow data-component
slideshows.forEach(initSlideShow);

function initSlideShow(slideshow) { // slideshow function

    var slides = document.querySelectorAll(`#${slideshow.id} [role="list"] .slide`);

    var index = 0, time = 5000; // set slide time
    slides[index].classList.add('active');

    setInterval( () => { // slide every 5 second
        slides[index].classList.remove('active');
        
        index++;
        if (index === slides.length) index = 0;

        slides[index].classList.add('active');

    }, time);
}