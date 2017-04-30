#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from mastodon import Mastodon

###
# 参考: http://qiita.com/code_monkey/items/e4929ef13e2a2032d467
#
###

Mastodon.create_app("ここにクライアント名(好きな名前を入れられます)",
                    api_base_url = "https://pawoo.net", # サーバーアドレス
                    to_file = "hoge.txt" # 出力先ファイル名
                    )

mastodon = Mastodon(client_id="hoge.txt",
                    api_base_url = "https://pawoo.net"
                    )

mastodon.log_in("ここにメールアドレス","ここにパスワード",
                to_file = "hoge.txt"
                )
