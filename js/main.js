document.addEventListener('DOMContentLoaded', () => {
    // Intersection Observer for Product Item Fade-in
    const items = document.querySelectorAll('.product-item');
    
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });
    
    items.forEach(item => {
        item.style.opacity = '0';
        item.style.transform = 'translateY(30px)';
        item.style.transition = 'opacity 0.8s ease, transform 0.8s ease';
        observer.observe(item);
    });

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
    document.querySelectorAll('.product-image-container').forEach(container => {
        container.addEventListener('click', () => {
            const productsAttr = container.getAttribute('data-products') || '[]';
            const halalAttr = container.getAttribute('data-halal') || '[]';
            
            // Clean attributes (sometimes single quotes cause issues with JSON.parse if not careful)
            const products = JSON.parse(productsAttr.replace(/'/g, '"'));
            const halal = JSON.parse(halalAttr.replace(/'/g, '"'));
            
            if (products.length === 0) return;
            
            productCarousel.innerHTML = products.map(src => `<img src="${src}" alt="Product Detail">`).join('');
            
            if (halal.length > 0) {
                currentHalalImages = halal;
                btnCheckHalal.style.display = 'inline-block';
            } else {
                currentHalalImages = [];
                btnCheckHalal.style.display = 'none';
            }
            
            productModal.classList.add('show');
            document.body.style.overflow = 'hidden';
        });
    });

    // Zoom Logic
    const handleZoom = (e) => {
        if (e.target.tagName === 'IMG') {
            e.target.classList.toggle('zoomed');
        }
    };

    productCarousel.addEventListener('click', handleZoom);
    halalCarousel.addEventListener('click', handleZoom);

    const resetZoom = () => {
        document.querySelectorAll('.carousel img.zoomed').forEach(img => {
            img.classList.remove('zoomed');
        });
    };

    // Close Modals
    const closeAllModals = () => {
        productModal.classList.remove('show');
        halalModal.classList.remove('show');
        document.body.style.overflow = '';
        resetZoom();
    };

    closeProductBtn.addEventListener('click', closeAllModals);

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

    closeHalalBtn.addEventListener('click', () => {
        halalModal.classList.remove('show');
        productModal.classList.add('show');
        resetZoom();
    });

    window.addEventListener('click', (e) => {
        if (e.target === productModal) closeAllModals();
        if (e.target === halalModal) {
            halalModal.classList.remove('show');
            productModal.classList.add('show');
            resetZoom();
        }
    });
});
