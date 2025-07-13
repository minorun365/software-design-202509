# Mastra MCPホスト

Mastraで開発したMCPホストのサンプルコードです。

## 起動手順

`3_mastra-mcp/src/mastra/index.ts` 内の以下部分に、PythonとMCPサーバーのフルパスを記載する

```ts
// MCPサーバーを設定
const mcp = new MCPClient({
    servers: {
        sequential: {
            command: "/Absolute/path/to/python",
            args: ["/Absolute/path/to/aws_updates.py"]
        },
    },
});
```

https://console.anthropic.com/ でAnthropicのAPIキーを取得する（最低5ドルのクレジットをチャージする必要あり）

MCPサーバーと別のターミナルを起動し、環境変数にAPIキーをセットする

```sh
export ANTHROPIC_API_KEY=sk-xxxxx（あなたのAPIキーを入力）
```

MCPホストアプリを起動する

```sh
cd 3_mastra-mcp
npm install
npm run dev
```

http://localhost:4111 にアクセスし、エージェントを選択して `Amazon Bedrockのアップデートを教えて` などのプロンプトを入力する