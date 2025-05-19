# ④ メール環境準備

---

### 1. mailpit インストールと起動
```bash
brew install mailpit
brew services start mailpit
```

### 2. メール管理画面アクセス
```
http://localhost:8025/
```

### 3. FastAPI メールAPI起動
```bash
uvicorn api.routes.main:app --reload
```
