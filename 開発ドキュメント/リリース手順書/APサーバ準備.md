# FastAPI アプリ Render デプロイ手順

このドキュメントは、FastAPI アプリを Render にデプロイする手順をまとめたものです。Render へのサインアップからデプロイ、ログの確認までを含みます。

## 前提条件

- FastAPI アプリのルートに `start.sh` を設置済み（Uvicorn 起動スクリプト）

```bash
#!/bin/bash
uvicorn api.routes.main:app --host 0.0.0.0 --port 10000
```

- `requirements.txt` がルートに存在している
- GitHub リポジトリに FastAPI アプリが push 済み

---

## 1. Render にサインアップ/ログイン

1. https://render.com にアクセス
2. 「Sign Up」もしくは「Log In」をクリック
3. GitHub アカウントと連携してログイン

---

## 2. 新しい Web Service の作成

1. 「New +」ボタンを押して「Web Service」を選択
2. GitHub のリポジトリ一覧から、対象の FastAPI アプリを選択
3. 以下の項目を設定

| 項目 | 設定例 |
|------|--------|
| Name | 任意のアプリ名（例: `fastapi-app`） |
| Region | `Singapore` など |
| Branch | `main` など、デプロイ対象ブランチ |
| Build Command | 空欄（不要） |
| Start Command | `./start.sh` |
| Environment | Python など自動選択される |
| Instance Type | Free を選択可能 |
| Port | 空欄（Renderが自動でPORTを環境変数として渡す） |

4. 「Create Web Service」をクリック

---

## 3. 実行確認

1. 以下のような実行ログが表示されていることを確認する
```log
INFO:     Uvicorn running on http://0.0.0.0:10000 (Press CTRL+C to quit)
INFO:     Application startup complete.
```

2. デプロイOKになると以下の形式でAPサーバのURLが動作するようになる

```url
https://<レポジトリ名>.onrender.com
```