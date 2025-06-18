#Program for accepting list of salaries and give 50% hike to Every Employee
print("Enter List of Employee Salaries:")
sallist=[float(sal) for sal in input().split()]
newsallist=list(map(lambda sal: sal+sal*50/100, sallist))
print("*"*50)
print("Old Salary List\t\tNew Salary List")
print("*"*50)
for osl,nsl in zip(sallist,newsallist):
    print("\t{}\t\t{}".format(osl,nsl))
print("*"*50)

