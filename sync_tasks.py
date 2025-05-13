import requests
import os
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

# GitHub API URL
API_URL = os.getenv("GITHUB_DOCUMENT_REPOS")

# GitHubトークン
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

# GitHub APIヘッダー
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# タスクファイルを読み込む
with open('task.md', 'r') as file:
    tasks = file.readlines()

# 既存のIssueを取得
response = requests.get(API_URL, headers=headers)
# デバッグ出力
print("Status Code:", response.status_code)
print("Response Text:", response.text)
issues = response.json()

existing_issues = [issue['title'] for issue in issues]

# 新しいタスクをIssueに追加
for task in tasks:
    if task.strip() not in existing_issues:
        data = {
            "title": task.strip(),
            "body": "Task from task.md",
            "state": "open"
        }
        response = requests.post(API_URL, json=data, headers=headers)
        if response.status_code == 201:
            print(f"Created issue for task: {task.strip()}")

# 削除されたタスクのIssueを閉じる
for issue in issues:
    if issue['title'] not in tasks:
        issue_data = {
            "state": "closed"
        }
        response = requests.patch(f"{API_URL}/{issue['number']}", json=issue_data, headers=headers)
        if response.status_code == 200:
            print(f"Closed issue: {issue['title']}")
