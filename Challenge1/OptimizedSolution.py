#Solution
def Productexceptself(contributions):
    n=len(contributions)
    impact=[1]*n
    left=1
    for  i in range(n):
        impact[i]=left
        left=left*contributions[i]
    right=1
    for i in range(n-1,-1,-1):
        impact[i]=impact[i]*right
        right*=contributions[i]
    return impact
#Test
nums=[1,2,3,4]
print(Productexceptself(nums))
