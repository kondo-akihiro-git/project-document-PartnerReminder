# ③ PostgreSQL準備

---

### 1. PostgreSQL インストールと起動
```bash
brew install postgresql
brew services start postgresql
```

### 2. psql にログイン
```bash
psql postgres
```

### 3. ユーザー作成
```sql
CREATE USER myuser WITH PASSWORD 'mypassword';
```

### 4. データベース作成
```sql
CREATE DATABASE mydb OWNER myuser;
```

### 5. 権限付与
```sql
GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;
```

### 6. psql 終了
```sql
exit
```

### 7. データベースに接続
```bash
psql -U myuser -d mydb
```

### 8. テーブル作成とデータ挿入
```sql
CREATE TABLE ...
```
