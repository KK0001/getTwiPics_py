#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from mastodon import Mastodon
import urllib
import os
import time

###
# mastodonのローカルタイムラインを流れるsensitiveな画像を保存していく。(今回はPawoo.net)
# 保存先は、『カレントディレクトリ/picsOnPawoo/ここ』にまとめて保存。
# ユーザー別にフォルダ分けはしません。
#
# 参考: http://qiita.com/code_monkey/items/e4929ef13e2a2032d467
###

def login():
    mastodon = Mastodon(
        client_id="hoge_clientcred.txt",
        access_token="hoge_clientcred.txt",
        api_base_url = "https://pawoo.net"
    )
    return mastodon

def download(url):
    if os.path.exists("./picsOnPawoo/") == False:
        os.makedirs("./picsOnPawoo/")

    img = urllib.request.urlopen(url)
    tmp_path = open("./picsOnPawoo/" + os.path.basename(url), "wb")
    tmp_path.write(img.read())
    img.close()
    tmp_path.close()


if __name__ == '__main__':
    mastodon = login()

    #タイムラインを取得
    while True:
        TL = mastodon.timeline_local()
        for toot in TL:

            #dawonload sensitive pictures only
            if len(toot["media_attachments"]) != 0 and toot["sensitive"] == True:
                url = toot["media_attachments"][0]["url"].split("?")[0]
                print(toot["account"]["username"] + "is uploaded picture")
                download(url)
        time.sleep(15)
