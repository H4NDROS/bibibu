import math

def f(x):
    return 37*x-math.pow(x,3)-100

def main():
    eps=1e-6
    x1=-8
    x2=-7
    ksi=(x1+x2)/2
    while(abs(f(ksi))>eps):
        if ((f(x1)>0) and (f(ksi)<0)) or ((f(x1)<0) and (f(ksi)>0)):
            x2=ksi
        elif ((f(ksi)>0) and (f(x2)<0)) or ((f(ksi)<0) and (f(x2)>0)):
            x1=ksi
        ksi=(x1+x2)/2
    return ksi

if __name__=='__main__':
    print(main())
