from criteria import PerformanceCriteria,Opentxt


data = Opentxt("Score_Sys_1.txt")

criter = PerformanceCriteria(data=data)
criter.displaygraphe(save=True,point=True,cp="red")
criter.show()


