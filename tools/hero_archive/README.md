# TOPヒーローの保管版

| フォルダ | 内容 | git タグ |
|---|---|---|
| v1_pale-skyblue-no-figure | 淡い水色・人物なし。PC(横長 hero_top.webp) とスマホ(縦長 hero_top_sp.webp) | hero-v1-pale-skyblue |

戻し方:
    cp tools/hero_archive/v1_pale-skyblue-no-figure/hero_top.webp    site/images/hero_top.webp
    cp tools/hero_archive/v1_pale-skyblue-no-figure/hero_top_sp.webp site/images/hero_top_sp.webp
    # tools/build.py の hero_top / hero_top_sp の ?v= を上げてから
    python3 tools/build.py

または git で丸ごと戻す:
    git checkout hero-v1-pale-skyblue -- site tools/build.py
