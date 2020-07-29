# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here

census=np.concatenate((data,new_record),axis=0)
age=np.array(census[:,0])
max_age=age.max()
min_age=age.min()
age_mean=age.mean()
age_std=age.std()
race_0=np.array(census[:,2]==0)
race_1=np.array(census[:,2]==1)
race_2=np.array(census[:,2]==2)
race_3=np.array(census[:,2]==3)
race_4=np.array(census[:,2]==4)



len_1=len(race_0)
len_1=len(race_1)
len_1=len(race_2)
len_1=len(race_3)
len_1=len(race_4)


if len(race_0)<len(race_1)<len(race_2)<len(race_3)<len(race_4):
    minority_race=0
elif len(race_1)<len(race_0)<len(race_2)<len(race_3)<len(race_4):
    minority_race=1
elif len(race_2)<len(race_0)<len(race_1)<len(race_3)<len(race_4):
    minority_race=2
elif len(race_3)<len(race_0)<len(race_1)<len(race_2)<len(race_4):
    minority_race=3
elif len(race_4)<len(race_0)<len(race_1)<len(race_2)<len(race_3):
    minority_race=4


senior_citizens=census[census[:,0]>60]
working_hours_sum=sum(senior_citizens[:,6])
print(working_hours_sum)

senior_citizens_len=len(senior_citizens)
avg_working=working_hours_sum/senior_citizens_len
print(avg_working)


high=census[census[:,1]>10]
low=census[census[:,1]<=10]
avg_pay_high=np.mean(high[:,7])
print(avg_pay_high)
avg_pay_low=np.mean(low[:,7])
print(avg_pay_low)

np.array_equal(avg_pay_high,avg_pay_low)



