#_*_coding:utf-8_*_

f = open('jobData.txt', 'r')
lines = f.readlines()
for line in lines:
	print line



	ak:  F8393b5f8813fddd1310521fe110d075






function distanceFunction(myPoint, targetPointArr):
	newTargetPointArr = array()
	for(var i=0;i<targetPointArr.length;i++){
		distance = sqrt((myPoint[0]  - targetPoint[0]) ** 2 + (targetPoint[i][0] - targetPoint[i][1]) ** 2)
		if distance <= 1000:
			newTargetPointArr.append(targetPoint[i])
		else:
			pass
	return newTargetPointArr
			
