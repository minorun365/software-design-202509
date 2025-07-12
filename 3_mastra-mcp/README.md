# Mastra MCPホスト

Mastraで開発したMCPホストのサンプルコードです。

## 起動手順

### MCPサーバーの起動

MCPサーバーを事前に起動しておく

```sh
cd 1_aws-updates-mcp
python aws_updates.py
```

### MCPホストの事前準備

`3_mastra-mcp/src/mastra/index.ts` 内の以下部分に、PythonとMCPサーバーのフルパスを記載する

```ts
// MCPサーバーを設定
const mcp = new MCPClient({
    servers: {
        sequential: {
            // command: "/Absolute/path/to/python",
            command: "/Users/mi-onda/.pyenv/shims/python",
            // args: ["/Absolute/path/to/aws_updates.py"]
            args: ["/Users/mi-onda/git/software-design-202509/1_aws-updates-mcp/aws_updates.py"]
        },
    },
});
```

https://console.anthropic.com/ でAnthropicのAPIキーを取得する（最低5ドルのクレジットをチャージする必要あり）

### MCPホストの起動

MCPサーバーと別のターミナルを起動し、環境変数にAPIキーをセットする

```sh
export ANTHROPIC_API_KEY=sk-xxxxx（あなたのAPIキーを入力）
```

MCPホストアプリを起動する

```sh
cd 3_mastra-mcp
npm run dev
```

http://localhost:4111 にアクセスし、エージェントを選択して `Amazon Bedrockのアップデートを教えて` などのプロンプトを入力する