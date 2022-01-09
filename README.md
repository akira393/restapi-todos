# restapi-todos

## 手順

- forkする
	- `https://github.com/GomaGoma676/restapi-todos`
- corsのurlを変更する
	- 今回は、`CORS_ORIGIN_ALLOW_ALL=True`を追加した
  - reactの環境をcodesandboxで用意したかったため
- requirementsのファイル名を変更する
  - `pa_autoconfigure_django.py`でセットアップを行う場合、デフォルトで`requirements.txt`を読み込むため
	- `requirements-dev.txt` to `requirements.txt`
- pythonanywhereでアカウント作成
- api tokenを作成
- bashコンソールに移動
- `pip install --user pythonanywhere`のインストール
- `pa_autoconfigure_django.py --pytho=3.8 https://github.com/<your user name>/restapi-todos.git --nuke`の実行
	- `--nuke`オプションは初めて実行する場合はいらない

- 管理者アカウントの作成
```bash
$ python manage.py createsuperuser
Username (leave blank to use 'xxxx'): adminadmin
Email address: admin@adomin.admin
Password: adminadmin
```

## **動作確認**

## **注意点**
- api tokenを作成する前に、コンソールを起動させちゃったら一度コンソールから抜ける
- 必要なライブラリがあれば、プロジェクト直下に`requirements.txt`というファイル名で格納する

