#some prime numbers
#2	3	5	7	11	13	17	19	23	29
#31	37	41	43	47	53	59	61	67	71
#73	79	83	89	97	101	103	107	109	113
#127	131	137	139	149	151	157	163	167	173
#179	181	191	193	197	199	211	223	227	229
#233	239	241	251	257	263	269	271	277	281
#283	293	307	311	313	317	331	337	347	349
#353	359	367	373	379	383	389	397	401	409
#419	421	431	433	439	443	449	457	461	463
#467	479	487	491	499	503	509	521	523	541
#547	557	563	569	571	577	587	593	599	601
#607	613	617	619	631	641	643	647	653	659
#661	673	677	683	691	701	709	719	727	733
#739	743	751	757	761	769	773	787	797	809
#811	821	823	827	829	839	853	857	859	863
#877	881	883	887	907	911	919	929	937	941
#947	953	967	971	977	983	991	997	1009	1013
#1019	1021	1031	1033	1039	1049	1051	1061	1063	1069
#1087	1091	1093	1097	1103	1109	1117	1123	1129	1151
#1153	1163	1171	1181	1187	1193	1201	1213	1217	1223


import time
start_time = time.time()

from decimal import Decimal
#Euclid's algorithm for determining the greatest common divisor
def gcd(a,b):
	if b==0:
		return a
	else:
		return gcd(b,a%b)

from PrimeNumGenerator import prime1, prime2
p = prime1
q = prime2
#p = int(input('Enter the value of p = '))
#q = int(input('Enter the value of q = '))
no = int(input('Enter the value of text = '))
n = p*q
t = (p-1)*(q-1)

for e in range(2,t):
	if gcd(e,t)== 1:
		break

#chooses d (d = (1 + (k*phi))/e)    k = i
for i in range(1,10):
	x = 1 + i*t
	if x % e == 0:
		d = int(x/e)
		break
ctt = Decimal(0)
ctt =pow(no,e)
ct = ctt % n

dtt = Decimal(0)
dtt = pow(ct,d)
dt = dtt % n

print('n = '+str(n)+' e = '+str(e)+' t = '+str(t)+' d = '+str(d)+' cipher text = '+str(ct)+' decrypted text = '+str(dt))
#print(i)



print("--- %s seconds ---" % (time.time() - start_time))