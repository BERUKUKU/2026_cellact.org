# CELLACT 公式サイト (cellact.org)

静的 HTML/CSS/JS + PHP（お問い合わせフォーム）。
`site/` が公開物。`tools/build.py` が各ページの HTML を生成します（HTML は直接編集せず、build.py を編集して再生成）。

    python3 tools/build.py          # site/ を再生成
    python3 tools/preview_server.py # http://localhost:8765 でプレビュー（PHP は未実行）

お問い合わせフォームは PHP が動くサーバーで確認してください（contact.php → contact_confirm.php → contact_process.php）。
