import socket
import time

# 机器人地址（IP+端口）
ROBOT_ADDR = ("192.168.1.103", 50001)  # 实际机器
# ROBOT_ADDR = ("0.0.0.0", 50001)  # 仿真环境

# 连接并测试Dashboard指令
with socket.socket() as s:
    s.connect(ROBOT_ADDR)
    s.settimeout(5)  # 超时设置
    
    # 1. 获取机器人状态
    cmd = "getStatus\n"
    s.send(cmd.encode('utf-8'))
    response = s.recv(1024).decode('utf-8').strip()
    print(f"发送: {cmd.strip()} → 响应: {response}")
    time.sleep(1)
    
    # 2. 解锁保护停止（如果机器人处于保护停止状态）
    cmd = "unlockProtectiveStop\n"
    s.send(cmd.encode('utf-8'))
    response = s.recv(1024).decode('utf-8').strip()
    print(f"发送: {cmd.strip()} → 响应: {response}")
    time.sleep(1)
    
    # 3. 启动程序（假设机器人上有默认程序"main.urp"）
    cmd = "play\n"
    s.send(cmd.encode('utf-8'))
    response = s.recv(1024).decode('utf-8').strip()
    print(f"发送: {cmd.strip()} → 响应: {response}")
    time.sleep(3)  # 等待程序运行
    
    # 4. 停止程序
    cmd = "stop\n"
    s.send(cmd.encode('utf-8'))
    response = s.recv(1024).decode('utf-8').strip()
    print(f"发送: {cmd.strip()} → 响应: {response}")
