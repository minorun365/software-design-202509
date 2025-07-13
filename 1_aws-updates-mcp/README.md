# AWSアップデート検索MCPサーバー

AWS What's NewのRSSフィードから、与えられたキーワードで最新のコンテンツを検索します。

## 機能

- Tool: `search_aws_updates`
  - キーワードを入力すると、最新のAWSアップデートを最大3件まで検索して返す

## 利用方法

MCPホストアプリへサーバー設定を実施する

```json
{
  "mcpServers": {
    "aws-updates": {
      "command": "/Absolute/path/to/sample-mcp-server/python",
      "args": ["/Absolute/path/to/sample-mcp-server/aws_updates.py"]
    }
  }
}
```

その後、MCPホストを起動して「Amazon Bedrockのアップデートを教えて」などのプロンプトを入力してみましょう。