import socket
import time

# 机器人地址（IP+50001端口）
# ROBOT_ADDR = ("192.168.1.103", 50001)  # 必须替换为实际IP
ROBOT_ADDR = ("0.0.0.0", 50001)  # 仿真环境（需确认仿真器开启Dashboard）

def test_dashboard():
    with socket.socket() as s:
        try:
            s.connect(ROBOT_ADDR)
            s.settimeout(10)  # 延长超时时间，适配机器人响应速度
            print(f"已连接到 {ROBOT_ADDR}")
            
            # 1. 发送"ping"指令（Dashboard必支持，测试连通性）
            cmd = "ping\n"
            s.send(cmd.encode('utf-8'))
            # 修复解码：忽略无效字符
            response = s.recv(1024).decode('utf-8', errors="ignore").strip()
            print(f"发送: {cmd.strip()} → 响应: {response}")
            time.sleep(2)
            
            # 2. 获取机器人状态（避免复杂指令，先验证基础功能）
            cmd = "getStatus\n"
            s.send(cmd.encode('utf-8'))
            response = s.recv(1024).decode('utf-8', errors="ignore").strip()
            print(f"发送: {cmd.strip()} → 响应: {response}")
            
        except ConnectionRefusedError:
            print(f"连接失败！请检查：1. 机器人IP是否正确 2. 50001端口是否开放")
        except TimeoutError:
            print("超时！请确认：1. 机器人Dashboard服务已启动 2. 网络无延迟")
        except Exception as e:
            print(f"错误：{e}")
        finally:
            print("连接关闭")

if __name__ == "__main__":
    test_dashboard()