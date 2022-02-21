# Working a production problem in scipy
# The problem
""" 
A company can produce two items: A and B. 
the max tha can be produced is 3a + 4b
the factory is limited to the following constraints:
2a + 5b <= 30
4a+2b<= 20
a,b>=0
"""

# Solution.. Scipy's linprog will be our blackbox.  It will find our optimal solution.  

#Construct parameters
c_ex1 = construct = np.array([3, 4])

# Inequality constraints
A_ex1 = np.array([[2, 5],
                  [4, 2]])
b_ex1 = np.array([30,20])

# Solve the problem
# we put a negative sign on the objective as linprog does minimization
res_ex1 = linprog(-c_ex1, A_ub=A_ex1, b_ub=b_ex1, method='revised simplex')

res_ex1