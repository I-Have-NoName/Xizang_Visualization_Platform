import requests
import json

# API 相关信息
API_URL = "https://api.deepinfra.com/v1/openai/chat/completions"
API_KEY = "NfBHAuXHcNGYldPZJGjaJfNSKqXGfEgI"  # 替换为你的API密钥


# 发送消息的函数
def send_message(messages):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    data = {
        "model": "Qwen/Qwen2.5-72B-Instruct",
        "messages": messages
    }

    response = requests.post(API_URL, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()
    else:
        print(f"请求失败，状态码: {response.status_code}, 错误信息: {response.text}")
        return None


# 控制台交互
def chat():
    messages = []
    print("开始聊天吧！(输入'退出'来结束对话)")

    # 初始化系统角色
    system_message = {
        "role": "system",
        "content": "你是一个智能聊天助手。"
    }
    messages.append(system_message)

    while True:
        # 获取用户输入
        user_input = input("你: ")

        if user_input.lower() == "退出":
            print("结束对话。")
            break

        # 将用户输入添加到消息列表
        messages.append({
            "role": "user",
            "content": user_input
        })

        # 调用API并获取响应
        response_data = send_message(messages)

        if response_data:
            # 获取助理的回复
            assistant_message = response_data["choices"][0]["message"]["content"]
            print(f"助手: {assistant_message}")

            # 将助理的回复添加到消息列表
            messages.append({
                "role": "assistant",
                "content": assistant_message
            })


# 运行聊天
if __name__ == "__main__":
    chat()
