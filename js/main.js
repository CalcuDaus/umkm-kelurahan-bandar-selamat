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
            header.style.background = 'linear-gradient(to bottom, var(--white) 0%, var(--bg-color) 100%)';
            header.style.boxShadow = '0 4px 20px rgba(0,0,0,0.03)';
        } else {
            header.style.background = 'linear-gradient(to bottom, var(--light-green) 0%, var(--bg-color) 100%)';
            header.style.boxShadow = 'none';
        }
    });
});
