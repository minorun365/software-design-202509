import { Mastra } from "@mastra/core";
import { Agent } from "@mastra/core/agent";
import { MCPClient } from "@mastra/mcp";
import { anthropic } from "@ai-sdk/anthropic";

// MCPサーバーを設定
const mcp = new MCPClient({
    servers: {
        sequential: {
            command: "/Absolute/path/to/python",
            args: ["/Absolute/path/to/aws_updates.py"]
        },
    },
});

// AIエージェントを作成
const agent = new Agent({
    name: "AWSアップデート検索エージェント",
    instructions: "AWSアップデートを検索します",
    model: anthropic("claude-4-sonnet-20250514"),
    tools: await mcp.getTools(),
});

// Mastraインスタンスを作成
export const mastra = new Mastra({
    agents: { agent },
});
