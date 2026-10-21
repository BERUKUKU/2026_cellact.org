<?php
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
$PURPOSES = ['treatment' => '治療に関するお問い合わせ', 'recruit' => '採用に関するお問い合わせ', 'other' => 'その他'];

if (empty($_SESSION['csrf'])) { $_SESSION['csrf'] = bin2hex(random_bytes(32)); }
$_SESSION['form_started'] = time();
$old = $_SESSION['form_data'] ?? [];
$errors = $_SESSION['errors'] ?? [];
unset($_SESSION['errors']);
$v = function (string $k) use ($old): string { return h((string)($old[$k] ?? '')); };
$purpose = (string)($old['purpose'] ?? ($_GET['purpose'] ?? ''));
?>
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CONTACT | 一般社団法人 CELLACT</title>
<meta name="description" content="一般社団法人 CELLACT へのお問い合わせフォーム。治療・採用などのご質問を24時間受け付けています。">

<link rel="canonical" href="https://cellact.org/contact.php">
<meta property="og:type" content="website">
<meta property="og:site_name" content="一般社団法人 CELLACT">
<meta property="og:title" content="CONTACT | 一般社団法人 CELLACT">
<meta property="og:description" content="一般社団法人 CELLACT へのお問い合わせフォーム。治療・採用などのご質問を24時間受け付けています。">
<meta property="og:image" content="https://cellact.org/images/hero_contact.webp">
<meta property="og:locale" content="ja_JP">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0f6b86">
<link rel="icon" href="images/cellact_logo.png?v=151" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500&amp;family=Noto+Serif+JP:wght@500;600&amp;display=swap">
<link rel="stylesheet" href="styles.css?v=1792550531">
<script>document.documentElement.classList.add('js')</script>

</head>
<body>
<a class="skip" href="#main">本文へスキップ</a>
<header class="site-header">
<div class="container">
<a class="brand" href="index.html" aria-label="一般社団法人 CELLACT トップへ"><img src="images/cellact_logo.png?v=151" alt="" width="62" height="66"><span>一般社団法人 CELLACT<small>REGENERATIVE MEDICINE</small></span></a>
<button class="menu-btn" aria-expanded="false" aria-controls="gnav" aria-label="メニュー"><span></span></button>
<nav class="gnav" id="gnav" aria-label="メインメニュー"><ul><li><a href="index.html">TOP</a></li><li><a href="business.html">BUSINESS</a></li><li><a href="company.html">COMPANY</a></li><li><a href="recruit.html">RECRUIT</a></li><li><a href="news-archive.html">NEWS</a></li><li><a class="nav-cta" href="contact.php" aria-current="page">CONTACT</a></li></ul></nav>
</div>
</header>
<section class="page-hero">
<div class="hero-bg"><img src="images/hero65_contact.webp" alt="" width="1500" height="375" style="object-position:50% 50%;--mpos:62% 50%"></div>
<div class="container" data-en="CONTACT"><p class="eyebrow">CONTACT</p><h1>お問い合わせ</h1><nav class="breadcrumb" aria-label="パンくず"><a href="index.html">TOP</a> &gt; CONTACT</nav></div>
</section>
<main id="main"><section class="section tint"><div class="container-narrow">
<ol class="steps" aria-label="手順"><li class="on">1 入力</li><li>2 確認</li><li>3 完了</li></ol>
<p class="lead" style="margin:0 auto 28px;text-align:center">フォームは24時間受け付けています。必須項目をご入力のうえ「確認画面へ」を押してください。</p>
<?php if ($errors): ?><div class="notice error" role="alert"><b>入力内容をご確認ください</b><ul><?php foreach ($errors as $e): ?><li><?= h($e) ?></li><?php endforeach; ?></ul></div><?php endif; ?>
<form class="form-card reveal" data-contact action="contact_confirm.php" method="post">
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
<div class="form-actions"><button type="submit" class="btn btn-primary">確認画面へ <span class="arrow" aria-hidden="true">→</span></button></div>
</form></div></section></main><footer class="site-footer">
<div class="container">
<div class="footer-grid">
<div>
<a class="footer-brand" href="index.html"><img src="images/cellact_logo_white.png?v=151" alt="" width="72" height="76"><b>一般社団法人 CELLACT</b></a>
<address>〒104-0061 東京都中央区銀座6-6-5<br>HULIC &amp; New GINZA NAMIKI6 11F<br>TEL <a href="tel:0332890202">03-3289-0202</a> / FAX 03-3289-0022</address>
</div>
<div><h4>MENU</h4><ul><li><a href="index.html">TOP</a></li><li><a href="business.html">BUSINESS</a></li><li><a href="company.html">COMPANY</a></li><li><a href="recruit.html">RECRUIT</a></li><li><a href="news-archive.html">NEWS</a></li><li><a href="contact.php">CONTACT</a></li></ul></div>
<div><h4>INFORMATION</h4><ul><li><a href="https://cellact.jp/" target="_blank" rel="noopener noreferrer">クリニック公式サイト</a></li><li><a href="privacy.html">プライバシーポリシー</a></li></ul></div>
</div>
<div class="copy"><span>&copy; 2026 一般社団法人 CELLACT. All rights reserved.</span></div>
</div>
</footer>
<script src="script.js?v=1792550531" defer></script>
</body>
</html>
