#using statistics module
import statistics as st
nums = [478,256,345,231,246,781]
with open("intern.txt","w")as fp:
    for i in nums:    
        fp.write(str(i)+"\n")    
with open("intern.txt","r")as fp:
    ans = fp.read().split()
for i in range(len(ans)):
    ans[i] = int(ans[i])
print("Mean using Statistics Module= ",st.mean(ans))
print("SD using Statistics Module = ",st.stdev(ans))



#using numpy
import numpy as np
nums = [478,256,345,231,246,781]
with open("intern.txt","w")as fp:
    for i in nums:       
        fp.write(str(i)+"\n")
    
with open("intern.txt","r")as fp:
    ans = fp.read().split()
for i in range(len(ans)):
    ans[i] = int(ans[i])
arr = np.array(ans)
print("Mean using Numpy = ",np.mean(arr))
print("SD using Numpy = ",np.std(arr,ddof = 1))  #ddof has a default value of 0, with ddof = 0 we can get the population standard deviation. setting ddof = 1 gives the sample standard devaition




#using pandas
import pandas as pd
import statistics as st
nums = [478,256,345,231,246,781]
with open("intern.txt","w")as fp:
    fp.write("Numbers\n")
    for i in nums:
        fp.write(str(i)+"\n")   
df = pd.read_csv('intern.txt',sep=" ")
print("Mean using Pandas = ",df["Numbers"].mean())
print("SD using Pandas = ",df["Numbers"].std())




