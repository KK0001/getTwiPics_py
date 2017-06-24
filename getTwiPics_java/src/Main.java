import twitter4j.StallWarning;
import twitter4j.Status;
import twitter4j.StatusDeletionNotice;
import twitter4j.StatusListener;
import twitter4j.TwitterStream;
import twitter4j.TwitterStreamFactory;
import twitter4j.auth.AccessToken;
import twitter4j.auth.OAuthAuthorization;
import twitter4j.conf.Configuration;
import twitter4j.conf.ConfigurationBuilder;

import java.io.*;
import java.net.*;
import java.nio.channels.Channels;
import java.nio.channels.ReadableByteChannel;


public class Main{

    public static void main(String[] args) {
        // インスタンス
        Configuration conf = new ConfigurationBuilder().build();
        OAuthAuthorization oauth = new OAuthAuthorization(conf);

        // OAuth関係(入力必須)
        oauth.setOAuthConsumer(consumerKey, consumerSecret);
        oauth.setOAuthAccessToken(new AccessToken(token, tokenSecret));

        // Streamのインスタンス
        TwitterStream stream = new TwitterStreamFactory().getInstance(oauth);


        // 初回起動時はイメージ保存先フォルダを作る
        File dir = new File("./images");
        if (!dir.exists())
            dir.mkdir();

        // Listener
        StatusListener listener = new StatusListener(){
            @Override
            public void onException(Exception arg0) {
                //do nothing
            }
            @Override
            public void onTrackLimitationNotice(int arg0) {
                //do nothing
            }
            @Override
            public void onStatus(Status status) {
                //get tweets
                System.out.println("------------------------------"); //仕切り的なもの
                System.out.println(status.getText()); //ツイート
                System.out.println(status.getUser().getName()); //ツイートしたユーザー
                if(status.getExtendedMediaEntities().length >= 1){
                    for(int i=0 ; i <= status.getExtendedMediaEntities().length ; i++){
                        String imageURL = status.getExtendedMediaEntities()[i].getMediaURL();
                        download2(imageURL); // ダウンロード
                    }
                }

            }
            @Override
            public void onStallWarning(StallWarning arg0) {
                //do nothing
            }
            @Override
            public void onScrubGeo(long arg0, long arg1) {
                //do nothing
            }
            @Override
            public void onDeletionNotice(StatusDeletionNotice arg0) {
                //do nothing
            }
        };

        // 上のListenerをStreamにAdd
        stream.addListener(listener);

        // TLを開始
        stream.user();
    }

    // ダウンローダー


    //ダウンローダー
    private static void download2(String imageURL){
        try {

            URL url = new URL(imageURL); // URL

            // ファイル名の決定
            String path = url.getFile(); // パス
            String[] parts = path.split("/"); // ファイル名を取得したい
            String fileName = parts[parts.length - 1]; // 最終のファイル名
            String filePath = "./images/"+fileName;

            // ダウンロード
//            URL website = new URL(imageURL);
            ReadableByteChannel rbc = Channels.newChannel(url.openStream());
            FileOutputStream fos = new FileOutputStream(filePath);
            fos.getChannel().transferFrom(rbc, 0, Long.MAX_VALUE);


            System.out.println("saved "+imageURL);

        } catch (FileNotFoundException e) {
            System.err.println(e);
        } catch (MalformedURLException e) {
            System.err.println(e);
        } catch (IOException e) {
            System.err.println(e);
        }

    }
}
