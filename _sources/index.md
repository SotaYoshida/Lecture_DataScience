# 実践データサイエンス

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
(第1章のノートブックで試してみてください)
<img src="https://github.com/SotaYoshida/Lecture_DataScience/blob/main/notebooks/pic_for_notebook/pic_0_0.jpg" width = 80%>


#### 数式の挿入

Jupyter Nootebookでは$\LaTeX$形式の数式をサポートしていてドルマークで囲むと、数式を表示させることが出来る。  
$f(x) = \frac{1}{2}\exp{(-2x^2 + 3x + 5)}$

### Google Colaboratoryの使い方

:::{note}
以下の内容は、Google Colaboratoryや関連サービスのアップデートに伴い、数ヶ月経つと微妙に設定の文言が変更されている場合があります。適宜対応するものに置き換えて読んでいただけると助かります。
:::

Google Colaboratory上でノートブックを開くと、下記のような画面が開きます。

ユーザーは
- テキストセル
- コードセル

の２つを駆使して、自分だけのノートブックを作成したり、他者が作成した`.ipynb`形式のファイルを開いてGoogle Colab.上でプログラムを実行したりできます。

#### 重要な注

ブックから開いたノートブック
```{margin}
ノートブックの実体(ソースファイル)は[GitHub上](https://github.com/SotaYoshida/Lecture_DataScience)にあります
```
は、皆さんがコピーをするなどしない限り、実行はできますが保存はできません。  
**必ず、[ファイル]から[ドライブにコピーを保存]し、ご自身のファイルを編集・保存するようにしてください**

ノートブックのファイル名の横にGitHubのロゴ(タコ足猫)が表示されている場合、皆さんが開いているのはGitHubからインポートされたノートブックであって、皆さん自身のファイルではありません。  
途中でうっかりタブやブラウザを閉じてしまうと作業内容が消えてしまいます。

![](https://drive.google.com/uc?export=view&id=1cs1XEAz0qbG2RtOqt1eIPGGiO9fngUE-)  


私も一連の講義資料作成時にGitHubから開いたノートブックを直接編集して数時間分の作業内容を消してしまったことが何度もあります...。辛いです。

コピーを編集している場合は、左上のノートブック名の隣がGoogle driveのロゴになっているはずです。  
この場合、編集されたものはGoogle Driveに一定時間で自動でバックアップされるので安心ですし、いつでもどの端末からでも開いて作業を再開することができます。  
![](https://drive.google.com/uc?export=view&id=1IibFQS1TVq6xDhG62AP9yG2Sy0c89Zut)


```{margin}
MS Officeなど、他の多くのソフトでも共通のショートカットなので、こまめに保存する手クセを付けておきましょう。
保存!保存!!保存!!!
```
Windowsなら`Ctrl+ S`, Macなら`Command + S`を押すことで随時Google Driveにバックアップを保存することができます。  
誤った内容に編集してしまった場合もGoogle Colaboratoryの"最終編集: X月Y日"といったところやGoogle Drive上でファイルの上で右クリック→"版を管理"から復元することができます。

#### なんか挙動が変だな、と思ったら。

複数のセルにまたがるコードを実行していくうちに変数に意図しないものが入っていたりなんか変だな、挙動が怪しいな、と思ったら[ランタイム]や[編集]などから下記の操作を行ってみましょう。

* セルの実行を停止したい場合: [ランタイム]→[実行の中断]で中断 (or [セッションの管理]から不要なセッションを削除する)
* 再起動したい場合: [ランタイム]→[ランタイムを再起動]
* 出力をいったん全部消したい: [編集]→[出力をすべて消去]

#### Google Driveからファイルのインポート

Google Colaboratoryでは、Google Driveに保存されたファイルの内容を読み込んだり、逆にコードでテキストファイル,エクセルファイルや画像,音声などを作成しGoogle Driveに保存することができます。

お使いのアカウントのDriveをGoogle colab.から操作する方法は主に2通りあります。

1つめ:  
以下を実行し、出てくるURLに遷移  
authorization codeをコピーし枠内に貼り付けてEnterを押す  
(Google colabからgoogle driveのファイルにアクセスできるようになります)

```Python
from google.colab import drive
drive.mount('/content/drive/') ##google driveを/content/という場所にマウント (２番めと整合するようにパスを選びましたが、マウントする場所は自由に選べます)
```

たとえばgoogle drive直下にあるXXX.pngというファイルを指定したい場合は
```Python
filename = "/content/drive/My Drive/XXX.png"
```
とすれば良い。

2つめ:  
Google Colabの左側にあるフォルダマークをクリックし、(「ファイルのブラウジングを有効にするには、ランタイムに接続してください。」と出る場合は、少し待ってください)  
次に、Google driveのロゴがついたフォルダをクリックする(画像の、[ファイル]というところの右下にある、driveのロゴがついたグレーがかったフォルダマーク)  
![](https://drive.google.com/uc?export=view&id=1RMjCaZN7emkVBqlYF-gFMcG8FRnw-9Xv)

この場合は自動で```/content/drive```という場所にマウントされるので(仕様が変更になる可能性あり)  
google drive直下にあるXXX.pngというファイルを指定したい場合はやはり
```Python
filename = "/content/drive/My Drive/XXX.png"
```
などとすれば良い。  
また、driveを一度マウントした後でパスがわからなくなったときには左の[ファイル]からdriveに相当するフォルダにマウスオーバーして縦3点$\vdots$から[パスをコピー]で、パスをクリップボードにコピーすることができます。


#### シェルコマンドとドライブ内のファイルのパス

Google Colab.では先頭にエクスクラメーションマークをつけることで
* ls (リスト,ファイル等表示)
* mkdir (ディレクトリ作成)

などのLinux/Unixで用いられるコマンドを実行することもできる。  
たとえばGoogle Driveをマウントした後にマイドライブ直下にあるpng画像のリストを表示させたければ
```bash
!ls /content/drive/MyDrive/*.png 
```
とすればよい。
なお、半角のアスタリスクはワイルドカード記号「対象を任意に」という命令になっている。


