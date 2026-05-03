import os

js_code = """
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

    // Close Product Modal
    closeProductBtn.addEventListener('click', () => {
        productModal.classList.remove('show');
        document.body.style.overflow = ''; // Restore scrolling
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
        }
    });

    // Close Halal Modal
    closeHalalBtn.addEventListener('click', () => {
        halalModal.classList.remove('show');
        // Bring back product modal
        productModal.classList.add('show');
    });

    // Close Modals on outside click
    window.addEventListener('click', (e) => {
        if (e.target === productModal) {
            productModal.classList.remove('show');
            document.body.style.overflow = '';
        }
        if (e.target === halalModal) {
            halalModal.classList.remove('show');
            productModal.classList.add('show');
        }
    });
"""

js_file = r'm:\DATA\Bisnis\Web-desa\js\main.js'

with open(js_file, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to insert this before the final `});` of `document.addEventListener('DOMContentLoaded', () => { ... });`
# So let's replace the last `});` with `js_code + '\n});'`

if content.endswith('});\n') or content.endswith('});'):
    # Remove the last `});` and append
    new_content = content.rstrip()[:-3] + js_code + '\n});\n'
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("JS Appended Successfully")
else:
    print("Error: Could not find the closing DOMContentLoaded block.")
