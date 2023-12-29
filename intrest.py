# Take P, N, R as input from user
P = float(input('Please enter Principal in INR : '))
N = float(input('Please enter number of Years : '))
R = float(input('Please enter rate of intrest in %p.a. : '))

# Calculate simple intrest
I = P*N*R/100

# Calculate the total amount
A = P + I 

# Print above resuts
print(f'Simple Intrest : {I:.2f} INR')
print(f'Total amount is : {A:.2f} INR')