#!/usr/bin/env python3
"""Generates the static pages in ../site from one template so header/footer stay identical.
Run:  python3 tools/build.py   (output goes to ./site). Edit content below, not the generated HTML."""
import os, html, time
ASSET_V = str(int(time.time()))   # cache-busting for styles.css / script.js, new on every build

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'site')
BASE = 'https://cellact.org/'
ORG = '一般社団法人 CELLACT'
TEL = '03-3289-0202'

NAV = [('index.html', 'TOP'), ('business.html', 'BUSINESS'), ('company.html', 'COMPANY'),
       ('recruit.html', 'RECRUIT'), ('news-archive.html', 'NEWS')]

NEWS = [  # newest first
    dict(slug='news-20270110-recruit', date='2027.01.10', tag='採用情報', warm=True, img='photo_glass1.webp',
         title='医療スタッフ募集のお知らせ',
         excerpt='看護師・受付スタッフを募集しています。',
         body='''<p>再生医療の現場をともに支える仲間を募集します。患者様に寄り添い、技術と温かさを両立させた医療を届けることのできる方をお待ちしています。</p>
<ul><li>募集職種：看護師（正看護師・准看護師）、受付スタッフ</li><li>勤務形態：正社員（試用期間あり）</li><li>勤務地：セルアクト クリニック銀座（CELLACT CLINIC GINZA）（東京都中央区銀座）</li><li>歓迎スキル：英語対応、再生医療・美容医療経験、ホスピタリティを重視した接遇</li></ul>
<p>教育・研修はチームでサポートし、未経験の方も段階的に業務を習得できる環境を整えています。ライフステージに合わせた働き方についてもお気軽にご相談ください。</p>
<p>応募・詳細は <a href="recruit.html">採用情報</a> をご覧のうえ、<a href="contact.php">お問い合わせ</a> からご連絡ください。担当者より折り返しご案内いたします。</p>'''),
    dict(slug='news-20270101-rename', date='2027.01.01', tag='クリニック情報', warm=False, img='photo_logo.webp',
         title='N2クリニック銀座本院は「セルアクト クリニック銀座（CELLACT CLINIC GINZA）」へ名称変更しました。',
         excerpt='N2クリニック銀座本院は、この度「セルアクト クリニック銀座（CELLACT CLINIC GINZA）」へ名称を変更いたしました。',
         body='''<p>日頃よりご愛顧いただき、誠にありがとうございます。</p>
<p>N2クリニック銀座本院は、この度、<strong>「セルアクト クリニック銀座（CELLACT CLINIC GINZA）」</strong>へ名称を変更いたしました。</p>
<ul><li>新名称：セルアクト クリニック銀座（CELLACT CLINIC GINZA）</li><li>所在地：〒104-0061 東京都中央区銀座6-6-5 HULIC &amp; New GINZA NAMIKI6 11F</li><li>電話番号：<a href="tel:0332890202">03-3289-0202</a>（変更ありません）</li></ul>
<p>住所・電話番号に変更はございません。今後とも変わらぬご支援を賜りますよう、お願い申し上げます。</p>
<p>ご不明な点は、<a href="contact.php">お問い合わせフォーム</a>、またはお電話でお寄せください。</p>'''),
    dict(slug='news-20270101-renewal', date='2027.01.01', tag='お知らせ', warm=False, img='news_renewal.webp',
         title='公式サイトをリニューアルしました。',
         excerpt='一般社団法人 CELLACT の公式サイトを、新しいデザインでリニューアルしました。',
         body='''<p>いつもご覧いただき、ありがとうございます。一般社団法人 CELLACT の公式サイトを、全面的にリニューアルいたしました。</p>
<p>再生医療に取り組む私たちの考え方や、事業の内容を、よりわかりやすくお伝えできるよう、デザインと構成を見直しています。</p>
<ul><li>事業内容のページを新設し、幹細胞療法・免疫細胞療法・幹細胞培養上清療法を、それぞれご紹介しています。</li><li>会社概要のページに、ロゴに込めた想いを加えました。</li><li>スマートフォンでも読みやすいよう、文字の大きさや、余白、ボタンの配置を最適化しています。</li><li>お問い合わせフォームは、入力、確認、完了の3ステップで、24時間受け付けています。</li></ul>
<p>今後も、お知らせや、取り組みを、随時更新してまいります。ご意見・ご感想がございましたら、お気軽に <a href="contact.php">お問い合わせ</a> ください。</p>'''),
]

SERVICES = [
    dict(id='stem', en='STEM CELL TREATMENT', name='幹細胞療法', img='cellact_stem.webp?v=4', yt=None,
         short='自己の幹細胞を用いた再生医療により、損傷した組織の修復・再生を促します。',
         lead='ご自身の幹細胞を用いた再生医療により、損傷した組織の修復・再生を促します。',
         paras=['幹細胞は、さまざまな細胞に変化する力と、自らを複製する力をもつ細胞です。この性質を医療に活かし、加齢や損傷によって傷んだ組織の回復を支えることを目指します。',
                '治療に用いる細胞は、徹底した品質管理のもとで培養します。一人ひとりの状態やご希望を伺い、診察のうえで治療計画をご提案します。'],
         points=[('どんな治療か', 'ご自身の細胞を用いる再生医療です。'),
                 ('特徴', '細胞の品質と、それを支える技術の信頼性を重視しています。'),
                 ('安全への取り組み', '再生医療等安全性確保法を遵守し、安全かつ高度な実践に努めています。')]),
    dict(id='immune', en='IMMUNE CELL TREATMENT', name='免疫細胞療法', img='cellact_immune.webp?v=3', yt=None,
         short='患者様自身の免疫細胞を活性化させ、体の自然治癒力を高める治療法です。',
         lead='患者様自身の免疫細胞を活性化させ、体の自然治癒力を高める治療法です。',
         paras=['免疫細胞は、体を守る仕組みの中心を担う細胞です。ご自身の免疫細胞を体の外で培養・活性化させ、その働きを高めることを目指します。',
                '培養は、品質管理の行き届いた環境で行います。治療の適応や進め方は、診察のうえで、医師が個別にご説明します。'],
         points=[('どんな治療か', 'ご自身の免疫細胞を活用する再生医療です。'),
                 ('特徴', '一人ひとりの状態に合わせて、治療計画を設計します。'),
                 ('安全への取り組み', '細胞の品質管理と、法令の遵守を徹底しています。')]),
    dict(id='super', en='STEMCELL SUPERNATANT', name='幹細胞培養上清療法', img='cellact_super.webp?v=5', yt=None,
         short='細胞間の情報伝達を担うサイトカインが豊富な培養上清で、細胞本来の活性をサポートします。',
         lead='細胞間の情報伝達を担うサイトカインが豊富な培養上清で、細胞本来の活性をサポートします。',
         paras=['幹細胞培養上清とは、幹細胞を培養する過程で、培養液に分泌される成分を取り出したものです。細胞間の情報伝達を担うサイトカインが豊富に含まれています。',
                '高品質な培養上清を用いることで、機能が低下した細胞に働きかけ、本来の活性をサポートします。当院の培養上清は、クリーンな環境下で製造され、ウイルス検査などの安全管理を徹底したサイトカイン成分です。'],
         points=[('どんな治療か', '幹細胞の培養上清に含まれる成分を用いる治療です。'),
                 ('特徴', '細胞間の情報伝達を担うサイトカインが豊富に含まれます。'),
                 ('安全への取り組み', 'クリーンな環境での製造と、ウイルス検査などの安全管理を徹底しています。')]),
]

CAPSULE_SVG = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'capsule_inline.svg'), encoding='utf-8').read()
ICON_ARROW = '<span class="arrow" aria-hidden="true">→</span>'


def esc(s):
    return html.escape(s, quote=True)


def head(title, desc, path, og_img='images/hero_top.webp', extra_head='', noindex=False):
    full = title if title.startswith(ORG) else f'{title} | {ORG}'
    robots = '<meta name="robots" content="noindex,nofollow">' if noindex else ''
    canon = '' if noindex else f'<link rel="canonical" href="{BASE}{path if path != "index.html" else ""}">'
    return f'''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full)}</title>
<meta name="description" content="{esc(desc)}">
{robots}
{canon}
<meta property="og:type" content="website">
<meta property="og:site_name" content="{ORG}">
<meta property="og:title" content="{esc(full)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{BASE}{og_img}">
<meta property="og:locale" content="ja_JP">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0f6b86">
<link rel="icon" href="images/cellact_logo.png?v=151" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500&amp;family=Noto+Serif+JP:wght@500;600&amp;display=swap">
<link rel="stylesheet" href="styles.css?v=151">
<script>document.documentElement.classList.add('js')</script>
{extra_head}
</head>
<body>
<a class="skip" href="#main">本文へスキップ</a>
'''


def header(current):
    items = ''
    for href, label in NAV:
        cur = ' aria-current="page"' if href == current else ''
        items += f'<li><a href="{href}"{cur}>{label}</a></li>'
    cur = ' aria-current="page"' if current == 'contact.php' else ''
    items += f'<li><a class="nav-cta" href="contact.php"{cur}>CONTACT</a></li>'
    return f'''<header class="site-header">
<div class="container">
<a class="brand" href="index.html" aria-label="{ORG} トップへ"><img src="images/cellact_logo.png?v=151" alt="" width="62" height="66"><span>{ORG}<small>REGENERATIVE MEDICINE</small></span></a>
<button class="menu-btn" aria-expanded="false" aria-controls="gnav" aria-label="メニュー"><span></span></button>
<nav class="gnav" id="gnav" aria-label="メインメニュー"><ul>{items}</ul></nav>
</div>
</header>
'''


def world_band(img, word, pos='50% 50%'):
    return f'''<div class="world-band under" aria-hidden="true"><img src="images/{img}" alt="" loading="lazy" style="object-position:{pos}"></div>
'''


def cta(heading='まずはお気軽にご相談ください'):
    return f'''<section class="section cta under">
<div class="cta-bg" aria-hidden="true"><img src="images/band_arches.webp" alt="" loading="lazy"></div>
<div class="container reveal">
<p class="eyebrow" style="color:#fff;opacity:.85">CONTACT</p>
<h2 class="section-title">{heading}</h2>
<p>治療や採用に関するご質問など、フォームから24時間受け付けています。</p>
<a class="btn btn-primary" href="contact.php">お問い合わせフォームへ {ICON_ARROW}</a>
<div class="tel">TEL <a href="tel:0332890202">{TEL}</a></div>
</div>
</section>
'''


def footer():
    nav = ''.join(f'<li><a href="{h}">{l}</a></li>' for h, l in NAV + [('contact.php', 'CONTACT')])
    return f'''<footer class="site-footer">
<div class="container">
<div class="footer-grid">
<div>
<a class="footer-brand" href="index.html"><img src="images/cellact_logo_white.png?v=151" alt="" width="72" height="76"><b>{ORG}</b></a>
<address>〒104-0061 東京都中央区銀座6-6-5<br>HULIC &amp; New GINZA NAMIKI6 11F<br>TEL <a href="tel:0332890202">{TEL}</a> / FAX 03-3289-0022</address>
</div>
<div><h4>MENU</h4><ul>{nav}</ul></div>
<div><h4>INFORMATION</h4><ul><li><a href="https://cellact.jp/" target="_blank" rel="noopener noreferrer">クリニック公式サイト</a></li><li><a href="privacy.html">プライバシーポリシー</a></li></ul></div>
</div>
<div class="copy"><span>&copy; 2026 {ORG}. All rights reserved.</span></div>
</div>
</footer>
<script src="script.js?v=151" defer></script>
</body>
</html>
'''


def page_hero(en, title, bg, crumbs, pos='50% 50%', flip=False, tall=False, mpos=None):
    mpos = mpos or pos
    bc = ' &gt; '.join(f'<a href="{h}">{l}</a>' for h, l in crumbs[:-1])
    bc = (bc + ' &gt; ' if bc else '') + esc(crumbs[-1][1])
    return f'''<section class="page-hero{" tall" if tall else ""}{" flip" if flip else ""}">
<div class="hero-bg"><img src="images/{bg}?v=14" alt="" width="2041" height="314" style="object-position:{pos};--mpos:{mpos}"></div>
<div class="container" data-en="{en}"><p class="eyebrow">{en}</p><h1>{title}</h1><nav class="breadcrumb" aria-label="パンくず">{bc}</nav></div>
</section>
'''


def section_head(en, title, center=False, lead=''):
    c = ' center' if center else ''
    l = f'<p class="lead">{lead}</p>' if lead else ''
    return f'<div class="section-head{c} reveal"><p class="eyebrow">{en}</p><h2 class="section-title">{title}</h2>{l}</div>'


def write(name, content):
    content = content.replace('styles.css?v=151', 'styles.css?v=' + ASSET_V).replace('script.js?v=151', 'script.js?v=' + ASSET_V)
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        f.write(content)


def news_list(items):
    rows = ''
    for n in items:
        w = ' warm' if n['warm'] else ''
        rows += (f'<li><a href="{n["slug"]}.html"><time datetime="{n["date"].replace(".", "-")}">{n["date"]}</time>'
                 f'<span class="tag{w}">{n["tag"]}</span><span class="ttl">{n["title"]}</span><span class="chev" aria-hidden="true">→</span></a></li>')
    return f'<ul class="news-list reveal">{rows}</ul>'


# ---------------------------------------------------------------- TOP
def build_index():
    cards = ''
    for s in SERVICES:
        cards += f'''<article class="service-card reveal"><a href="business.html#{s["id"]}" style="text-decoration:none;color:inherit;display:flex;flex-direction:column;flex:1">
<div class="thumb"><img src="images/{s["img"]}" alt="" loading="lazy" width="1500" height="857"{" data-pan"}></div>
<div class="body"><span class="en">{s["en"]}</span><h3>{s["name"]}</h3><p>{s["short"]}</p><span class="more" style="color:var(--teal-deep)">詳しく見る</span></div></a></article>'''
    ld = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"Organization","name":"一般社団法人 CELLACT","url":"https://n2cellact.or.jp/","logo":"https://n2cellact.or.jp/images/cellact_logo.png?v=151","telephone":"+81-3-3289-0202","email":"info@cellact.org","address":{"@type":"PostalAddress","postalCode":"104-0061","addressRegion":"東京都","addressLocality":"中央区","streetAddress":"銀座6-6-5 HULIC & New GINZA NAMIKI6 11F","addressCountry":"JP"}}</script>'''
    s = head(f'{ORG} | 再生医療クリニック',
             '再生する力で、健康と希望の未来を創る。幹細胞療法・免疫細胞療法・幹細胞培養上清療法など、再生医療を提供する一般社団法人 CELLACT の公式サイトです。',
             'index.html', extra_head=ld)
    s += header('index.html')
    s += f'''<main id="main">
<section class="hero">
<div class="hero-bg"><picture><source media="(max-width: 820px)" srcset="images/hero_top_sp.webp?v=11" width="6000" height="1000"><img src="images/hero_top.webp?v=246" alt="" width="5400" height="900" fetchpriority="high"></picture></div>
<div class="hero-intro" aria-hidden="true"><div class="hi-veil"></div><div class="hi-logo" data-capsule-intro>{CAPSULE_SVG}</div><button type="button" class="hi-skip">スキップ</button></div>
<div class="container hero-inner">
<p class="hero-eyebrow">CELLACT / REGENERATIVE MEDICINE</p>
<h1>再生する力で、<br>健康と希望の未来を創る。</h1>
<p class="hero-sub">Advancing Health and Hope Through Regeneration.</p>
<div class="hero-actions"><a class="btn btn-primary" href="business.html">事業内容を見る {ICON_ARROW}</a><a class="btn btn-ghost" href="contact.php">お問い合わせ</a></div>
</div>
<div class="hero-actions-sp"><a class="btn btn-primary" href="business.html">事業内容を見る {ICON_ARROW}</a><a class="btn btn-ghost" href="contact.php">お問い合わせ {ICON_ARROW}</a></div>
<span class="scroll-hint" aria-hidden="true">SCROLL</span>
</section>

<section class="section philosophy" id="philosophy"><div class="container-narrow">
{section_head('PHILOSOPHY', '私たちの使命', True)}
<p class="statement reveal">患者様一人ひとりの<strong>健康と希望</strong>に向き合い、<br>未来に希望をつなぐこと。<br>それが、私たちの使命です。</p>
<p class="body reveal">私たちは、再生医療の可能性を追求しています。最先端の医療技術に、人としての温かさを重ね、個々の状態や想いを尊重した医療の提供を目指します。生活の質の向上に貢献し、未来に希望をつなぐ。その一点に、私たちは誠実に取り組みます。</p>
</div>
</section>

<section class="section tint" id="business"><div class="container">
{section_head('BUSINESS', '事業内容', True, '細胞の力を活かした3つの再生医療に取り組んでいます。')}
<div class="service-list">{cards}</div>
<p style="text-align:center;margin-top:40px"><a class="btn btn-line" href="business.html">事業内容の詳細 {ICON_ARROW}</a></p>
</div></section>

<section class="section warm" id="news"><div class="container">
{section_head('NEWS', 'お知らせ', True)}
{news_list(NEWS)}
<p style="margin-top:28px;text-align:center"><a class="btn btn-line" href="news-archive.html">過去の記事を見る {ICON_ARROW}</a></p>
</div></section>

{cta()}
</main>
'''
    s += footer()
    write('index.html', s)


# ---------------------------------------------------------------- SERVICES
def build_services():
    s = head('BUSINESS', '一般社団法人 CELLACT の事業内容。幹細胞療法、免疫細胞療法、幹細胞培養上清療法などの再生医療に取り組んでいます。', 'business.html')
    s += header('business.html')
    s += page_hero('BUSINESS', '事業内容', 'hero65_business.webp', [('index.html', 'TOP'), ('business.html', 'BUSINESS')], pos='50% 50%', mpos='60% 50%')
    s += '<main id="main"><section class="section"><div class="container">'
    s += section_head('FIELDS', '取り組んでいる再生医療', False, '細胞の力を活かした、3つの領域で医療を提供しています。')
    for sv in SERVICES:
        paras = ''.join(f'<p>{p}</p>' for p in sv['paras'])
        pts = ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in sv['points'])
        s += f'''<article class="service-detail reveal" id="{sv["id"]}"><div class="sd-media"><img src="images/{sv["img"]}" alt="" loading="lazy" width="1500" height="857"{" data-pan"}></div>
<div class="sd-text"><p class="eyebrow" style="color:var(--peach-deep)">{sv["en"]}</p><h2>{sv["name"]}</h2><p class="sd-lead">{sv["lead"]}</p>{paras}<dl class="sd-points">{pts}</dl></div></article>'''
    s += '<p class="sd-note reveal">※ 治療の内容・期間・リスク・費用などについては、診察時に医師が個別にご説明します。治療の経過や感じ方には、個人差があります。</p>'
    s += '''</div></section>
<section class="section tint"><div class="container safety-grid"><figure class="safety-photo reveal"><img src="images/photo_ope.webp" alt="クリニックの処置室" loading="lazy" width="1536" height="1024"></figure><div>''' + section_head('SAFETY', '安全への姿勢') + '''
<div class="reveal"><p>日本では、2014年に再生医療等安全性確保法が施行され、再生医療には厳格な規制のもとでの実施が求められています。私たちはこの法律を遵守し、安全かつ高度な再生医療の実践に努めています。</p>
<p>治療に用いる細胞の品質と、それを支える技術の信頼性は極めて重要です。徹底した品質管理のもとで培養された細胞を用い、患者様一人ひとりに安心して治療を受けていただける環境を整えています。</p></div>
</div></div></section>
<section class="section"><div class="container-narrow"><div class="patient-box reveal">
<p class="eyebrow">FOR PATIENTS</p><h2 class="section-title" style="font-size:1.4rem">治療を検討されている方へ</h2>
<p>治療の内容やご予約については、クリニックの公式サイトをご覧ください。</p>
<a class="btn btn-teal" href="https://cellact.jp/" target="_blank" rel="noopener noreferrer">クリニック公式サイトへ ''' + ICON_ARROW + '''</a></div></div></section>''' + cta('事業に関するお問い合わせ') + '</main>' + footer()
    write('business.html', s)


# ---------------------------------------------------------------- COMPANY
def build_company():
    rows = [('法人名', ORG), ('住所', '〒104-0061 東京都中央区銀座6-6-5<br>HULIC &amp; New GINZA NAMIKI6 11F'),
            ('TEL', f'<a href="tel:0332890202">{TEL}</a>'), ('FAX', '03-3289-0022'), ('事業内容', '再生医療クリニックの運営'),
            ('クリニックHP', '<a href="https://cellact.jp/" target="_blank" rel="noopener noreferrer">https://cellact.jp/</a>'),
            ('代表理事', '藤原彰子')]
    info = ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in rows)
    about = [
        ('CELLACTは、再生医療の可能性を追求し、安全で質の高い医療をお届けします。',
         'CELLACTは、幹細胞療法や免疫細胞療法などの再生医療に取り組んでいます。日本では、2014年に再生医療等安全性確保法が施行され、厳格な規制のもとでの治療が求められています。私たちはこの法律を遵守し、安全かつ高度な再生医療の実践に努めています。完全予約制のプライベートな環境で、国内外の患者様一人ひとりに向き合っています。'),
        ('細胞の品質と安全管理を大切に、一人ひとりに最適な再生医療を。',
         '再生医療において、治療に用いる細胞の品質と、それを支える技術の信頼性は極めて重要です。徹底した品質管理のもとで培養された細胞を用いることで、患者様一人ひとりに安心して治療を受けていただける環境を提供しています。再生医療に精通した医師が協力しながら診療を行い、患者様それぞれに最適な治療プランを設計します。')]
    cards = ''.join(f'<article class="about-card reveal"><h3>{t}</h3><p>{p}</p></article>' for t, p in about)
    mapq = 'https://www.google.com/maps?q=%E9%8A%80%E5%BA%A76-6-5%20HULIC%20%26%20New%20GINZA%20NAMIKI6%2011F&output=embed'
    s = head('COMPANY', '一般社団法人 CELLACT の法人概要。再生医療の取り組みと、所在地・連絡先のご案内。', 'company.html')
    s += header('company.html') + page_hero('COMPANY', '法人概要', 'hero65_company.webp', [('index.html', 'TOP'), ('company.html', 'COMPANY')], pos='50% 50%', mpos='82% 50%')
    s += f'''<main id="main"><section class="section"><div class="container split"><div class="split-head">{section_head('ABOUT US', '私たちについて')}</div><div class="about-grid">{cards}</div></div></section>
<section class="section"><div class="container logo-meaning"><div class="lm-mark reveal" data-capsule>{CAPSULE_SVG}<button type="button" class="lm-replay">もう一度見る</button></div>
<div class="lm-body">{section_head('LOGO', 'ロゴに込めた想い')}
<p class="lm-lead reveal">六角形の中に、ひとりの人が立っています。</p>
<p class="reveal">細胞を表す六角形の中に、「C」「＋」「Λ」の3つの形を縦に重ねて、人の姿を描いています。細胞の力（CELL）に、医療（＋）が加わり、行動（ACT）として人を支える。私たちが大切にしている、再生医療のあり方を、ひとつの形にしました。</p>
<dl class="lm-legend reveal">
<div><dt>六角形</dt><dd>細胞。生命の基本単位であり、再生医療の出発点です。</dd></div>
<div><dt>C</dt><dd>CELL。人の頭にあたり、細胞の力を表します。</dd></div>
<div><dt>＋</dt><dd>医療。人の胴体にあたり、医療の営みを表します。</dd></div>
<div><dt>Λ</dt><dd>ACT。人の脚にあたり、一歩を踏み出す「行動」を表します。</dd></div>
<div><dt>全体</dt><dd>細胞の力と医療が、人の健康と希望を支えるかたち。</dd></div>
</dl></div></div></section>
<section class="section tint"><div class="container">{section_head('INFORMATION', '法人情報')}
<div class="info-wrap reveal"><img src="images/photo_sofa.webp" alt="大きな窓のあるクリニックの待合スペース" loading="lazy" width="1536" height="1024"><dl class="info-table">{info}</dl></div>
<div class="map reveal"><iframe title="所在地の地図" src="{mapq}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
</div></section>{cta()}</main>''' + footer()
    write('company.html', s)


# ---------------------------------------------------------------- RECRUIT
def build_recruit():
    pos = [('看護師（正社員）', [('応募資格', '正看護師・准看護師 臨床経験3年以上'), ('歓迎するスキルや経験', '再生医療や美容外科の未経験者も歓迎'), ('試用期間（研修含）', '6ヵ月'), ('給与', 'スキルやご経験に応じて相談')]),
           ('受付（正社員）', [('応募資格', '経験3年以上'), ('歓迎するスキルや経験', '英語必須 再生医療や美容外科の未経験者も歓迎'), ('試用期間（研修含）', '6ヵ月'), ('給与', 'スキルやご経験に応じて相談')])]
    cards = ''
    for t, rows in pos:
        cards += f'<article class="position reveal"><h3>{t}</h3><dl>' + ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in rows) + '</dl></article>'
    s = head('RECRUIT', '再生医療の現場で、医療の未来を共に築きませんか。看護師・受付スタッフの募集要項。', 'recruit.html', og_img='images/hero_recruit.webp')
    s += header('recruit.html') + page_hero('RECRUIT', '採用情報', 'hero65_recruit.webp', [('index.html', 'TOP'), ('recruit.html', 'RECRUIT')], pos='50% 50%', mpos='40% 50%')
    s += f'''<main id="main"><section class="section"><div class="container split"><div class="split-head">{section_head('MESSAGE', '私たちの仕事は未来を再生すること。')}</div>
<div class="reveal message"><p>再生医療の現場で、医療の未来を共に築きませんか？<br>私たちは、幹細胞療法や免疫細胞療法による再生医療のほか、幹細胞培養上清療法などを提供しています。</p>
<p>未来の医療である「再生医療」の現場に、あなたのスキルと情熱を活かしませんか？<br>私たちは患者様の生活を再生し、希望を届けるために共に働ける仲間を探しています。</p>
<p>技術や経験はもちろん、何より「医療の可能性を信じ、成長したい」という意欲を重視します。</p></div></div>
<div class="container"><div class="photo-row reveal"><img src="images/photo_glass2.webp" alt="ガラス張りの待合スペース" loading="lazy" width="1536" height="1024"><img src="images/photo_logo.webp" alt="CELLACT CLINIC GINZAのエントランス" loading="lazy" width="1536" height="1024"><img src="images/photo_window.webp" alt="大きな窓のあるラウンジ" loading="lazy" width="1672" height="941"></div></div></section>
<section class="section tint"><div class="container">{section_head('POSITIONS', '募集要項')}<div class="positions">{cards}</div>
<p style="text-align:center;margin-top:36px"><a class="btn btn-teal" href="contact.php?purpose=recruit">採用に関するお問い合わせ {ICON_ARROW}</a></p></div></section></main>''' + footer()
    write('recruit.html', s)


# ---------------------------------------------------------------- NEWS
def build_news():
    s = head('NEWS', 'CELLACT からのお知らせ一覧。', 'news-archive.html', og_img='images/hero_top.webp')
    s += header('news-archive.html') + page_hero('NEWS', 'お知らせ', 'hero65_news.webp', [('index.html', 'TOP'), ('news-archive.html', 'NEWS')], pos='50% 50%', mpos='60% 50%')
    s += f'<main id="main"><section class="section"><div class="container-narrow">{section_head("NEWS ARCHIVE", "お知らせ一覧")}{news_list(NEWS)}</div></section></main>' + footer()
    write('news-archive.html', s)
    for n in NEWS:
        w = ' warm' if n['warm'] else ''
        d = n['title']
        s = head(n['title'], n['excerpt'].replace('&amp;', '&'), n['slug'] + '.html', og_img='images/' + n['img'])
        s += header('news-archive.html') + page_hero('NEWS', 'お知らせ', 'hero65_news.webp', [('index.html', 'TOP'), ('news-archive.html', 'NEWS'), (n['slug'] + '.html', n['title'])], pos='50% 50%', mpos='60% 50%')
        s += f'''<main id="main"><section class="section"><div class="container-narrow"><article class="article reveal">
<header class="article-head"><div class="article-meta"><time datetime="{n["date"].replace(".", "-")}">{n["date"]}</time><span class="tag{w}">{n["tag"]}</span></div><h1>{n["title"]}</h1></header>
{(f'<figure class="article-fig logo-over"><img class="article-img" src="images/{n["img"]}" alt="" width="1500" height="844"><img class="fig-logo" src="images/cellact_logo.png?v=2" alt="CELLACT" width="788" height="840"></figure>' if n.get('logo') else f'<img class="article-img" src="images/{n["img"]}" alt="" width="1500" height="844">')}
<div class="article-body">{n["body"]}</div>
<div class="article-nav"><a class="btn btn-teal" href="news-archive.html">一覧へ戻る</a><a class="btn btn-line" href="index.html#news">TOPのNEWSへ</a></div>
</article></div></section></main>''' + footer()
        write(n['slug'] + '.html', s)


# ---------------------------------------------------------------- CONTACT (PHP)
PURPOSES = "['treatment' => '治療に関するお問い合わせ', 'recruit' => '採用に関するお問い合わせ', 'other' => 'その他']"

PHP_COMMON = '''<?php
// 共通設定
declare(strict_types=1);
ini_set('display_errors', '0');
error_reporting(E_ALL);
session_set_cookie_params(['httponly' => true, 'samesite' => 'Lax', 'secure' => !empty($_SERVER['HTTPS'])]);
session_start();
header('X-Content-Type-Options: nosniff');
header('X-Frame-Options: SAMEORIGIN');
header('Referrer-Policy: strict-origin-when-cross-origin');
function h(string $v): string { return htmlspecialchars($v, ENT_QUOTES, 'UTF-8'); }
$PURPOSES = ''' + PURPOSES + ''';
'''


def build_contact():
    # --- contact.php (form)
    s = PHP_COMMON + '''
if (empty($_SESSION['csrf'])) { $_SESSION['csrf'] = bin2hex(random_bytes(32)); }
$_SESSION['form_started'] = time();
$old = $_SESSION['form_data'] ?? [];
$errors = $_SESSION['errors'] ?? [];
unset($_SESSION['errors']);
$v = function (string $k) use ($old): string { return h((string)($old[$k] ?? '')); };
$purpose = (string)($old['purpose'] ?? ($_GET['purpose'] ?? ''));
?>
'''
    s += head('CONTACT', '一般社団法人 CELLACT へのお問い合わせフォーム。治療・採用などのご質問を24時間受け付けています。', 'contact.php', og_img='images/hero_contact.webp')
    s += header('contact.php') + page_hero('CONTACT', 'お問い合わせ', 'hero65_contact.webp', [('index.html', 'TOP'), ('contact.php', 'CONTACT')], pos='50% 50%', mpos='62% 50%')
    s += '''<main id="main"><section class="section tint"><div class="container-narrow">
<ol class="steps" aria-label="手順"><li class="on">1 入力</li><li>2 確認</li><li>3 完了</li></ol>
<p class="lead" style="margin:0 auto 28px;text-align:center">フォームは24時間受け付けています。必須項目をご入力のうえ「確認画面へ」を押してください。</p>
<?php if ($errors): ?><div class="notice error" role="alert"><b>入力内容をご確認ください</b><ul><?php foreach ($errors as $e): ?><li><?= h($e) ?></li><?php endforeach; ?></ul></div><?php endif; ?>
<form class="form-card reveal" data-contact action="contact_confirm.php" method="post" novalidate_off>
<input type="hidden" name="csrf" value="<?= h($_SESSION['csrf']) ?>">
<div class="hp" aria-hidden="true"><label>この欄は空のままにしてください<input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
<div class="field"><label for="purpose">ご用件<span class="req">必須</span></label>
<select id="purpose" name="purpose" required><option value="">選択してください</option>
<?php foreach ($PURPOSES as $k => $label): ?><option value="<?= h($k) ?>"<?= $purpose === $k ? ' selected' : '' ?>><?= h($label) ?></option><?php endforeach; ?></select></div>
<div class="field"><span class="label" id="nm">お名前<span class="req">必須</span></span>
<div class="two" role="group" aria-labelledby="nm"><input type="text" name="lastName" placeholder="姓" autocomplete="family-name" required value="<?= $v('lastName') ?>" aria-label="姓"><input type="text" name="firstName" placeholder="名" autocomplete="given-name" required value="<?= $v('firstName') ?>" aria-label="名"></div></div>
<div class="field"><label for="phone">電話番号<span class="req">必須</span></label><input type="tel" id="phone" name="phone" placeholder="03-1234-5678" autocomplete="tel" inputmode="tel" required value="<?= $v('phone') ?>"><p class="hint">半角で入力してください。</p></div>
<div class="field"><label for="email">メールアドレス<span class="req">必須</span></label><input type="email" id="email" name="email" placeholder="example@email.com" autocomplete="email" required value="<?= $v('email') ?>"></div>
<div class="field"><label for="email_confirm">メールアドレス（確認用）<span class="req">必須</span></label><input type="email" id="email_confirm" name="email_confirm" placeholder="確認のため再入力してください" autocomplete="off" required value="<?= $v('email') ?>"></div>
<div class="field"><label for="message">お問い合わせ内容<span class="req">必須</span></label><textarea id="message" name="message" maxlength="3000" required placeholder="お問い合わせ内容をご入力ください"><?= $v('message') ?></textarea><p class="hint">3,000文字まで。</p></div>
<div class="field"><label class="agree"><input type="checkbox" name="agree" value="1" required><span><a href="privacy.html" target="_blank" rel="noopener">プライバシーポリシー</a>に同意します。</span></label></div>
<div class="notice">お急ぎの場合はお電話（<a href="tel:0332890202">03-3289-0202</a>）でもご相談いただけます。お送りいただいた個人情報は、お問い合わせへの対応以外には使用しません。</div>
<div class="form-actions"><button type="submit" class="btn btn-primary">確認画面へ ''' + ICON_ARROW + '''</button></div>
</form></div></section></main>''' + footer()
    s = s.replace(' novalidate_off', '')
    write('contact.php', s)

    # --- contact_confirm.php
    c = PHP_COMMON + '''
if ($_SERVER['REQUEST_METHOD'] !== 'POST') { header('Location: contact.php'); exit; }

$in = function (string $k): string { return trim((string)($_POST[$k] ?? '')); };
$data = [
    'purpose' => $in('purpose'), 'lastName' => $in('lastName'), 'firstName' => $in('firstName'),
    'phone' => $in('phone'), 'email' => $in('email'), 'message' => str_replace(["\\r\\n", "\\r"], "\\n", $in('message')),
];
$emailConfirm = $in('email_confirm');
$errors = [];

// CSRF・ボット対策（ハニーポット、極端に短時間の送信）
if (!hash_equals((string)($_SESSION['csrf'] ?? ''), (string)($_POST['csrf'] ?? ''))) { $errors[] = 'セッションの有効期限が切れました。もう一度ご入力ください。'; }
if ($in('website') !== '') { http_response_code(400); exit; }
if (time() - (int)($_SESSION['form_started'] ?? 0) < 3) { $errors[] = '送信が早すぎます。内容をご確認のうえ、もう一度お試しください。'; }

if (!isset($PURPOSES[$data['purpose']])) { $errors[] = 'ご用件を選択してください。'; }
if ($data['lastName'] === '' || $data['firstName'] === '') { $errors[] = 'お名前を入力してください。'; }
if (mb_strlen($data['lastName']) > 50 || mb_strlen($data['firstName']) > 50) { $errors[] = 'お名前が長すぎます。'; }
if (!preg_match('/^[0-9０-９+\\-ー() ]{8,20}$/u', $data['phone'])) { $errors[] = '電話番号を正しく入力してください。'; }
if (!filter_var($data['email'], FILTER_VALIDATE_EMAIL)) { $errors[] = '有効なメールアドレスを入力してください。'; }
elseif ($data['email'] !== $emailConfirm) { $errors[] = 'メールアドレスと確認用メールアドレスが一致しません。'; }
if ($data['message'] === '') { $errors[] = 'お問い合わせ内容を入力してください。'; }
if (mb_strlen($data['message']) > 3000) { $errors[] = 'お問い合わせ内容は3,000文字以内で入力してください。'; }
if ($in('agree') !== '1') { $errors[] = 'プライバシーポリシーへの同意が必要です。'; }

if ($errors) {
    $_SESSION['errors'] = $errors;
    unset($data['email_confirm']);
    $_SESSION['form_data'] = $data;
    header('Location: contact.php');
    exit;
}

$_SESSION['form_data'] = $data;
$_SESSION['confirmed'] = true;
?>
'''
    c += head('送信内容の確認', '入力内容をご確認ください。', 'contact_confirm.php', noindex=True)
    c += header('contact.php') + page_hero('CONTACT', 'お問い合わせ', 'hero65_contact.webp', [('index.html', 'TOP'), ('contact.php', 'CONTACT'), ('contact_confirm.php', '確認')], pos='50% 50%', mpos='62% 50%')
    c += '''<main id="main"><section class="section tint"><div class="container-narrow">
<ol class="steps" aria-label="手順"><li>1 入力</li><li class="on">2 確認</li><li>3 完了</li></ol>
<div class="form-card">
<p style="margin-top:0">以下の内容で送信します。よろしければ「送信する」を押してください。</p>
<table class="confirm-table">
<tr><th>ご用件</th><td><?= h($PURPOSES[$data['purpose']]) ?></td></tr>
<tr><th>お名前</th><td><?= h($data['lastName'] . ' ' . $data['firstName']) ?></td></tr>
<tr><th>電話番号</th><td><?= h($data['phone']) ?></td></tr>
<tr><th>メールアドレス</th><td><?= h($data['email']) ?></td></tr>
<tr><th>お問い合わせ内容</th><td><?= h($data['message']) ?></td></tr>
</table>
<form action="contact_process.php" method="post"><input type="hidden" name="csrf" value="<?= h($_SESSION['csrf']) ?>">
<div class="form-actions"><a class="btn btn-line" href="contact.php">修正する</a><button type="submit" class="btn btn-primary">送信する ''' + ICON_ARROW + '''</button></div></form>
</div></div></section></main>''' + footer()
    write('contact_confirm.php', c)

    # --- contact_process.php
    p = PHP_COMMON + '''
$TO = 'info@cellact.org';
$FROM = 'noreply@cellact.org';
$TEL = '03-3289-0202';

if ($_SERVER['REQUEST_METHOD'] !== 'POST' || empty($_SESSION['confirmed']) || empty($_SESSION['form_data'])
    || !hash_equals((string)($_SESSION['csrf'] ?? ''), (string)($_POST['csrf'] ?? ''))) {
    header('Location: contact.php');
    exit;
}
$d = $_SESSION['form_data'];
// ヘッダーインジェクション対策（改行除去）。メールアドレスは確認ページで FILTER_VALIDATE_EMAIL 済み
$clean = function (string $s): string { return str_replace(["\\r", "\\n"], ' ', $s); };
$name = $clean($d['lastName'] . ' ' . $d['firstName']);
$email = $clean($d['email']);
$purposeLabel = $PURPOSES[$d['purpose']] ?? 'その他';
$when = date('Y年m月d日 H:i:s');
$line = str_repeat('-', 34);

$body = "CELLACT へお問い合わせがありました。\\n\\n$line\\n"
      . "■ ご用件\\n$purposeLabel\\n\\n■ お名前\\n$name 様\\n\\n■ 電話番号\\n{$d['phone']}\\n\\n"
      . "■ メールアドレス\\n$email\\n\\n■ お問い合わせ内容\\n{$d['message']}\\n$line\\n\\n送信日時: $when\\n";
$headers = "From: $FROM\\r\\nReply-To: $email\\r\\nContent-Type: text/plain; charset=UTF-8\\r\\n";

$reply = "$name 様\\n\\nこの度はお問い合わせいただき、誠にありがとうございます。\\n以下の内容で受け付けいたしました。担当者より折り返しご連絡いたしますので、今しばらくお待ちください。\\n\\n$line\\n"
       . "ご用件: $purposeLabel\\nお名前: $name\\n電話番号: {$d['phone']}\\nメールアドレス: $email\\n\\nお問い合わせ内容:\\n{$d['message']}\\n$line\\n\\n"
       . "※このメールは自動送信です。ご返信いただいてもお答えできません。\\n\\n一般社団法人 CELLACT\\n〒104-0061 東京都中央区銀座6-6-5 HULIC & New GINZA NAMIKI6 11F\\nTEL: $TEL\\nEmail: $TO\\n";
$replyHeaders = "From: 一般社団法人 CELLACT <$FROM>\\r\\nContent-Type: text/plain; charset=UTF-8\\r\\n";

$sent = false;
if (function_exists('mb_send_mail')) {
    mb_language('Japanese');
    mb_internal_encoding('UTF-8');
    $sent = mb_send_mail($TO, "【CELLACT】お問い合わせ: $purposeLabel", $body, $headers);
    if ($sent) { mb_send_mail($email, '【CELLACT】お問い合わせを受け付けました', $reply, $replyHeaders); }
} else {
    $sent = mail($TO, '=?UTF-8?B?' . base64_encode("【CELLACT】お問い合わせ: $purposeLabel") . '?=', $body, $headers);
}

if (!$sent) {
    error_log('contact form: mail send failed');
    http_response_code(500);
    ?>
'''
    p += head('送信に失敗しました', '送信に失敗しました。', 'contact_process.php', noindex=True)
    p += header('contact.php')
    p += f'''<main id="main"><section class="section tint"><div class="container-narrow"><div class="form-card" style="text-align:center">
<h1 class="section-title" style="font-size:1.4rem">送信に失敗しました</h1>
<p>申し訳ありません。時間をおいて再度お試しいただくか、お電話（<a href="tel:0332890202">{TEL}</a>）でご連絡ください。</p>
<div class="form-actions"><a class="btn btn-teal" href="contact.php">フォームに戻る</a></div></div></div></section></main>''' + footer()
    p += '''<?php
    exit;
}

// 完了：セッション情報を破棄してサンクスページへ（再送信防止）
unset($_SESSION['form_data'], $_SESSION['confirmed'], $_SESSION['errors']);
$_SESSION['csrf'] = bin2hex(random_bytes(32));
header('Location: contact_thanks.html');
exit;
'''
    write('contact_process.php', p)

    # --- thanks
    t = head('お問い合わせありがとうございます', '送信が完了しました。', 'contact_thanks.html', noindex=True)
    t += header('contact.php') + page_hero('CONTACT', 'お問い合わせ', 'hero65_contact.webp', [('index.html', 'TOP'), ('contact.php', 'CONTACT'), ('contact_thanks.html', '完了')], pos='50% 50%', mpos='62% 50%')
    t += '''<main id="main"><section class="section tint"><div class="container-narrow">
<ol class="steps" aria-label="手順"><li>1 入力</li><li>2 確認</li><li class="on">3 完了</li></ol>
<div class="form-card" style="text-align:center"><h2 class="section-title" style="font-size:1.5rem">お問い合わせありがとうございます</h2>
<p>送信が完了しました。担当者よりご連絡いたしますので、しばらくお待ちください。</p>
<p class="hint" style="color:var(--ink-soft);font-size:.9rem">数分経っても自動返信メールが届かない場合は、メールアドレスや迷惑メール設定をご確認ください。</p>
<div class="form-actions"><a class="btn btn-teal" href="index.html">TOPへ戻る</a></div></div></div></section></main>''' + footer()
    write('contact_thanks.html', t)


# ---------------------------------------------------------------- PRIVACY (DRAFT) / 404 / sitemap
def build_misc():
    s = head('プライバシーポリシー', '一般社団法人 CELLACT のプライバシーポリシー。', 'privacy.html')
    s += header('') + page_hero('PRIVACY', 'プライバシーポリシー', 'hero65_privacy.webp', [('index.html', 'TOP'), ('privacy.html', 'プライバシーポリシー')], pos='50% 50%', mpos='40% 50%')
    s += f'''<main id="main"><section class="section"><div class="container-narrow prose">
<!-- 公開前に法務確認のうえ、内容を最終化してください -->
<p>{ORG}（以下「当法人」）は、お問い合わせ・採用に関するご連絡などを通じてお預かりする個人情報の重要性を認識し、個人情報の保護に関する法律（個人情報保護法）その他の関係法令を遵守して、以下の方針に基づき適切に取り扱います。</p>
<h2>1. 個人情報の定義</h2><p>個人情報とは、個人情報保護法に定める、生存する個人に関する情報で、氏名、電話番号、メールアドレスなどにより特定の個人を識別できるものをいいます。</p>
<h2>2. 取得する情報</h2><p>当法人は、本サイトのお問い合わせフォームを通じて、次の情報を取得します。</p>
<ul><li>お名前</li><li>電話番号</li><li>メールアドレス</li><li>お問い合わせの内容</li></ul>
<p>あわせて、フォームの不正利用を防ぐために必要な範囲で、送信時刻やアクセスに関する技術情報を一時的に取り扱うことがあります。なお、お問い合わせの際、病状や既往歴などの要配慮個人情報のご記入は、お控えください。診療に関するご相談は、クリニックの窓口（<a href="https://cellact.jp/" target="_blank" rel="noopener">cellact.jp</a>）へお願いいたします。</p>
<h2>3. 利用目的</h2><p>取得した個人情報は、次の目的の範囲内で利用します。</p>
<ul><li>お問い合わせへの回答、およびご連絡のため</li><li>採用に関するご案内、および連絡のため</li><li>当法人の事業に関する連絡や、ご案内のため</li><li>サービス向上のための、問い合わせ内容の分析のため（個人を特定できない形で行います）</li></ul>
<h2>4. 利用目的の変更</h2><p>利用目的は、変更前の目的と関連性を有すると合理的に認められる範囲でのみ変更します。変更する場合は、本ページへの掲載などにより、お知らせします。</p>
<h2>5. 第三者への提供</h2><p>当法人は、次の場合を除き、ご本人の同意なく個人情報を第三者へ提供しません。</p>
<ul><li>法令に基づく場合</li><li>人の生命、身体、または財産の保護のために必要で、ご本人の同意を得ることが困難な場合</li><li>公衆衛生の向上、または児童の健全な育成のために特に必要で、ご本人の同意を得ることが困難な場合</li><li>国の機関、もしくは地方公共団体などが法令の定める事務を遂行することに協力する必要がある場合</li></ul>
<h2>6. 業務委託</h2><p>利用目的の達成に必要な範囲で、個人情報の取り扱いを外部に委託することがあります。その場合は、委託先との間で秘密保持などを定め、適切に監督します。</p>
<h2>7. 安全管理措置</h2><p>個人情報への不正アクセス、紛失、破壊、改ざん、漏えいなどを防止するため、組織的、人的、物理的、技術的な安全管理措置を講じます。お問い合わせフォームの通信は、暗号化（SSL/TLS）して行います。</p>
<h2>8. 保管期間</h2><p>お預かりした個人情報は、利用目的の達成に必要な期間に限って保管し、不要となったときは、速やかに、かつ安全な方法で削除、または廃棄します。</p>
<h2>9. Cookie（クッキー）について</h2><p>本サイトのお問い合わせフォームでは、不正な送信を防ぐために、セッション用の Cookie を使用します。この Cookie から、個人を特定する情報を取得することはありません。ブラウザの設定で Cookie を無効にすると、フォームが正しく動作しない場合があります。</p>
<h2>10. 外部サービスの利用</h2><p>本サイトでは、地図表示に Google マップ、フォント配信に Google Fonts を利用しています。これらの利用により、閲覧情報などが各提供事業者に送信される場合があります。その取り扱いは、各事業者のプライバシーポリシーに従います。また、本サイトからリンクする外部サイトでの個人情報の取り扱いについて、当法人は責任を負いません。</p>
<h2>11. 開示・訂正・利用停止などのご請求</h2><p>ご本人から、保有個人データの開示、訂正、追加、削除、利用停止などのご請求があった場合は、ご本人であることを確認したうえで、法令に従い、遅滞なく対応します。下記の窓口までご連絡ください。</p>
<h2>12. プライバシーポリシーの変更</h2><p>当法人は、法令の改正や、取り扱いの見直しにあわせて、本ポリシーを変更することがあります。変更後の内容は、本ページに掲載した時点から効力を生じます。</p>
<h2>13. お問い合わせ窓口</h2>
<p>{ORG}<br>〒104-0061 東京都中央区銀座6-6-5 HULIC &amp; New GINZA NAMIKI6 11F<br>TEL {TEL} / FAX 03-3289-0022<br>メール info@cellact.org（<a href="contact.php">お問い合わせフォーム</a>）</p>
<p class="sub-note">制定日：2027年1月1日</p>
</div></section></main>''' + footer()
    write('privacy.html', s)

    s = head('ページが見つかりません', 'お探しのページは見つかりませんでした。', '404.html', noindex=True)
    s += header('') + f'''<main id="main"><section class="section"><div class="container-narrow" style="text-align:center">
<p class="eyebrow">404 NOT FOUND</p><h1 class="section-title" style="font-size:1.6rem">ページが見つかりません</h1>
<p>URLが変更されたか、削除された可能性があります。</p><a class="btn btn-teal" href="index.html">TOPへ戻る</a></div></section></main>''' + footer()
    write('404.html', s)

    urls = ['', 'business.html', 'company.html', 'recruit.html', 'news-archive.html', 'contact.php', 'privacy.html'] + [n['slug'] + '.html' for n in NEWS]
    write('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + ''.join(f'<url><loc>{BASE}{u}</loc></url>\n' for u in urls) + '</urlset>\n')
    write('robots.txt', f'User-agent: *\nAllow: /\nDisallow: /contact_confirm.php\nDisallow: /contact_process.php\nSitemap: {BASE}sitemap.xml\n')
    write('.htaccess', '''# Apache (レンタルサーバー向け)
ErrorDocument 404 /404.html
Options -Indexes
<IfModule mod_headers.c>
  Header always set X-Content-Type-Options "nosniff"
  Header always set X-Frame-Options "SAMEORIGIN"
  Header always set Referrer-Policy "strict-origin-when-cross-origin"
</IfModule>
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType image/webp "access plus 1 month"
  ExpiresByType image/png "access plus 1 month"
  ExpiresByType text/css "access plus 1 week"
  ExpiresByType application/javascript "access plus 1 week"
</IfModule>
''')
    write('.gitignore', '.DS_Store\n**/.DS_Store\n')


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    build_index(); build_services(); build_company(); build_recruit(); build_news(); build_contact(); build_misc()
    print('built:', sorted(os.listdir(OUT)))
