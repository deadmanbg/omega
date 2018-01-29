import onionGpio as og
import time

pin0 = og.OnionGpio(0)
pin1 = og.OnionGpio(1)

pin0.setOutputDirection(1)
pin1.setInputDirection()

for i in range(100):
  print(pin1.getValue())
  time.sleep(0.5)

 


