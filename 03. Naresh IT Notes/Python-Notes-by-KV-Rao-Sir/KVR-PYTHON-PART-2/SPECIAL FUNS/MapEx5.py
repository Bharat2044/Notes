#Program for Computing total sal of Two List Objects
# where they Must contain Salary and Bonus
#MapEx5.py
print("Enter List of Salaries for Employees Separated by Space:")
sallst=[float(val) for val in input().split()]
print("Enter List of Bonus for Employee Separated by Space:")
bonuslist=[float(val) for val in input().split()]
#Case-1  First List Elements are More then Second list Elements and substitute 0 for remaining Elements in second list
if(len(sallst)>len(bonuslist)):
    for i in range(len(sallst)-len(bonuslist)):
        bonuslist.append(0)
elif (len(bonuslist)>len(sallst)):
    for i in range(len(bonuslist)-len(sallst)):
        sallst.append(0)
totlst=list(map(lambda sal,bonus:sal+bonus,sallst,bonuslist))
print("*"*50)
print("Emp Salary\t\tEmp Bonus\t\tTotal Salary")
print("*"*50)
for sal,bonus,tot in zip(sallst,bonuslist,totlst):
    print("\t{}\t\t\t{}\t\t\t\t{}".format(sal,bonus,tot))
print("*"*50)


