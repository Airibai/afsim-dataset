# test_auth.py - 最小化 Token 验证脚本
import requests
import json

# 🔴 请替换为您的真实 Token
TOKEN = "eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFM1MTIifQ.eyJqdGkiOiI4MDkwMDY5MiIsInJvbCI6IlJPTEVfUkVHSVNURVIiLCJpc3MiOiJPcGVuWExhYiIsImlhdCI6MTc3NDg1NTIwMywiY2xpZW50SWQiOiJsa3pkeDU3bnZ5MjJqa3BxOXgydyIsInBob25lIjoiIiwib3BlbklkIjpudWxsLCJ1dWlkIjoiMmJkZjBkYzEtOGJlYi00ZjYwLWFmMWMtZWZkOWEyMTcwMTg1IiwiZW1haWwiOiIiLCJleHAiOjE3ODI2MzEyMDN9.sd9mG8LYCpS9FKqOJswjrP5eDPkkTCy5OJfEY1R98BIMO6zhOuzJPGnHIO7dZJMvRcn50ZucLzWIC7VeJPVSGw"  

    
# 1. 检查 Token 格式
if not TOKEN.startswith("sk-") and not TOKEN.startswith("mr-") and not TOKEN.startswith("eyJ"):
    print(f"⚠️  警告：Token 格式看起来不对：{TOKEN[:10]}...")
    print("✅ 正确格式示例：sk-abc123... 或 mr-xyz789...")

# 2. 构建请求头
headers = {
    "Authorization": f"Bearer {TOKEN}",  # ⚠️ 注意：必须有 "Bearer " 前缀 + 空格
    "Content-Type": "application/json"
}

print(f"🔑 测试 Token: {TOKEN[:10]}...")
print(f"📡 请求头 Authorization: {headers['Authorization'][:20]}...")

# 3. 尝试调用一个轻量接口（获取上传链接）
url = "https://mineru.net/api/v4/file-urls/batch"
payload = {
    "files": [{"name": "test.pdf"}],
    "model_version": "vlm",
    "language": "ch"
}

print(f"\n🌐 发送请求到：{url}")
try:
    resp = requests.post(url, headers=headers, json=payload, timeout=10)
    
    print(f"📊 状态码：{resp.status_code}")
    print(f"📄 响应内容：{resp.text[:300]}")
    
    # 解析响应
    try:
        data = resp.json()
        if resp.status_code == 200 and data.get("code") == 0:
            print("✅ Token 有效！认证通过")
        elif resp.status_code == 401:
            print("❌ 401 Unauthorized: Token 无效或格式错误")
            print("💡 检查：1.是否复制完整  2.是否有空格  3.是否已过期")
        elif resp.status_code == 403:
            print("⚠️  403 Forbidden: Token 有效但无权限")
            print("💡 检查：是否开通了 Precision API 权限")
        elif data.get("code") != 0:
            print(f"❌ 业务错误：{data.get('msg')}")
        else:
            print(f"❓ 未知响应：{data}")
    except json.JSONDecodeError:
        print(f"⚠️  响应不是 JSON: {resp.text[:100]}")
        
except requests.exceptions.ConnectionError:
    print("❌ 连接错误：无法访问 mineru.net，检查网络/代理")
except requests.exceptions.Timeout:
    print("❌ 请求超时：网络太慢或服务器无响应")
except Exception as e:
    print(f"❌ 未捕获异常：{type(e).__name__}: {e}")