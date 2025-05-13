import requests
import os
import re

# GitHub API URL とトークン
GITHUB_TOKEN = os.environ.get("API_TOKEN")
API_URL = os.environ.get("DOCUMENT_REPOS")

if not GITHUB_TOKEN:
    raise ValueError("API_TOKEN is not set.")
if not API_URL:
    raise ValueError("DOCUMENT_REPOS is not set.")

headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# タスクファイル読み込み
with open('task.md', 'r') as file:
    task_lines = file.readlines()

# タスクをIDでマッピング
task_map = {}
task_pattern = re.compile(r'^\[(ID\d+)\]\s*(.+)$')

for line in task_lines:
    match = task_pattern.match(line.strip())
    if match:
        task_id, task_title = match.groups()
        task_map[task_id] = task_title

# 既存のIssueを取得
response = requests.get(API_URL, headers=headers)
if response.status_code != 200:
    raise RuntimeError("Failed to fetch issues")

issues = response.json()

# 既存IssueをIDでマッピング
issue_map = {}
for issue in issues:
    match = task_pattern.match(issue['title'])
    if match:
        issue_id, _ = match.groups()
        issue_map[issue_id] = issue

# タスクをIssueに反映（作成 or 更新）
for task_id, task_title in task_map.items():
    title = f"[{task_id}] {task_title}"
    if task_id not in issue_map:
        # 新規Issue作成
        data = {
            "title": title,
            "body": "Task from task.md",
            "state": "open"
        }
        res = requests.post(API_URL, json=data, headers=headers)
        if res.status_code == 201:
            print(f"Issue created: {title}")
    else:
        # 既存Issueタイトルが違えば更新（タイトル変更対応）
        issue = issue_map[task_id]
        if issue['title'] != title:
            res = requests.patch(f"{API_URL}/{issue['number']}", json={"title": title}, headers=headers)
            if res.status_code == 200:
                print(f"Issue title updated: {task_id}")

# 不要なIssueはClose
task_ids = set(task_map.keys())
for issue_id, issue in issue_map.items():
    if issue_id not in task_ids:
        res = requests.patch(f"{API_URL}/{issue['number']}", json={"state": "closed"}, headers=headers)
        if res.status_code == 200:
            print(f"Issue closed: {issue['title']}")
