from criteria import PerformanceCriteria,Opentxt


data = Opentxt("Score_Sys_1.txt")

criter = PerformanceCriteria(data=data)
criter.dispOldDET()
criter.show()