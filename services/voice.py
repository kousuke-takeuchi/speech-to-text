import pyaudio
import wave


'''マイクから録音し、wavデータを作成する
参考 -> https://to-kei.net/python/google-cloud-speech-api/
:params: filename ファイル名
:params: channels 1-モノラル 2-ステレオ
:params: rate サンプルレート
:params: chunk データ点数
:params: record_seconds 録音する時間の長さ（秒）
'''
def record(filename, channels=2, rate=44100, chunk=1024, record_seconds=5):
    # 基本情報の設定
    format = pyaudio.paInt16
    audio = pyaudio.PyAudio()
    # ioの確保
    stream = audio.open(format=format,
                        channels=channels,
                        rate=rate,
                        input=True,
                        frames_per_buffer=chunk)

    # 録音開始
    print ("recording...")
    frames = []
    for i in range(0, int(rate / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # ioの開放と録音終了
    stream.stop_stream()
    stream.close()
    audio.terminate()
    print ("finished recording")

    # waveファイルへの書き込みと保存
    waveFile = wave.open(filename, 'wb')
    waveFile.setnchannels(channels)
    waveFile.setsampwidth(audio.get_sample_size(format))
    waveFile.setframerate(rate)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
