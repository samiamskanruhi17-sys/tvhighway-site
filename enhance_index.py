with open('scratch/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add featured court image in history article
target_history = '<h3>The Origin & Vision of Vineyard Youth Tennis (1997–Present)</h3>'
replacement_history = '''<h3>The Origin & Vision of Vineyard Youth Tennis (1997–Present)</h3>
                    <img src="https://images.unsplash.com/photo-1595435934249-5df7ed86e1c0?auto=format&fit=crop&w=1000&q=80" alt="Har-Tru Red Clay Courts Oak Bluffs" style="width:100%; height:320px; object-fit:cover; border-radius:8px; margin:16px 0; border:1px solid #e5e7eb;">'''

# Add clubhouse image in facilities article
target_facility = '<h3>World-Class Har-Tru Clay Courts & Facilities</h3>'
replacement_facility = '''<h3>World-Class Har-Tru Clay Courts & Facilities</h3>
                    <img src="https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&w=1000&q=80" alt="Chuck Sullivan Designed Clubhouse" style="width:100%; height:320px; object-fit:cover; border-radius:8px; margin:16px 0; border:1px solid #e5e7eb;">'''

if target_history in html and 'Har-Tru Red Clay Courts Oak Bluffs' not in html:
    html = html.replace(target_history, replacement_history)
if target_facility in html and 'Chuck Sullivan Designed Clubhouse' not in html:
    html = html.replace(target_facility, replacement_facility)

with open('scratch/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Enhanced index.html with featured images!')
