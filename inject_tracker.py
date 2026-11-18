import os, re

histats_code = '''
<!-- Histats.com  START  (aync)-->
<script type="text/javascript">var _Hasync= _Hasync|| [];
_Hasync.push(['Histats.start', '1,728028,4,0,0,0,00010000']);
_Hasync.push(['Histats.fasi', '1']);
_Hasync.push(['Histats.track_hits', '']);
(function() {
var hs = document.createElement('script'); hs.type = 'text/javascript'; hs.async = true;
hs.src = ('//s10.histats.com/js15_as.js');
(document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(hs);
})();</script>
<noscript><a href="/" target="_blank"><img  src="//sstatic1.histats.com/0.gif?728028&101" alt="page hit counter" border="0"></a></noscript>
<!-- Histats.com  END  -->
'''

files = ['index.html', 'history.html', 'facilities.html', 'programs.html', 'contact.html']

for fn in files:
    path = os.path.join('scratch', fn)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove old histats if already present
        if 'Histats.start' not in content:
            content = content.replace('</body>', histats_code + '\n</body>')
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Injected Histats into {fn}')
        else:
            print(f'Histats already in {fn}')
