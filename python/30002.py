# UR机器人DO端口控制程序
# 功能：通过30002端口循环控制指定DO端口的高低电平
# 注意：无需额外配置环境，开启UR机器人电源后即可运行

import socket
import time

# ROBOT_ADDR = ("192.168.1.103", 30002)  # 实际机器
ROBOT_ADDR = ("127.0.0.1", 30002)  # 仿真环境

# 目标DO端口
DO_PORT = 4

# 连接并控制
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(ROBOT_ADDR)
    # 循环切换高低电平
    for i in range(5):
        print(f"\n第{i+1}次循环：")
        # 设置高电平
        s.send(f"set_digital_out({DO_PORT}, True)\n".encode('utf-8'))
        print(f"DO{DO_PORT} 已设为高电平")
        time.sleep(2)
        
        # 设置低电平
        s.send(f"set_digital_out({DO_PORT}, False)\n".encode('utf-8'))
        print(f"DO{DO_PORT} 已设为低电平")
        time.sleep(2)
    print("\n循环完成")