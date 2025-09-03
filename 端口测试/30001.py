# 读取关节角度

import socket
import time
import math

# 机器人地址（IP+端口）
ROBOT_ADDR = ("192.168.1.103", 30001)  # 实际机器人
# ROBOT_ADDR = ("0.0.0.0", 30001)  # 仿真环境

def read_joints():
    try:
        with socket.socket() as s:
            s.connect(ROBOT_ADDR)
            print("连接成功，关节角度（度）：J1  J2  J3  J4  J5  J6")
            while True:
                # 接收并解析数据
                parts = s.recv(4096).decode().strip().split(',')
                if len(parts)>=9:
                    # 提取弧度值→转换为度并打印
                    joints = [round(math.degrees(float(parts[i])),2) for i in range(3,9)]
                    print(f"\r{joints[0]}  {joints[1]}  {joints[2]}  {joints[3]}  {joints[4]}  {joints[5]}", end='')
                time.sleep(0.1)
    except ConnectionRefusedError:
        print(f"连接失败，请检查IP：{ROBOT_ADDR[0]}")
    except KeyboardInterrupt:
        print("\n程序退出")
    except Exception as e:
        print(f"错误：{e}")

if __name__ == "__main__":
    read_joints()
