import sys
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
if A>=3 and B<=4:
    print("TroyMartian")
if A<=6 and B>=2:
    print("VladSaturnian")
if A<=2 and B<=3:
    print("GraemeMercurian")