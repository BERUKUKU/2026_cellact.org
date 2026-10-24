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

if ($_SERVER['REQUEST_METHOD'] !== 'POST') { header('Location: contact.php'); exit; }

$in = function (string $k): string { return trim((string)($_POST[$k] ?? '')); };
$data = [
    'purpose' => $in('purpose'), 'lastName' => $in('lastName'), 'firstName' => $in('firstName'),
    'phone' => $in('phone'), 'email' => $in('email'), 'message' => str_replace(["\r\n", "\r"], "\n", $in('message')),
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
if (!preg_match('/^[0-9０-９+\-ー() ]{8,20}$/u', $data['phone'])) { $errors[] = '電話番号を正しく入力してください。'; }
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
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>送信内容の確認 | 一般社団法人 CELLACT</title>
<meta name="description" content="入力内容をご確認ください。">
<meta name="robots" content="noindex,nofollow">

<meta property="og:type" content="website">
<meta property="og:site_name" content="一般社団法人 CELLACT">
<meta property="og:title" content="送信内容の確認 | 一般社団法人 CELLACT">
<meta property="og:description" content="入力内容をご確認ください。">
<meta property="og:image" content="https://cellact.org/images/hero_top.webp">
<meta property="og:locale" content="ja_JP">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0f6b86">
<link rel="icon" href="images/cellact_logo.png?v=151" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500&amp;family=Noto+Serif+JP:wght@500;600&amp;display=swap">
<link rel="stylesheet" href="styles.css?v=1792825062">
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
<div class="hero-bg"><img src="images/hero65_contact.webp?v=14" alt="" width="2041" height="314" style="object-position:50% 50%;--mpos:62% 50%"></div>
<div class="container" data-en="CONTACT"><p class="eyebrow">CONTACT</p><h1>お問い合わせ</h1><nav class="breadcrumb" aria-label="パンくず"><a href="index.html">TOP</a> &gt; <a href="contact.php">CONTACT</a> &gt; 確認</nav></div>
</section>
<main id="main"><section class="section tint"><div class="container-narrow">
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
<div class="form-actions"><a class="btn btn-line" href="contact.php">修正する</a><button type="submit" class="btn btn-primary">送信する <span class="arrow" aria-hidden="true">→</span></button></div></form>
</div></div></section></main><footer class="site-footer">
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
<script src="script.js?v=1792825062" defer></script>
</body>
</html>
