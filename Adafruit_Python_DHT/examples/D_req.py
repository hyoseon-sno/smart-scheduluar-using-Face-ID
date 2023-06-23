import sys
import time
import Adafruit_DHT
import sqlite3

# Parse command line parameters.
sensor_args = {'11': Adafruit_DHT.DHT11,
               '22': Adafruit_DHT.DHT22,
               '2302': Adafruit_DHT.AM2302}
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
else:
    print('Usage: sudo ./Adafruit_DHT.py [11|22|2302] <GPIO pin number>')
    print('Example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO pin #4')
    sys.exit(1)

# SQLite 데이터베이스 연결
conn = sqlite3.connect('/home/hyoseon928/project01/project01.db')
c = conn.cursor()

# sensor_data 테이블 생성 (이미 존재하는 경우 무시됨)
c.execute('''CREATE TABLE IF NOT EXISTS dsensor
             (time TEXT, humi REAL, tem REAL)''')

while True:
    # Try to grab a sensor reading. Use the read_retry method which will retry up
    # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    # Un-comment the line below to convert the temperature to Fahrenheit.
    # temperature = temperature * 9/5.0 + 32

    # Note that sometimes you won't get a reading and
    # the results will be null (because Linux can't
    # guarantee the timing of calls to read the sensor).
    # If this happens try again!
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))

        # 현재 시간과 온습도 값을 데이터베이스에 저장
        timestamp = time.strftime('%H:%M:%S')
        c.execute("INSERT INTO dsensor (time, humi, tem) VALUES (?, ?, ?)",
                  (timestamp, humidity, temperature))
        conn.commit()

    else:
        print('Failed to get reading. Try again!')

    time.sleep(3)  # Wait for 3 seconds before taking the next reading.

# 데이터베이스 연결 종료
conn.close()
