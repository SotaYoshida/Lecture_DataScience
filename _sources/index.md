# 資料:実践データサイエンス

本コンテンツは宇都宮大学の基盤科目「実践データサイエンス」の授業資料です。


## 資料の使い方

本講義で用いる資料には幾つか種類(≒ファイル形式)がある。
慣れないうちは混同するかと思うので、ここに資料自体の説明と各種アプリケーションやサービスの説明をまとめておく。

### ブック
本資料は[Jupyter Notebook](https://github.com/jupyter/notebook)形式で作成されたソースファイルを[Jupyter Book](https://jupyterbook.org/en/stable/intro.html)を用いて変換することで作成されたコンテンツです。
授業内では**ブック**ないし"Book"と表記・呼称します。  
概要を理解したり復習する際にはこちらのブックを閲覧してください。

### ノートブック

[Jupyter Notebook](https://github.com/jupyter/notebook)とは、Markdownテキスト・数式・図などを含んだドキュメント作成とPythonなどのプログラミング実行環境とを提供する環境で、授業資料は`.ipynb`という拡張子を持つ、Jupyter Notebook形式のファイルとして作成されています。  
またGitHubと呼ばれるサービスを利用してこれらのソースファイルの管理と共有を行っています。  
(この授業を受講する上で、皆さんがGitHubのアカウントを取得したりする必要はありません)

Jupyter Notebookを編集・実行するための環境はいくつかありますが、本授業では環境構築やそれにかかるトラブルシューティングを最小化するために、Google Colaboratoryというサービスを利用して**Googleのクラウド環境上でJupyter Nootebookを編集・実行する方式**を採用します。

**ブック**は概要をとらえたり復習をするときには便利ですが、実際に自身でコードを実行したりプログラムを書く場合には**Google Colaboratory上でJupyter Notebookを開く**ことになります。

Google Colab.上でノートブックを開くには、各章の冒頭に用意された"Open in Colab"というボタンをクリックするか、上のロケットの形をしたボタンにマウスオーバーして"Colab"から開きます。
(第0章や第1章のノートブックで試してみてください)
![](notebooks/pic_for_notebook/pic_0_0.png)

