# 实时数据交换接口，30004 作为 RTDE 的默认端口，被ur-rtde库内置

import rtde_receive
import rtde_control

ROBOT_IP = "192.168.1.103"  # 实际机器
# ROBOT_IP = "0.0.0.0"      # 仿真环境

def rtde_control_simple():
    try:
        # 建立连接
        rtde_r = rtde_receive.RTDEReceiveInterface(ROBOT_IP)
        rtde_c = rtde_control.RTDEControlInterface(ROBOT_IP)
        
        # 读当前位姿
        curr_pose = rtde_r.getActualTCPPose()
        print(f"当前位姿: {[round(p,4) for p in curr_pose]}")
        
        # Z轴+5cm并移动
        tgt_pose = curr_pose.copy()
        tgt_pose[2] += 0.05
        print(f"目标位姿: {[round(p,4) for p in tgt_pose]}")
        rtde_c.moveL(tgt_pose, 0.2, 0.1)
        
    except Exception as e:
        print(f"错误: {e}")
    finally:
        if 'rtde_c' in locals(): rtde_c.disconnect()
        if 'rtde_r' in locals(): rtde_r.disconnect()
        print("连接关闭")

if __name__ == "__main__":
    rtde_control_simple()
