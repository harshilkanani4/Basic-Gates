def ANDgate():
    print("AND GATE")
    for i in range (0,4):
        a=int(input("Enter A:"))
        b=int(input("Enter B:"))
        if( a==1 and b==1):
            print(i+1,"Output is:",1)
        else:
            print(i+1,"Output is:",0)
            
def ORgate():
    print("OR GATE")
    for i in range (0,4):
        a=int(input("Enter A:"))
        b=int(input("Enter B:"))
        if( a==0 and b==0):
            print(i+1,"Output is:",0)
        else:
            print(i+1,"Output is:",1)
def NOTgate():
    print("NOT GATE")
    for i in range (0,2):
        a=int(input("Enter A:"))
        if( a==1 ):
            print(i+1,"Output is:",0)
        else:
            print(i+1,"Output is:",1)
ANDgate()
ORgate()
NOTgate()
