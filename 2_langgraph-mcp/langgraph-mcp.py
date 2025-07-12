import asyncio
from langgraph.prebuilt import create_react_agent
from langchain_mcp_adapters.tools import load_mcp_tools
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# MCPサーバーを設定
server_params = StdioServerParameters(
    command="/Absolute/path/to/python3",
    args=["/Absolute/path/to/aws_updates.py"]
)

async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # AIエージェントを作成
            agent = create_react_agent(
                model="anthropic:claude-4-sonnet-20250514",
                tools=await load_mcp_tools(session)
            )

            # AIエージェントを呼び出し
            response = await agent.ainvoke(
                {"messages": "Amazon Bedrockのアップデートを教えて"}
            )
            print(response["messages"][-1].content)

# 非同期実行
asyncio.run(main())