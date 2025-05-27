# PartnerReminder

**PartnerReminder** は、彼女と会話した内容や彼女の好きなところ、お互いの服装や次回までにやっておくべきことなどを覚えておくことができるアプリです。

## 特徴

- 会話した内容やお互いの服装などをデート情報として管理できる。
- これまでのデート情報から彼女の良いところを一覧で確認できる。
- デート前日に彼女の良いところや次回までに取り組むことのリマインドメールを受け取ることができる。

## 公開URL
```
https://project-react-partner-reminder.vercel.app/
```

## 主な画面

<a href="https://github.com/kondo-akihiro-git/project-document-PartnerReminder/tree/main/%E7%94%BB%E9%9D%A2">画面一覧ページ</a>

## 主な機能

- 以下、デート関連の機能
  - デート情報登録/編集/削除機能
  - 彼女の良いところ一覧表示機能
  - 次回デートのスケジュール追加機能
  - デート前日にリマインドメールを自動送信

- 以下、ユーザー関連の機能
  - 新規ユーザー登録機能
  - メールアドレス認証機能
  - ログイン/ログアウト機能
  - ユーザー設定機能


## 使用技術

- **フロントエンド**: React
- **バックエンド**: FastAPI
- **データベース**: PostgreSQL
- **メール送信**: SMTP
- **バッチスケジューラ**: APScheduler



## 使用サービス

| サーバ名（例）                         | サービス名                              | 用途                                  | URL                                      |
|---------------------------------------|-----------------------------------------|--------------------------------------|-------------------------------------------|
| **フロントエンド**              | **Vercel**                              | フロントエンドのホスティング             | https://vercel.com                        |
| **バックエンド**                | **Render**                              | バックエンド(API/Batch)のホスティング   | https://render.com                        |
| **バッチジョブ**                | **Cron-job.org**                        | 定期実行ジョブ管理                      | https://cron-job.org                      |
| **データベース**                | **Supabase**                            | DB管理                                  | https://supabase.com                      |
| **画像保存サーバ**                    | **Cloudinary**                          | 画像の保存と取得                        | https://cloudinary.com                    |
| **SMTPサーバ**                  | **Brevo**              | メール送信・SMTPサービス                | https://www.brevo.com                     |
| **メール受信確認サーバ**              | **Mailpit**                             | 開発用メール受信確認                    | https://mailpit.axllent.org/              |



## レポジトリ

### フロントエンド
[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=kondo-akihiro-git&repo=project-React-PartnerReminder)](https://github.com/kondo-akihiro-git/project-React-PartnerReminder)

### バックエンド(API)
[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=kondo-akihiro-git&repo=project-FastAPI-PartnerReminder)](https://github.com/kondo-akihiro-git/project-FastAPI-PartnerReminder)

### バックエンド(Batch)
[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=kondo-akihiro-git&repo=project-Batch-PartnerReminder)](https://github.com/kondo-akihiro-git/project-Batch-PartnerReminder)

### ドキュメント
[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=kondo-akihiro-git&repo=project-document-PartnerReminder)](https://github.com/kondo-akihiro-git/project-document-PartnerReminder)
