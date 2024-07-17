def cc_en(text,n):
    ct=""
    for i in range(len(text)):
        ch = text[i]
        if (ch==" "):
            ct = ct + " "
        elif (ch.isupper()):
            ct = ct + chr((ord(ch)+n-65)%26+65)
        else :
            ct = ct + chr((ord(ch)+n-97)%26+97)
    print(ct)

def cc_dp(text,n):
    ct=""
    for i in range(len(text)):
        ch = text[i]
        if (ch==" "):
            ct = ct + " "
        elif (ch.isupper()):
            ct = ct + chr((ord(ch)-n-65)%26+65)
        else :
            ct = ct + chr((ord(ch)-n-97)%26+97)
    print(ct)

def main():
    pt = str(input("Enter the plaintext: "))
    key = int(input("Enter the key: "))
    print("What do you want to perform in Caesar Cipher: ")
    x = int(input("1)Encryption\n2)Decryption\n"))
    match(x):
        case(1):
            print("The Cipher text is: ")
            cc_en(pt,key)
        case(2):
            print("The Cipher text is: ")
            cc_dp(pt,key)
main()