Speech to Textクラウドサービス比較
===============================

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

## 検討サービス
### Amazon
+ [AWS Transcribe](https://aws.amazon.com/jp/transcribe/)
+ [Alexa Voice Service (AVS)](https://github.com/alexa/avs-device-sdk/wiki/Raspberry-Pi-Quick-Start-Guide-with-Script)

### Google
+ [Cloud Speech-to-Text](https://cloud.google.com/speech-to-text/?hl=ja)
+ [Google Assistant SDK for devices](https://developers.google.com/assistant/sdk/)

### Microsoft
+ [Speech to Text](https://azure.microsoft.com/ja-jp/services/cognitive-services/speech-to-text/)

## 実装方針

|サービス|連携方法|依存ライブラリ|参考文献|
|:--|:--|:--|:--|
|AWS Transcribe|音声データをS3にアップロード後、S3のURLをTranscribe APIに渡してテキストに変換する|[Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)|[AWS Transcribe - ご利用開始にあたって (SDK for Python)](https://docs.aws.amazon.com/ja_jp/transcribe/latest/dg/getting-started-python.html)|
|AVS|Amazon Developerに製品登録してRaspberry PiでSDKの初期認証を行う。|[avs-device-sdk](https://github.com/alexa/avs-device-sdk)|[Raspberry PiでAlexa Voice Service(AVS)を利用する方法](https://qiita.com/zono_0/items/2c485b4176d349964876),[ラズパイでAlexaする](http://engetu21.hatenablog.com/entry/2018/08/20/230741),[Raspberry Pi Quick Start Guide](https://github.com/alexa/avs-device-sdk/wiki/Raspberry-Pi-Quick-Start-Guide)|
|Cloud Speech-to-Text|gcloudで認証後、GCSのAPIに音声データを送信する|[CLOUD SDK](https://cloud.google.com/sdk/?hl=ja)|[Google Cloud Speech APIのリアルタイム音声認識は使い物になる精度なのか？](https://qiita.com/hamham/items/9b553d0759a2319ea211)|
|Google Assistant SDK for devices|音声データをGoogle Assistant APIに送信し、IFTTTを経由して、Raspberry Piのサーバーで受信する|[Google Assistant SDK for devices - Python](https://github.com/googlesamples/assistant-sdk-python)|[Raspberry Pi にGoogle Assistant SDKを搭載して「OK Google」してみる。](https://qiita.com/PonDad/items/52eaa93338496b06cb1a)|
|Azure Speech to text|調査中|[Microsoft Cognitive Services Speech SDK](https://github.com/Azure-Samples/cognitive-services-speech-sdk)|[クイック スタート:Python から Speech Service を使用する](https://docs.microsoft.com/ja-jp/azure/cognitive-services/speech-service/quickstart-python)|

## 比較

\* 処理速度(s/req): 「こんにちは」と発言して、最初のAPIへのリクエストからテキストデータが返ってくるまでを計測し、10回実行した際の平均時間を掲載

### サービスタイプ

\* リアルタイム処理: 音声データをローカルでmp4に保存せずにAPIで直接分析する

\* mp4: 音声データをmp4に保存後に分析する

\* 非同期処理: 音声データをクラウドにアップロード後、クラウドのAPIを使ってバックグラウンドで分析する

|サービス|処理速度|サービスタイプ|
|:--|:--|:--|
|AWS Transcribe|(日本語非対応)|`非同期処理`|
|Azure Speech to text|||
