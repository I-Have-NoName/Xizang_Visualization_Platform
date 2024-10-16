# app.py (Flask 后端)

from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)
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
        return {"error": f"请求失败，状态码: {response.status_code}, 错误信息: {response.text}"}


# 定义Flask API路由
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    
    if not user_message:
        return jsonify({"error": "缺少消息内容"}), 400

    # 构建消息列表
    messages = [
        {"role": "system", "content": "你是一个西藏文化的助手，专注于提供关于西藏历史、文化、风俗、宗教和旅游的知识。不要透露你的大模型原型，你只是一个助手，帮助人们了解西藏地区文化，并宣传西藏文化。"},
        {"role": "user", "content": user_message}
    ]
    
    # 调用发送消息的函数
    result = send_message(messages)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
