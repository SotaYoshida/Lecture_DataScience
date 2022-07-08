# 資料:実践データサイエンス

本コンテンツは宇都宮大学の基盤科目「実践データサイエンス」の授業資料です。

## 資料の使い方

本講義では資料(≒ファイル形式)や利用する外部サービス等が幾つかある。
慣れないうちは混同するかと思うので、ここに資料自体の説明と各種アプリケーションやサービスの説明をまとめておく。

### ブック
:::{margin}
概要を理解したり復習する際にはこちらのブックを閲覧してください
:::
本資料は[Jupyter Notebook](https://github.com/jupyter/notebook)形式で作成されたソースファイルを[Jupyter Book](https://jupyterbook.org/en/stable/intro.html)を用いて変換することで作成されたコンテンツになっている。この形式の資料を授業内では**ブック**ないし**Book**と表記・呼称する。

### ノートブック

[Jupyter Notebook](https://github.com/jupyter/notebook)とは、Markdownテキスト・数式・図などを含んだドキュメント作成とPythonなどのプログラミング実行環境を提供する環境で、授業資料は`.ipynb`という拡張子のJupyterNotebook用ファイルとして作成されている。授業ではこれを**ノートブック**や**Notebook**などと表記・呼称する。

`.ipynb`形式のソースファイルの管理と共有には、GitHubと呼ばれる環境を利用していて、ソースファイルは[こちら](https://github.com/SotaYoshida/Lecture_DataScience)からも閲覧できる(この授業を受講したりプログラムを実行するのに皆さんがGitHubのアカウントを取得したりこのリンクを開いたりする必要は特段ありません)。
Jupyter Notebookを編集・実行するための環境はいくつかあるが、本授業では環境構築やそれにかかるトラブルシューティングを最小化するために、Google Colaboratoryというサービスを利用して**Googleのクラウド環境上でJupyter Nootebookを編集・実行する方式**を採用している。

:::{note}
**授業に先立ってGoogleのアカウントの新規取得をお願いします**
:::

**ブック**は概要をとらえたり復習をするときには見やすくて便利だが、実際に自身でコードを実行したりプログラムを書く場合には**Google Colaboratory上でJupyter Notebookを開く**ことになる。  
Google Colab.上でノートブックを開くには、各章の冒頭に用意された"Open in Colab"というボタンをクリックするか、上のロケットの形をしたボタンにマウスオーバーして"Colab"から開く。左の"Google Colaboratoryの使い方"や第1章のノートブックで試してみよう。参考:
![](notebooks/pic_for_notebook/pic_0_0.png)


### 講義の予定

各回の予定と対応する資料の章を括弧内に書いておく。予定はあくまでも予定...。

- 第1回: ガイダンスとGoogle Colab等の説明  (Google Colaboratoryの使い方)
- 第2回: 機械学習とはなにか？ 
- 第3回: 基本的な変数と演算 (1. Pythonの基本 その１)
- 第4回: リストとループ処理 (2. Pythonの基本 その２)
- 第5回: 関数 (3. 関数) 
- 第6回: モジュールと可視化 (4. モジュールと可視化)
- 第7回: 確率と疑似乱数 (5.確率と疑似乱数)
- 第8回: ファイル・文字列操作 (6.ファイル・文字列操作)
- 第9回: 相関・回帰分析 (7.相関回帰分析)
- 第10回: 最適化問題の基礎 (8. 最適化問題の基礎)
- 第11回: 発展:実験計画 (おまけ ベイズ最適化による実験計画法)
- 第12回: 発展:Pandas (おまけ Pandasの使い方 (基礎))
- 第13回: 最終課題1
- 第14回: 最終課題2
- 第15回: 最終課題3


## 不具合報告または問い合わせ

本講義資料に関する不具合(リンク切れなど)の報告や問い合わせについては下記のフォームよりお願いします。
授業受講者からの不具合報告関しては授業やCL等で返答します。授業外の問い合わせについては、お答え出来ない場合もありますので予めご了承ください。

<iframe src="https://docs.google.com/forms/d/e/1FAIpQLSe9kSorMjkJPhbHqDWUwBNykaZ1yVDZ1eGl-5goFnNS-vQsQA/viewform?embedded=true" width="900" height="800" frameborder="0" marginheight="0" marginwidth="0">読み込んでいます…</iframe>