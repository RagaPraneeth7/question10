t=int(input())          # read number of testcases
for i in range (t):     # for each i in range 0 and t
    n=int(input())      # read n as integer input
    if n<1500:          # if n is less than 1500, calculate HRA,DA as per given conditions and print overall sum
        HRA=n*0.1       
        DA=n*0.9        
        print(n+HRA+DA) 
    else:               # else calculate HRA,DA as per remaining conditions and print overall sum
        HRA=500         
        DA=n*0.98       
        print(n+HRA+DA) 
