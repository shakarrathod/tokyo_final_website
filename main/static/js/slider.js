const customSlider = document.querySelector('.custom-slider');
const customSlides = document.querySelectorAll('.custom-slide');
const prevBtn = document.querySelector('.custom-prev-btn');
const nextBtn = document.querySelector('.custom-next-btn');

let currentIndex = 0;
const slideDuration = 8000; // 4 seconds

function showSlide(index) {
    customSlider.style.transform = `translateX(-${index * 100}%)`;
}

function nextSlide() {
    currentIndex = (currentIndex + 1) % customSlides.length;
    showSlide(currentIndex);
}

function prevSlide() {
    currentIndex = (currentIndex - 1 + customSlides.length) % customSlides.length;
    showSlide(currentIndex);
}

prevBtn.addEventListener('click', () => {
    prevSlide();
    resetAutoSlide();
});

nextBtn.addEventListener('click', () => {
    nextSlide();
    resetAutoSlide();
});

// Auto-slide functionality
let autoSlide = setInterval(nextSlide, slideDuration);

function resetAutoSlide() {
    clearInterval(autoSlide);
    autoSlide = setInterval(nextSlide, slideDuration);
}

// Initialize the first slide
showSlide(currentIndex);


function scrollToTop() {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  }

document.querySelector('.hamburger').addEventListener('click', function () {
    const navLinks = document.querySelector('.nav-links');
    navLinks.classList.toggle('active');
});


function toggleMenu() {
  const navLinks = document.querySelector('.nav-links');
  navLinks.classList.toggle('active');
  console.log(toggleMenu)
}


function toggleMenu() {
  const navLinks = document.querySelector('.nav-links');
  if (navLinks) {
      navLinks.classList.toggle('active');
  } else {
      console.error("No element with class 'nav-links' found.");
  }
}


