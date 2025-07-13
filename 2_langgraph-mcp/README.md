# LangGraph MCPホスト

LangGraphで開発したMCPホストのサンプルコードです。

## 起動手順

`2_langgraph-mcp/langgraph-mcp.py` 内の以下部分に、PythonとMCPサーバーのフルパスを記載する

```py
# MCPサーバーを設定
server_params = StdioServerParameters(
    command="/Absolute/path/to/python",
    args=["/Absolute/path/to/aws_updates.py"]
)
```

https://console.anthropic.com/ でAnthropicのAPIキーを取得する（最低5ドルのクレジットをチャージする必要あり）

```sh
export ANTHROPIC_API_KEY=sk-xxxxx（あなたのAPIキーを入力）
```

MCPホストアプリを起動する

```sh
cd 2_langgraph-mcp
pip install -r requirements.txt
python langgraph-mcp.py
```