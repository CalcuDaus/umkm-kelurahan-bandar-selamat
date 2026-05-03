import re

html_path = r'm:\DATA\Bisnis\Web-desa\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

descriptions = {
    "KERIPIK UBI PEDAS MAK KARIN": "Camilan keripik ubi renyah dengan bumbu pedas manis rahasia yang bikin ketagihan. Dibuat dari ubi pilihan tanpa pengawet.",
    "CEMAL CEMIL NAILUL MUNA": "Berbagai variasi camilan tradisional dan modern dengan rasa yang autentik. Cocok untuk menemani waktu santai Anda bersama keluarga.",
    "Cucur Azizah Salsabilah": "Kue cucur legendaris dengan tekstur yang lembut di tengah dan renyah di pinggir. Aroma gula merah yang khas dan manisnya pas.",
    "Wajik Bandung Original Mak Zulfanz": "Wajik ketan khas Bandung dengan balutan kertas warna-warni. Tekstur legit dan rasa manis alami dari gula kelapa murni.",
    "Cemilan & Kerajinan Lin Sundari": "Produk kreatif yang menggabungkan kelezatan camilan rumahan dengan keindahan kerajinan tangan lokal yang unik.",
    "Makanan & Minuman Olahan Nurul A.": "Berbagai olahan makanan dan minuman segar berkualitas tinggi yang diproses dengan higienis untuk menjaga rasa dan nutrisi.",
    "DIMSUM": "Dimsum premium dengan isian daging melimpah dan tekstur yang sangat lembut. Disajikan dengan saus sambal spesial yang menggugah selera.",
    "Bakery Widayu Astuti": "Roti dan kue panggang segar setiap hari dengan bahan-bahan pilihan. Lembut, wangi, dan tersedia dalam berbagai varian rasa.",
    "Mie Ayam Tebet": "Mie ayam dengan bumbu rempah khas yang gurih, potongan ayam yang besar, dan mie yang kenyal. Cita rasa otentik yang selalu dirindukan.",
    "KEV & KEZ PAYET": "Jasa pemasangan payet profesional untuk berbagai busana pesta dan formal. Detail yang rapi dan desain yang elegan untuk penampilan Anda."
}

for title, desc in descriptions.items():
    # Find the title and insert description after it
    pattern = re.escape(f'<h2 class="product-title">{title}</h2>')
    replacement = f'<h2 class="product-title">{title}</h2>\n                        <p class="product-description">{desc}</p>'
    content = re.sub(pattern, replacement, content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
