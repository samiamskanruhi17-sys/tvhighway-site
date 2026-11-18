import urllib.request, re

req = urllib.request.Request(
    'https://html.duckduckgo.com/html/?q=site:isfe.eu',
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
)
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        matches = re.findall(r'<a class="result__url"[^>]*href="([^"]+)"', html)
        if not matches:
            matches = re.findall(r'href="([^"]*isfe\.eu[^"]*)"', html)
        for m in matches[:15]:
            print(m)
except Exception as e:
    print('Error:', e)
