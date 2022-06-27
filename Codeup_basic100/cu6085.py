w, h, b  = map(int,input().split())
print(format(w*h*b/8/1024/1024,'.2f'), "MB")
"""비슷 풀이
w,h,b = input().split()
res=int(w)*int(h)*int(b)/1024/1024/8
print('%.2f'%res,"MB")
"""