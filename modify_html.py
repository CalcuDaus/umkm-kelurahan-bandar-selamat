import re
import json

html_file = r'm:\DATA\Bisnis\Web-desa\index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Dictionary of data for each lingkungan
data_map = {
    "1": {
        "products": ["attachment/lingkungan-1/kripik-mak-karin.jpeg"],
        "halal": ["attachment/lingkungan-1/sertif-halal-lingkungan1_1.jpg", "attachment/lingkungan-1/sertif-halal-lingkungan1_2.jpg"]
    },
    "2": {
        "products": ["attachment/lingkungan-2/cemal-cemil-nailul-muna.jpeg"],
        "halal": ["attachment/lingkungan-2/sertif-halal-lingkungan2_1.jpg", "attachment/lingkungan-2/sertif-halal-lingkungan2_2.jpg", "attachment/lingkungan-2/sertif-halal-lingkungan2_3.jpg"]
    },
    "3": {
        "products": ["attachment/lingkungan-3/cucur-azizah-salsabilah1.jpeg", "attachment/lingkungan-3/cucur-azizah-salsabilah2.jpeg"],
        "halal": ["attachment/lingkungan-3/sertif-halal-lingkungan3_1.jpg", "attachment/lingkungan-3/sertif-halal-lingkungan3_2.jpg", "attachment/lingkungan-3/sertif-halal-lingkungan3_3.jpg"]
    },
    "4": {
        "products": ["attachment/lingkungan-4/wajik-bandung-orginial-mak-zulfanz.jpeg"],
        "halal": []
    },
    "5": {
        "products": ["attachment/lingkungan-5/cemilan-dan-kerajinan-tangan-lilin-sundari.jpeg"],
        "halal": ["attachment/lingkungan-5/sertif-halal-lingkungan5.jpg"]
    },
    "6": {
        "products": ["attachment/lingkungan-6/makanan-dan-minuman-olahan.jpeg"],
        "halal": ["attachment/lingkungan-6/sertif-halal-lingkungan6.jpg"]
    },
    "7": {
        "products": [],
        "halal": []
    },
    "8": {
        "products": ["attachment/lingkungan-8/WhatsApp Image 2026-05-01 at 6.04.21 PM.jpeg"],
        "halal": ["attachment/lingkungan-8/sertif-halal-lingkungan8.jpg"]
    },
    "9": {
        "products": ["attachment/lingkungan-9/WhatsApp Image 2026-05-01 at 6.05.33 PM.jpeg"],
        "halal": ["attachment/lingkungan-9/sertif-halal-lingkungan9.jpg"]
    },
    "10": {
        "products": [],
        "halal": []
    },
    "11": {
        "products": ["attachment/lingkungan-11/WhatsApp Image 2026-05-01 at 6.10.40 PM.jpeg"],
        "halal": ["attachment/lingkungan-11/sertif-halal-lingkungan11.jpg"]
    }
}

# The block to find:
# <a href="..." class="card-link" ...>
#     <div class="card-image-wrapper"> ... </div>
#     <div class="card-body"> ... </div>
# </a>

pattern = re.compile(
    r'<article class="card(?P<placeholder>.*?)">\s*'
    r'<a href="(?P<url>[^"]+)" class="card-link" target="_blank" rel="noopener noreferrer">\s*'
    r'<div class="card-image-wrapper">\s*'
    r'(?P<image_content>.*?)\s*'
    r'<span class="badge">Lingkungan (?P<lingkungan>\d+)</span>\s*'
    r'</div>\s*'
    r'<div class="card-body">',
    re.DOTALL
)

def replacer(match):
    placeholder = match.group('placeholder')
    url = match.group('url')
    img_content = match.group('image_content')
    lingkungan = match.group('lingkungan')
    
    data = data_map.get(lingkungan, {"products": [], "halal": []})
    prod_json = json.dumps(data["products"]).replace('"', '&quot;')
    halal_json = json.dumps(data["halal"]).replace('"', '&quot;')
    
    return (
        f'<article class="card{placeholder}">\n'
        f'                <div class="card-image-wrapper" data-products="{prod_json}" data-halal="{halal_json}" style="cursor: pointer;">\n'
        f'                    {img_content}\n'
        f'                    <span class="badge">Lingkungan {lingkungan}</span>\n'
        f'                </div>\n'
        f'                <a href="{url}" class="card-link" target="_blank" rel="noopener noreferrer">\n'
        f'                    <div class="card-body">'
    )

new_content = pattern.sub(replacer, content)

# Also need to replace the placeholder cards that don't have <a href...
# Wait, placeholder cards look like:
# <article class="card placeholder-card">
#     <div class="card-image-wrapper">
#         <div class="placeholder-image"> ... </div>
#         <span class="badge">Lingkungan 7</span>
#     </div>
#     <div class="card-body"> ... </div>
# </article>
# My pattern only matches cards with `<a href=...>` which is fine! Placeholders don't have `<a href...>` and don't need modals.

# Now replace "Pesan di WhatsApp" to "Tanya-tanya di Whatsapp"
new_content = new_content.replace('Pesan di WhatsApp', 'Tanya-tanya di Whatsapp')

# Add modal HTML
modal_html = """

    <!-- Modals -->
    <div id="product-modal" class="modal">
        <div class="modal-content">
            <span class="close-modal">&times;</span>
            <div class="modal-body">
                <div id="product-carousel" class="carousel"></div>
                <button id="btn-check-halal" class="btn-halal" style="display: none;">Cek Sertifikat Halal</button>
            </div>
        </div>
    </div>

    <div id="halal-modal" class="modal">
        <div class="modal-content">
            <span class="close-halal">&times;</span>
            <div class="modal-body">
                <h3 style="text-align: center; margin-bottom: 1rem; color: var(--primary-green);">Sertifikat Halal</h3>
                <div id="halal-carousel" class="carousel"></div>
            </div>
        </div>
    </div>
"""

new_content = new_content.replace('</section>\n    </main>', '</section>\n    </main>' + modal_html)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Updated index.html")
