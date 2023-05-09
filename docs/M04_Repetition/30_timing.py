import time
import math
start = time.time()

sum = 0
for num in range(1,1000000):
    sum = sum + math.sqrt(num)

end = time.time()
print('That took',end-start,'seconds.')
print('Oh, and the sum is', sum)
