# SMTP サーバ準備手順

このドキュメントでは、FastAPI などのアプリケーションからメールを送信するために必要な SMTP サーバ設定の準備手順をまとめます。ここでは Brevo（旧 Sendinblue）を例に説明します。

---

## 1. SMTP アカウントの準備

1. Brevo にアカウント登録（ https://www.brevo.com/ ）
2. ダッシュボードの右上のユーザー設定から「SMTP & API」メニューにアクセス
3. 「SMTP」タブにて以下を確認・取得：

   - SMTPサーバ: `smtp-relay.brevo.com`
   - ポート番号: `587`
   - ログイン（SMTP_USER）: `xxxxx@smtp-brevo.com`
   - パスワード（SMTP_PASS / SMTP key value）: 作成または再発行

---

## 2. 送信元アドレス（EMAIL_FROM）の設定

1. Brevo ダッシュボードから「送信者とドメイン」を開く
2. 使用したいメールアドレス（例: `noreply@example.com`）を送信者として追加
3. メール認証リンクを受信し、承認する
   - 認証が完了していないアドレスからは送信できません

---

## 3. .env ファイルの設定例

以下のように環境変数を設定します：

```env
SMTP_HOST=smtp-relay.brevo.com
SMTP_PORT=587
SMTP_USER=xxxxx@smtp-brevo.com
SMTP_PASS=your_generated_password
EMAIL_FROM=noreply@example.com
```