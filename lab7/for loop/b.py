def double_power(a, n):
    if n==0:
        return 1
    else:
        return a*pow(a,n-1)
print(double_power(int(input()), int(input())))