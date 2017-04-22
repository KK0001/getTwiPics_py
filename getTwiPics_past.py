#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# http://ayihis.hatenablog.com/entry/2016/06/24/172435 のほぼパクリ。
# 自分用に(ついでにPy3で動くように)改良しました。
# 自分のツイッターリストからユーザーを取得して画像を保存します。
# Python3で動きます。

import sys
import tweepy
import urllib
import os

def get_oauth():
    CONSUMER_KEY=''
    CONSUMER_SECRET=''
    ACCESS_TOKEN_KEY=''
    ACCESS_TOKEN_SECRET=''

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
    return auth

if __name__ == "__main__":
    auth=get_oauth()
    api=tweepy.API(auth)

    userList={} #py用に絵師リストを作る

    screen_name="" #リスト作成者のtwitterID
    listname="" #リスト名
    for member in tweepy.Cursor(api.list_members,slug=listname,owner_screen_name=screen_name).items():
        print(member.screen_name)
        userList[member.screen_name]=member.screen_name
    print(".....got users!")

    ###
    # あるいは、自分でユーザーIDを入力しても良い。
    # userList={} にディクショナリ型で書き込めば、特定ユーザーの画像を保存対象にできる。
    # その場合、上の「screen_name=~」から「print(".....got users!")」までをコメントアウト等しておく。
    ###

    # 取得したユーザー名を表示
    print("---------------------------")
    for name,twi_id in userList.items():
        print("userID:" + twi_id)
    print("---------------------------")

    # Picsの取得
    count=0 # 12人以上の場合に対策をするため
    for name,twi_id in userList.items():
        maxid = api.user_timeline(twi_id).max_id
        count+=1
        if os.path.exists("./twitterPics/" + name) == False:
            os.makedirs("./twitterPics/" + name)
        for l in range(16):
            for twi in api.user_timeline(twi_id, count=200, max_id=maxid):
                if hasattr(twi, "extended_entities"):
                    if "media" in twi.extended_entities:
                        for index,media in enumerate(twi.extended_entities["media"]):
                            img_url = media["media_url_https"]
                            print(name + " image " +  str(img_url) + " save to ./twitterPics/" + name)
                            img = urllib.request.urlopen(img_url)
                            tmp_path = open("./twitterPics/" + name + "/" + os.path.basename(img_url), "wb")
                            tmp_path.write(img.read())
                            img.close()
                            tmp_path.close()
                maxid = twi.id

        # 15分で180回以上のリクエストができないので対策(15分休む)
        if count==11:
            for i in range(900):
                print(i)
                time.sleep(1)
