# Supabase データベース接続手順（ローカルから）

このドキュメントは、Supabase 上で PostgreSQL データベースを作成し、ローカル環境から `psql` コマンドで接続して動作確認する手順をまとめたものです。

---

## 1. Supabase プロジェクトの作成

1. [https://supabase.com/](https://supabase.com/) にアクセス
2. アカウントを作成してログイン
3. 新しいプロジェクトを作成
    - Project name: 任意の名前
    - Password: データベース接続用のパスワード（強力なものを設定）
    - Region: 任意（例: ap-northeast-1）
4. 作成完了

---

## 2. 接続情報の確認

1. Supabase ダッシュボードにログイン
2. ダッシュボードから「「Connect」を選択
3. Type「PSQL」を選択
4. 「Transaction pooler」のコマンドかparametersをコピー
```bash
psql -h <your-host> -p <your-port> -d <your-db> -U <your-username>
```

## 3. ローカルからの接続（psql）

### 必要条件

- `psql` コマンドがインストールされていること  

### 接続コマンド

1. コマンドを実行
```bash
psql -h <your-host> -p <your-port> -d <your-db> -U <your-username>
```
2. パスワードを入力すると、ログインできる