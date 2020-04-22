import decimal
import random
from time import sleep

while True:
	rnd_time = decimal.Decimal(random.randrange(10000))/2500
	print(str(rnd_time)+"s")
	sleep(1)