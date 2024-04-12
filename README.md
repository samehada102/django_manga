# 概要
Django練習用、localhostで立ち上がる漫画管理アプリケーション。  
機能としては、漫画の登録、検索、編集、削除と漫画サイトの少年漫画ランキングの確認ができる。

# 環境
**Python 3.12.2**

| No. | ライブラリ名        | ver.   |
| :-- | :------------------ | :----- |
| 1   | django              | 5.0.4  |
| 2   | django-crispy-forms | 2.1    |
| 3   | django-filter       | 24.2   |
| 4   | crispy-bootstrap4   | 2024.1 |
| 5   | requests            | 2.31.0 |
| 6   | beautifulsoup4      | 4.12.3 |
| 7   | lxml                | 5.2.1 |

# アプリケーション起動手順
Windowsのコマンドプロンプトにて以下手順を実行してください。
1. 「python -m venv env」を入力し仮想環境を作成
2. 「.\env\Scripts\activate」で仮想環境を有効化
3. 本リポジトリ構成を「env」ディレクトリと同じ階層に入れる
4. 「pip install -r requirements.txt」で必要ライブラリのインストール
5. 「manage.py migrate」でDBを作成(ファイル名：db.sqlite3)
6. 「manage.py createsuperuser」で管理者アカウントを作成
7. 「manage.py runserver」で起動
8. ブラウザで「http://localhost:8000」にアクセス
9. ログイン画面が表示されるので手順4で作成したアカウントでログイン