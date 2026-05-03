document.addEventListener('DOMContentLoaded', () => {
    // Intersection Observer for Card Fade-in Animation
    const cards = document.querySelectorAll('.card');
    
    // Create the observer
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            // If the element is visible
            if (entry.isIntersecting) {
                // Add the 'visible' class to trigger animation
                entry.target.classList.add('visible');
                // Unobserve the element so animation only happens once
                observer.unobserve(entry.target);
            }
        });
    }, {
        root: null, // Use viewport
        rootMargin: '0px',
        threshold: 0.1 // Trigger when 10% of element is visible
    });
    
    // Observe all cards
    cards.forEach(card => {
        observer.observe(card);
    });

    // Header scroll effect
    const header = document.querySelector('.header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.style.background = 'rgba(255, 255, 255, 0.95)';
            header.style.backdropFilter = 'blur(10px)';
            header.style.boxShadow = '0 4px 20px rgba(0,0,0,0.05)';
        } else {
            header.style.background = 'transparent';
            header.style.backdropFilter = 'none';
            header.style.boxShadow = 'none';
        }
    });

    // Initialize Particles.js
    if (typeof particlesJS !== 'undefined') {
        particlesJS('particles-js', {
            "particles": {
                "number": {
                    "value": 60,
                    "density": {
                        "enable": true,
                        "value_area": 800
                    }
                },
                "color": {
                    "value": "#95a5a6" // Grey
                },
                "shape": {
                    "type": "circle",
                    "stroke": {
                        "width": 0,
                        "color": "#000000"
                    }
                },
                "opacity": {
                    "value": 0.4,
                    "random": false,
                    "anim": {
                        "enable": false
                    }
                },
                "size": {
                    "value": 4,
                    "random": true,
                    "anim": {
                        "enable": false
                    }
                },
                "line_linked": {
                    "enable": true,
                    "distance": 150,
                    "color": "#95a5a6",
                    "opacity": 0.3,
                    "width": 1
                },
                "move": {
                    "enable": true,
                    "speed": 2,
                    "direction": "none",
                    "random": false,
                    "straight": false,
                    "out_mode": "out",
                    "bounce": false,
                    "attract": {
                        "enable": false
                    }
                }
            },
            "interactivity": {
                "detect_on": "canvas",
                "events": {
                    "onhover": {
                        "enable": true,
                        "mode": "grab"
                    },
                    "onclick": {
                        "enable": true,
                        "mode": "push"
                    },
                    "resize": true
                },
                "modes": {
                    "grab": {
                        "distance": 140,
                        "line_linked": {
                            "opacity": 0.8
                        }
                    },
                    "push": {
                        "particles_nb": 4
                    }
                }
            },
            "retina_detect": true
        });
    }

    // Modal Logic
    const productModal = document.getElementById('product-modal');
    const halalModal = document.getElementById('halal-modal');
    const productCarousel = document.getElementById('product-carousel');
    const halalCarousel = document.getElementById('halal-carousel');
    const btnCheckHalal = document.getElementById('btn-check-halal');
    
    const closeProductBtn = document.querySelector('.close-modal');
    const closeHalalBtn = document.querySelector('.close-halal');
    
    let currentHalalImages = [];

    // Open Product Modal
    document.querySelectorAll('.card-image-wrapper').forEach(wrapper => {
        wrapper.addEventListener('click', () => {
            const products = JSON.parse(wrapper.getAttribute('data-products') || '[]');
            const halal = JSON.parse(wrapper.getAttribute('data-halal') || '[]');
            
            if (products.length === 0) return; // No products to show
            
            // Populate Product Carousel
            productCarousel.innerHTML = products.map(src => `<img src="${src}" alt="Product Detail">`).join('');
            
            // Setup Halal Button
            if (halal.length > 0) {
                currentHalalImages = halal;
                btnCheckHalal.style.display = 'block';
            } else {
                currentHalalImages = [];
                btnCheckHalal.style.display = 'none';
            }
            
            productModal.classList.add('show');
            document.body.style.overflow = 'hidden'; // Prevent scrolling
        });
    });

    // Zoom Logic for Carousel Images
    const handleZoom = (e) => {
        if (e.target.tagName === 'IMG') {
            e.target.classList.toggle('zoomed');
        }
    };

    productCarousel.addEventListener('click', handleZoom);
    halalCarousel.addEventListener('click', handleZoom);

    // Reset Zoom function
    const resetZoom = () => {
        document.querySelectorAll('.carousel img.zoomed').forEach(img => {
            img.classList.remove('zoomed');
        });
    };

    // Close Product Modal
    closeProductBtn.addEventListener('click', () => {
        productModal.classList.remove('show');
        document.body.style.overflow = ''; // Restore scrolling
        resetZoom();
        // Wait for transition before clearing content
        setTimeout(() => {
            if(!productModal.classList.contains('show')) productCarousel.innerHTML = '';
        }, 300);
    });

    // Open Halal Modal
    btnCheckHalal.addEventListener('click', () => {
        if (currentHalalImages.length > 0) {
            halalCarousel.innerHTML = currentHalalImages.map(src => `<img src="${src}" alt="Sertifikat Halal">`).join('');
            // Hide product modal, show halal modal
            productModal.classList.remove('show');
            halalModal.classList.add('show');
            resetZoom();
        }
    });

    // Close Halal Modal
    closeHalalBtn.addEventListener('click', () => {
        halalModal.classList.remove('show');
        // Bring back product modal
        productModal.classList.add('show');
        resetZoom();
    });

    // Close Modals on outside click
    window.addEventListener('click', (e) => {
        if (e.target === productModal) {
            productModal.classList.remove('show');
            document.body.style.overflow = '';
            resetZoom();
        }
        if (e.target === halalModal) {
            halalModal.classList.remove('show');
            productModal.classList.add('show');
            resetZoom();
        }
    });

});
