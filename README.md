# getTwiPics_py
Twitter上でフォローしてるユーザー(あるいは、リストに追加しているユーザー)がアップロードした画像を自動で全部保存させたい。  

### 前提
Tweepyを使用。  
Python3.X。  

## 使い方
1. Python(3.~)の環境を準備。([ここ](http://www.pythonweb.jp/install/)などを参照するか、あるいはパッケージ管理ツール(pyenvなど)でインストールする。)  
注意: 忘れずにPATHを通しておくこと。

2. パッケージのインストールの準備。([ここ](http://prpr.hatenablog.jp/entry/2015/04/02/windows%E7%92%B0%E5%A2%83%E3%81%AEPython3.4%E3%81%A7pip%E3%82%92%E3%81%A4%E3%81%8B%E3%81%A3%E3%81%A6%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%99%E3%82%8B)などを参照すると良いかも。)

3. Tweepyをインストール。  
コンソールにて`$ sudo pip3 install tweepy`。  
だめだったら、`$ sudo pip install tweepy`とやってみると良いかも。

4. 起動したいPythonファイル内に、自分のConsumer KeyやConsumer Key Secretを記述するところがあるので、入力する。

5. Windowsの場合、起動したいファイルをダブルクリック。
(Macの場合、コンソールにて`$ Python3 ~.py`で起動。カレントディレクトリに注意。)

## ファイル一覧
### getTwiPics_past.py
自分(あるいは他人の)リストを取得し、追加されているユーザーを取得。そのユーザー達のツイートを遡り、アップロードされた画像を保存していく。1人に対して200ツイートほど遡って画像を保存する。  

### getTwiPics_TL.py
自分のタイムラインを取得し、画像が投稿されたら保存。  

### getPawooPics
mastodon(ここではPawoo.net)でも同じことがしたい。mastodon.pyという簡単にAPIが叩けるスクリプトがあるらしいので作ってみた。  
pipでmastodon.pyをインストールすれば使用可能。setup.pyを自分用に編集(クライアント名、hoge_clientcred.txtの名称変更、アカウント情報追加。)し、対応するgetPawooPics.pyの行を反映するように書き換え(login()部分。)れば準備完了。  

### getTwiPics_java
[ここ](https://github.com/KK0001/getTwiPics_java)で公開しています。  
javaバージョン。javaの勉強がてら作成してみた。TLに流れてきた画像を保存します。  
src/Main.java内のOAuthのところに自分のものを入力すれば準備完了。各自の環境で起動すればOK。  
