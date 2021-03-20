ini=10000
second=0
recoverPerMin=300
comsumePerMin=600
while 1:

##    当剩下的 体力不足以跑一分钟时
    if(ini-comsumePerMin<=0):
##        换算成秒为单位
        second=second*60+ini//(comsumePerMin//60)
        break
    else:ini-=comsumePerMin
    second+=1
    ini+=recoverPerMin
    second+=1
print(second)
    
