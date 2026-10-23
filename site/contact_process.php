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
$clean = function (string $s): string { return str_replace(["\r", "\n"], ' ', $s); };
$name = $clean($d['lastName'] . ' ' . $d['firstName']);
$email = $clean($d['email']);
$purposeLabel = $PURPOSES[$d['purpose']] ?? 'その他';
$when = date('Y年m月d日 H:i:s');
$line = str_repeat('-', 34);

$body = "CELLACT へお問い合わせがありました。\n\n$line\n"
      . "■ ご用件\n$purposeLabel\n\n■ お名前\n$name 様\n\n■ 電話番号\n{$d['phone']}\n\n"
      . "■ メールアドレス\n$email\n\n■ お問い合わせ内容\n{$d['message']}\n$line\n\n送信日時: $when\n";
$headers = "From: $FROM\r\nReply-To: $email\r\nContent-Type: text/plain; charset=UTF-8\r\n";

$reply = "$name 様\n\nこの度はお問い合わせいただき、誠にありがとうございます。\n以下の内容で受け付けいたしました。担当者より折り返しご連絡いたしますので、今しばらくお待ちください。\n\n$line\n"
       . "ご用件: $purposeLabel\nお名前: $name\n電話番号: {$d['phone']}\nメールアドレス: $email\n\nお問い合わせ内容:\n{$d['message']}\n$line\n\n"
       . "※このメールは自動送信です。ご返信いただいてもお答えできません。\n\n一般社団法人 CELLACT\n〒104-0061 東京都中央区銀座6-6-5 HULIC & New GINZA NAMIKI6 11F\nTEL: $TEL\nEmail: $TO\n";
$replyHeaders = "From: 一般社団法人 CELLACT <$FROM>\r\nContent-Type: text/plain; charset=UTF-8\r\n";

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
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>送信に失敗しました | 一般社団法人 CELLACT</title>
<meta name="description" content="送信に失敗しました。">
<meta name="robots" content="noindex,nofollow">

<meta property="og:type" content="website">
<meta property="og:site_name" content="一般社団法人 CELLACT">
<meta property="og:title" content="送信に失敗しました | 一般社団法人 CELLACT">
<meta property="og:description" content="送信に失敗しました。">
<meta property="og:image" content="https://cellact.org/images/hero_top.webp">
<meta property="og:locale" content="ja_JP">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0f6b86">
<link rel="icon" href="images/cellact_logo.png?v=151" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500&amp;family=Noto+Serif+JP:wght@500;600&amp;display=swap">
<link rel="stylesheet" href="styles.css?v=1792752760">
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
<main id="main"><section class="section tint"><div class="container-narrow"><div class="form-card" style="text-align:center">
<h1 class="section-title" style="font-size:1.4rem">送信に失敗しました</h1>
<p>申し訳ありません。時間をおいて再度お試しいただくか、お電話（<a href="tel:0332890202">03-3289-0202</a>）でご連絡ください。</p>
<div class="form-actions"><a class="btn btn-teal" href="contact.php">フォームに戻る</a></div></div></div></section></main><footer class="site-footer">
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
<script src="script.js?v=1792752760" defer></script>
</body>
</html>
<?php
    exit;
}

// 完了：セッション情報を破棄してサンクスページへ（再送信防止）
unset($_SESSION['form_data'], $_SESSION['confirmed'], $_SESSION['errors']);
$_SESSION['csrf'] = bin2hex(random_bytes(32));
header('Location: contact_thanks.html');
exit;
