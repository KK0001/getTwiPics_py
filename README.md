# getTwiPics_py
Twitter上でフォローしてるユーザー(あるいは、リストに追加しているユーザー)がアップロードした画像を自動で全部保存させたい。  

### 前提
Tweepyを使用。  
Python3.X。  

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
