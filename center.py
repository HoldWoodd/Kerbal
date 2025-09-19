import krpc
import time
import ctrl
import keyboard

conn = krpc.connect(name='Hello World') # 连接服务器
vessel = conn.space_center.active_vessel # 获取当前载具
print(vessel.name) # 打印载具名

flight = vessel.flight()
verti = ""

deg = 1.5
while True:
    if keyboard.is_pressed("shift"):
            deg += 0.1
            #ctrl.up(vessel)
    elif keyboard.is_pressed("ctrl"):
            deg -= 0.1
            #ctrl.down(vessel)



    if keyboard.is_pressed("w"):
        if keyboard.is_pressed("space"):
            ctrl.forward_20(vessel, flight, deg)
        else:
            ctrl.forward_10(vessel, flight, deg)
    elif keyboard.is_pressed("s"):
        if keyboard.is_pressed("space"):
            ctrl.backward_20(vessel, flight, deg)
        else:
            ctrl.backward_10(vessel, flight, deg)
    else:
        ctrl.stop(vessel, flight, deg)

    if keyboard.is_pressed("esc"):
        print("退出程序")
        break
    time.sleep(0.02)