import urllib.request
import xml.etree.ElementTree as ET
from typing import List, Dict
from mcp.server.fastmcp import FastMCP

# MCPサーバーを作成
mcp = FastMCP("AWSアップデート検索")

# ツールを定義
@mcp.tool()
def search_aws_updates(keyword: str) -> List[Dict[str, str]]:
    """AWSのアップデートをキーワードで検索し、結果を返す関数"""
    
    # RSSフィードを取得・解析
    with urllib.request.urlopen("https://aws.amazon.com/new/feed/") as response:
        root = ET.fromstring(response.read())
    
    results = []
    
    # 各記事をチェック
    for item in root.findall('.//item'):
        title = getattr(item.find('title'), 'text', '') or ''
        desc = getattr(item.find('description'), 'text', '') or ''
        date = getattr(item.find('pubDate'), 'text', '') or ''
        
        # キーワードが含まれているかチェック
        if keyword.lower() in title.lower() or keyword.lower() in desc.lower():
            results.append({
                'title': title,
                'desc': desc[:100] + '...' if len(desc) > 100 else desc,
                'date': date
            })
            
            # 3件で終了
            if len(results) >= 3:
                break

    return results

# MCPサーバーを起動
mcp.run()