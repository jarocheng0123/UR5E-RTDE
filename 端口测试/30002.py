# 控制IO

import socket
import time

# 机器人地址（IP+端口）
# ROBOT_ADDR = ("192.168.1.103", 30002)  # 实际机器
ROBOT_ADDR = ("0.0.0.0", 30002)  # 仿真环境

# 目标DO端口
DO_PORT = 4

# 连接并控制
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(ROBOT_ADDR)
    
    # 设置高电平
    s.send(f"set_digital_out({DO_PORT}, True)\n".encode('utf-8'))
    print(f"DO{DO_PORT} 已设为高电平")
    time.sleep(5)
    
    # 设置低电平
    s.send(f"set_digital_out({DO_PORT}, False)\n".encode('utf-8'))
    print(f"DO{DO_PORT} 已设为低电平")
    time.sleep(5)