import re
import json

html_file = r'm:\DATA\Bisnis\Web-desa\index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove particles-js
content = content.replace('<div id="particles-js"></div>', '')

# Replace grid with list
content = content.replace('<section class="products-grid">', '<section class="products-list">')

# Pattern to extract card data
# We need to find each <article class="card"> ... </article>
card_pattern = re.compile(r'<!-- Lingkungan (\d+) -->\s*<article class="card.*?">.*?</article>', re.DOTALL)

data_map = {
    "1": ("KERIPIK UBI PEDAS MAK KARIN", "Camilan ubi renyah bumbu pedas manis. Tanpa pengawet, rasa autentik dan nagih."),
    "2": ("CEMAL CEMIL NAILUL MUNA", "Variasi camilan tradisional dan modern. Rasa nikmat untuk teman santai keluarga."),
    "3": ("Cucur Azizah Salsabilah", "Kue cucur renyah di pinggir, lembut di tengah. Manis alami dari gula merah pilihan."),
    "4": ("Wajik Bandung Mak Zulfanz", "Wajik ketan legit dengan aroma wangi. Sajian manis khas tradisional yang istimewa."),
    "5": ("Cemilan & Kerajinan Lin Sundari", "Produk kreatif gabungan camilan lezat dan kerajinan tangan lokal yang unik."),
    "6": ("Olahan Nurul A.", "Makanan dan minuman olahan higienis. Segar, bergizi, dan terjaga kualitas rasanya."),
    "8": ("DIMSUM PREMIUM", "Dimsum daging tebal dengan tekstur lembut. Disajikan dengan saus sambal spesial."),
    "9": ("Bakery Widayu Astuti", "Roti panggang segar setiap hari. Tekstur lembut dengan berbagai pilihan rasa favorit."),
    "11": ("Mie Ayam Tebet", "Mie ayam gurih dengan potongan daging besar. Cita rasa asli yang selalu dirindukan."),
    "12": ("KEV & KEZ PAYET", "Jasa payet profesional busana pesta. Detail rapi dan elegan untuk tampil istimewa.")
}

# Instead of regex-replacing the whole article, let's rebuild the products-list content
new_products_html = ""
counter = 1

# List of lingkungan in order
lingkungan_order = ["1", "2", "3", "4", "5", "6", "8", "9", "11", "12"]

# Re-extract data from original content to keep image paths and modal data
# We'll search for the card-image-wrapper for each lingkungan
for ling_id in lingkungan_order:
    # Find the data for this lingkungan in the original content
    pattern = re.compile(fr'<!-- Lingkungan {ling_id} -->.*?data-products="(.*?)".*?data-halal="(.*?)".*?src="(.*?)".*?href="(.*?)"', re.DOTALL)
    match = pattern.search(content)
    if match:
        prod_data = match.group(1)
        halal_data = match.group(2)
        img_src = match.group(3)
        wa_url = match.group(4)
        
        title, desc = data_map.get(ling_id, ("Produk UMKM", "Deskripsi produk segera hadir."))
        num_str = f"{counter:02}"
        
        new_products_html += f"""
            <!-- Product {num_str} -->
            <div class="product-item">
                <div class="product-info">
                    <span class="product-number">{num_str}. {title.upper()}</span>
                    <h2 class="product-title">{title.upper()}</h2>
                    <p class="product-description">{desc}</p>
                    <a href="{wa_url}" class="product-link" target="_blank" rel="noopener noreferrer">TANYA DI WHATSAPP</a>
                </div>
                <div class="product-image-container" data-products='{prod_data}' data-halal='{halal_data}'>
                    <img src="{img_src}" alt="{title}" class="product-image">
                </div>
            </div>
        """
        counter += 1

# Replace the entire products-list section
# Find the start and end of the original section
list_start = content.find('<section class="products-list">')
list_end = content.find('</section>', list_start) + 10 # include closing tag

content = content[:list_start] + f'<section class="products-list">\n{new_products_html}\n</section>' + content[list_end:]

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)
