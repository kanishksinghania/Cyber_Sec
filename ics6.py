def check_prime(a):
    if a < 1:
        return -1
    elif a > 1:
        if a == 2:
            return 1
        for i in range(2, a):
            if a % i == 0:
                return -1
            return 1
        
def check_primitive(b,a,l): 
     for i in range(1, a):
        l.append(pow(b, i) % a)
     for i in range(1, a):
        if l.count(i) > 1:
            l.clear()
            return -1
        return 1

cl=[] #cl =checklist
def main():
    n = int(input("Enter the value of n: "))
    if check_prime(n) == -1:
        print("Number Is Not Prime")
    else:
        g = int(input("Enter the primitive root of n: "))
        if check_primitive(g,n,cl) == -1:
            print("Number Is Not A Primitive Root Of n!")
        else:
            k1 = int(input("Enter the key for Kanishk: "))
            k2 = int(input("Enter the key for Simone: "))
            if k1 >= n or k2>= n:
                print("Private key for both users should be less than n!")
            else:
                x1 = pow(g,k1) % n
                x2 = pow(g,k2) % n 
                y1 = pow(x2,k1) % n
                y2 = pow(x1,k2) % n
                if y1 == y2:
                    print("Keys exchanged successfully!")
                    print("And the value of key generated is:",y1)
                else:
                    print("Keys were not able to exchange")
                       
main()