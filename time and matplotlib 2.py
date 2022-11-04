import matplotlib.pyplot as plt
import time as t

times = []

print("This program will help you type faster. You will have to type a word as fast as you can far five times")
input("Press enter to continue")

while len(times)<5:
      start = t.time()
      word = input ("Type the word:")
      end = t.time()
      time_elapsed = end - start

      times.append (time_elapsed)

print("Now let's see your evaluation")
t.sleep(4)

x = [1,2,3,4,5]
y = times
plt.plot(x,y)
scheme = ["1","2","3","4","5"]
plt.xticks(x, scheme)
plt.xlabel("Attempts")
plt.ylabel("Time in seconds")
plt.title('This graph show your typing frequency')
plt.show()
