# anonymous99782

import time
import os
import random

print("Getting data from server Higgs Domino.....")
time.sleep(3.5)
    
step = 1
connect = 0
collect = 0
extract = 0
print(f'Connecting fafafa slot server...')
while connect < 98:     
	print(f'Connect to server...{connect}%')
	step = random.randint(1, 4)
	connect += step
	time.sleep(step/5)
    
time.sleep(4)
print(f'Connect to server...100%')
time.sleep(2)
print(f'Connected!')
time.sleep(2.5)

while collect < 6545:     
	print(f'Collect slot pattern from server...{collect}kb/6548kb')
	step = random.randint(1, 300)
	collect += step
	time.sleep(step/100)

time.sleep(3)
print(f'Collect slot pattern from server...6548kb/6548kb')
time.sleep(3)

for _ in range(24):
	print(random.sample(range(100000, 999999), 6))
	time.sleep(0.2)

while extract < 16701:     
	print(f'Extract data to device...{extract}kb/16703kb')
	step = random.randint(1, 300)
	extract += step
	time.sleep(step/200)

time.sleep(0.4)
print(f'Extract data to device...16703kb/16703kb')
time.sleep(2)
print(f'Finishing procces...')
time.sleep(1.5)
print(f'Success! Open game higgs domino fafafa')
