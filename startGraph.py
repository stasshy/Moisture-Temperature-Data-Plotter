import time
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(i, moistureList, tempList, ser):
    ser.write(b'g')
    data_string = ser.readline().decode('ascii')
    try:
        tmpList = data_string.split(",")
        moistureData_float = float(tmpList[0])
        tempData_float = float(tmpList[1])
        moistureList.append(moistureData_float)
        tempList.append(tempData_float)
    except:
        pass
    moistureList[:] = moistureList[-50:]
    tempList[:] = tempList[-50:]
    ax.clear()
    ax.plot(moistureList)
    ax2.clear()
    ax2.plot(tempList, 'r')
    ax.set_ylim([0, 100])
    ax2.set_ylim([1, 45])
    ax.set_title("Moisture and Temperature data")
    ax.set_ylabel("Moisture", color="blue", fontsize=14)
    ax2.set_ylabel("Temperature", color="red", fontsize=14)

moistureList = []
tempList = []

fig = plt.figure()
ax = fig.add_subplot(111)
ax2 = ax.twinx()

ser = serial.Serial("COM6", 9600)  # Change as needed
time.sleep(2)

ani = animation.FuncAnimation(fig, animate, frames=30, fargs=(moistureList, tempList, ser), interval=100)
plt.show()
ser.close()
