from itertools import zip_longest
from math import pow

#convert IP address to binary
def ipcn(ipadd):
    ip = ipadd.split(".")
    #print(ip)
    ipbit = ".".join(map(str, ["{0:08b}".format(int(x)) for x in ip]))
    #print(ipbit)
    ipb = ipbit.split(".")
    #print(ipb)
    return ipb


#convert mask to binary
def snm(sm):
    #print(sm)
    t = ['0'] * 32
    t1 = []
    for i in range(0, sm):
      t[i] = '1'
    for i in range(0, 25, 8):
      t1.append("".join(t[i:i + 8]))
    #print(t1)
    return t1


#Geting Host IP Address in binary form
def hip(t1,ipb):
    t2 = []
    t4=[]
    for i in range(4):
        p=t1[i]
        q=ipb[i]
        t3 = ""
        for j in range(8):
             if(p[j]=='1' and q[j]=='1'):
                 t3+='1'
             else:
                t3+='0'
             t4.append("".join(t3[j:j + 8]))
        t2.append(t3)
    #print(t2)   #Host binary list
    #print(t4)   #host bits list
    return (t2,t4)


#checking whether given number is power of 2 or not
def powOf2(n):
    if(n==0):
        return False
    i=0
    a=n
    while (n!=1):
        if(n%2==0):
            n = n // 2
            i = i + 1
        else:
            return False
    return i


def getbits(sm, n, x, t4):
    l1 = t4[0:sm]
    #print(l1)  # host bits list of size mask
    l2 = []
    for i in range(0,n):
        l2.append(l1)
    #print(l2)
    l3 = []
    l5 = []
    for i in range(0, n):
        z='{:0'+str(x)+'b}'
        l4 = z.format(i)
        l3.append(l4)

    #print(l3)
    for i in range(n):
        l6 = []
        for j in range(x):
            l6.append(l3[i][j])
        l5.append(l6)
    #print(l5)
    return (l2,l5)




#Network id, broadCast id, Min,Max Network id in Binary
def getBinaryid(l2, size):
    l00 = []
    l11 = []
    l01 = []
    l10 = []
    for i in range(len(l2)):
        t = []
        for j in range(size):
            t.append('0')
        t = l2[i] + t
        l00.append(t)

        t = []
        for j in range(size):
            t.append('1')
        t = l2[i] + t
        l11.append(t)

        t = []
        for j in range(size - 1):
            t.append('0')
        t = l2[i] + t + ['1']
        l01.append(t)

        t = []
        for j in range(size - 1):
            t.append('1')
        t = l2[i] + t + ['0']
        l10.append(t)

    return(l00,l11,l01,l10)



#Network id, broadCast id, Min,Max Network id in Decimal
def getDecimalid(l00,l11,l01,l10):
    nid = []
    for j in l00:
        it = iter(map(str, j))
        res = [int("".join(i), 2) for i in zip_longest(*iter([it] * 8), fillvalue="")]
        nid.append(res)
    #print("\nNetwork Id\n", nid)

    bid = []
    for j in l11:
        it = iter(map(str, j))
        res = [int("".join(i), 2) for i in zip_longest(*iter([it] * 8), fillvalue="")]
        bid.append(res)
    #print("\nBroadcast Id\n", bid)

    minid = []
    for j in l01:
        it = iter(map(str, j))
        res = [int("".join(i), 2) for i in zip_longest(*iter([it] * 8), fillvalue="")]
        minid.append(res)
    #print("\nMin Network Id\n", minid)

    maxid = []
    for j in l10:
        it = iter(map(str, j))
        res = [int("".join(i), 2) for i in zip_longest(*iter([it] * 8), fillvalue="")]
        maxid.append(res)
    #print("\nMax Network Id\n", maxid)

    return(nid, bid, minid, maxid)




#Network id, broadCast id, Min,Max Network id in IP Address Format
def getIpAddrid(nid, bid, minid, maxid):
    ipnid = []
    #print("\nNetwork id \n")
    for i in range(len(nid)):
        temp = '.'.join(str(j) for j in nid[i])
        ipnid.append(temp)
    #print(ipnid)

    ipbid = []
    #print("\n Broad Cast id \n")
    for i in range(len(bid)):
        temp = '.'.join(str(j) for j in bid[i])
        ipbid.append(temp)
    #print(ipbid)

    ipminid = []
    #print("\nMinimum Network id \n")
    for i in range(len(minid)):
        temp = '.'.join(str(j) for j in minid[i])
        ipminid.append(temp)
    #print(ipminid)

    ipmaxid = []
    #print("\nMaximum Network id \n")
    for i in range(len(maxid)):
        temp = '.'.join(str(j) for j in maxid[i])
        ipmaxid.append(temp)
    #print(ipmaxid)

    return(ipnid, ipbid, ipminid, ipmaxid)



#Calling Functions

ipadd = input("Enter IP Address : \n")
ipb = ipcn(ipadd)
sm = int(input("Enter Subnet mask : \n"))
t1 = snm(sm)
t2, t4 = hip(t1, ipb)
n = int(input("Enter Number of subnets : \n"))
x = powOf2(n)
l2, l5 = getbits(sm, n, x, t4)

for i in range(len(l2)):
    l2[i] = l2[i] + l5[i]
#print("\n", l2)

size = 32 - (sm + x)


l00,l11,l01,l10 = getBinaryid(l2, size)
nid, bid, minid, maxid = getDecimalid(l00, l11, l01, l10)
ipnid, ipbid, ipminid, ipmaxid = getIpAddrid(nid, bid, minid, maxid)

for i in range(len(ipnid)):
    print("\nNetwork No:", i+1)
    print("\tNetwork Id: ", ipnid[i])
    print("\tBroadCast Id: ", ipbid[i])
    print("\tMinimum Network Id: ", ipminid[i])
    print("\tMaximum Network Id: ", ipmaxid[i])
    print("\tAvailable Networks: ", int(pow(2, size)-2))