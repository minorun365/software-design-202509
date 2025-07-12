# AWSアップデート検索MCPサーバー

AWS What's NewのRSSフィードから、与えられたキーワードで最新のコンテンツを検索します。

## 機能

- Tool: `search_aws_updates`
  - キーワードを入力すると、最新のAWSアップデートを最大3件まで検索して返す

## 利用方法

MCPサーバーの起動

```zsh
python aws_updates.py
```

MCPホストアプリへサーバー設定を実施

```json
{
  "mcpServers": {
    "aws-updates": {
      "command": "/Absolute/path/to/python",
      "args": ["/Absolute/path/to/sample-mcp-server/aws_updates.py"]
    }
  }
}
```