# 实时数据交换接口
# 开启远程模式

import rtde_receive
import rtde_control
import time


# ROBOT_IP = "192.168.1.103"  # 实际机器
ROBOT_IP = "0.0.0.0"      # 仿真环境

def rtde_multi_move():
    rtde_r, rtde_c = None, None
    try:
        # 连机器人
        rtde_c = rtde_control.RTDEControlInterface(ROBOT_IP)
        rtde_r = rtde_receive.RTDEReceiveInterface(ROBOT_IP)
        
        # 读初始位姿
        curr_pose = rtde_r.getActualTCPPose()
        print(f"初始位姿: {[round(p,4) for p in curr_pose]}")

        # 相对偏移（x,y,z,rx,ry,rz）
        offsets = [
            [0, 0, 0.05, 0, 0, 0],        # 1. Z轴抬升5cm
            [0.15, 0, 0, 0, 0, 1.5708],   # 2. X+15cm+绕Z轴转90°
            [0, 0.1, 0, 0, 0.7854, 0],    # 3. Y+10cm+绕Y轴转45°
            [0, 0, -0.03, 0, 0, 0],       # 4. Z轴下降3cm
            [-0.15, -0.1, 0.02, 0, -0.7854, -1.5708]  # 5. 复位
        ]
        # 逐点移动
        for i, off in enumerate(offsets, 1):
            tgt = [curr_pose[j] + off[j] for j in range(6)]
            print(f"目标{i}: {[round(p,4) for p in tgt]}")
            rtde_c.moveL(tgt, 0.2, 0.1)
            time.sleep(1)
            curr_pose = tgt

        print("所有位置移动完成")

    except Exception as e:
        print(f"错误: {e}")
    finally:
        rtde_c and rtde_c.disconnect()
        rtde_r and rtde_r.disconnect()
        print("连接关闭")

if __name__ == "__main__":
    rtde_multi_move()