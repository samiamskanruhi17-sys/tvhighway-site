with open('scratch/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_nav = '''            <ul class="nav-menu">
                <li><a href="#history">Our History</a></li>
                <li><a href="#mission">Philanthropic Mission</a></li>
                <li><a href="#programs">Youth Academy</a></li>
                <li><a href="#facilities">Har-Tru Courts</a></li>
                <li><a href="#match-center">Live Match Desk</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>'''

new_nav = '''            <ul class="nav-menu">
                <li><a href="/">Home</a></li>
                <li><a href="/history.html">Foundation History</a></li>
                <li><a href="/facilities.html">Har-Tru Facilities</a></li>
                <li><a href="/programs.html">Youth Programs</a></li>
                <li><a href="/contact.html">Contact & Location</a></li>
                <li><a href="#match-center" style="color: var(--clay-orange);">Live Match Desk</a></li>
            </ul>'''

if old_nav in html:
    html = html.replace(old_nav, new_nav)
    with open('scratch/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Updated index.html nav successfully!')
else:
    print('old_nav not found')
