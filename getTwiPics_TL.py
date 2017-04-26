#!/usr/bin/env python3
# -*- coding:utf-8 -*-

###
# タイムライン上の画像を保存する。
# bashにTLを流して、画像を見つけたら保存。
# 保存先としては、投稿者ユーザーのID(@~)のフォルダを『カレントディレクトリ/streamPics/userID』。
#
# 参考:
# http://kivantium.hateblo.jp/entry/2015/01/03/000225
# https://gist.github.com/kurozumi/d1228fc0761eb3dc128ad1b2abd8f818#file-twi-streaming-py
# http://thetree.hatenadiary.jp/entry/2017/02/19/python_標準出力のフラッシュ_sys.stdout.flush
###

import sys
import tweepy
import urllib
import os
import time

def get_oauth():
    CONSUMER_KEY=''
    CONSUMER_SECRET=''
    ACCESS_TOKEN_KEY=''
    ACCESS_TOKEN_SECRET=''

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
    return auth

class Listener(tweepy.StreamListener):
    def on_status(self, status):
        print('------------------------------')
        print(status.text)
        print(u"{name}({screen}) {created} via {src}\n".format(
                                                               name=status.author.name, screen=status.author.screen_name,
                                                               created=status.created_at, src=status.source))

        if hasattr(status, "extended_entities"):
            if "media" in status.extended_entities:
                if os.path.exists("./streamPics/" + status.author.screen_name) == False:
                    os.makedirs("./streamPics/" + status.author.screen_name)
                for index,media in enumerate(status.extended_entities["media"]):
                    img_url = media["media_url_https"]
                    print(status.author.screen_name + " image " +  str(img_url) + " save to ./streamPics/" + status.author.screen_name)
                    img = urllib.request.urlopen(img_url)
                    tmp_path = open("./streamPics/" + status.author.screen_name + "/" + os.path.basename(img_url), "wb")
                    tmp_path.write(img.read())
                    img.close()
                    tmp_path.close()

        return True

    def on_error(self, status_code):
        print('ERROR CODE: ' + str(status_code))
        return True

    def on_timeout(self):
        print('TIMEOUT...')
        return True

if __name__ == '__main__':
    auth=get_oauth()
    stream = tweepy.Stream(auth, Listener())

    while True:
      try:
        stream.userstream()
      except:
        # 10秒間sleepして再接続
        print("RECONNECTING...")
        for i in range(10):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(1)
        stream = tweepy.Stream(auth, Listner())
        print("RECONNECTED.")
