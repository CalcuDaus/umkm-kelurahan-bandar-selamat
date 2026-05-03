import re
import os

html_path = r'm:\DATA\Bisnis\Web-desa\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

mapping = {
    "lingkungan-1": "keripik-ubi-pedas-mak-karin.png",
    "lingkungan-2": "cemal-cemil-nailul-muna.png",
    "lingkungan-3": "cucur-Azizah-salsabilah.png",
    "lingkungan-4": "wajik-bandung-original-Mak-Zulfanz.png",
    "lingkungan-5": "cemilan-dan-kerajinan-tangan-lin-sundari.png",
    "lingkungan-6": "makanan-dan-minuman-Nurul-Andeni-Lubis.png",
    "lingkungan-8": "dimsum.png",
    "lingkungan-9": "bakery-Widayu-Astuti.png",
    "lingkungan-11": "mie-ayam-tebet.png",
    "lingkungan-12": "kev-dan-payet.png"
}

for ling, filename in mapping.items():
    # Update main src
    pattern_src = re.compile(fr'src="attachment/{ling}/.*?"')
    content = pattern_src.sub(f'src="attachment/{ling}/{filename}"', content)
    
    # Update data-products (it's a JSON array in the attribute)
    # Finding the product-image-container for this lingkungan
    # The counter is used in the HTML: <!-- Product 01 -->, <!-- Product 02 -->, etc.
    # But ling-id is also unique in the path.
    pattern_data = re.compile(fr'data-products=\'\[&quot;attachment/{ling}/.*?&quot;\]\'')
    content = pattern_data.sub(f"data-products='[&quot;attachment/{ling}/{filename}&quot;]'", content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
