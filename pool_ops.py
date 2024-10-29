# pool_ops.py
#
# Usage: Determine the output shape and operation count of an average pooling layer.
# Parameters:
# c_in: input channel count
# h_in: input height count
# w_in: input width count
# h_pool: average pooling kernel height count
# w_pool: average pooling kernel width count
# s: stride of average pooling kernel
# p: amount of padding on each of the four input map sides
# Output:
#  output channel count, output height count, output width count, number of additions, multiplications and divisions performed
#
# Written by Tejas Vinod
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.
#
# Test Inputs:
# python3 
# Expected Answer
# 


# import Python modules
import math # math module
import sys # argv

# "constants"
# none

# helper functions
# none

# initialize script arguments
c_in = float('nan') # input channel count
h_in = float('nan') # input height count
w_in = float('nan') # input width count
h_pool = float('nan') # average pooling kernel height count
w_pool = float('nan') # average pooling kernel width count
s = float('nan') # stride of average pooling kernel
p = float('nan') # amount of padding on each of the four input map sides

# parse script arguments
if len(sys.argv)==8:
    c_in = float(sys.argv[1]) # input channel count
    h_in = float(sys.argv[2]) # input height count
    w_in = float(sys.argv[3]) # input width count
    h_pool = float(sys.argv[4]) # average pooling kernel height count
    w_pool = float(sys.argv[5]) # average pooling kernel width count
    s = float(sys.argv[6]) # stride of average pooling kernel
    p = float(sys.argv[7]) # amount of padding on each of the four input map sides
else:
  print(\
   'Usage: '\
   'python3 pool_ops.py c_in h_in w_in h_pool w_pool s p'\
  )
  exit()

c_out = c_in
h_out = math.floor((h_in+2.0*p-h_pool)/s + 1)
w_out = math.floor((w_in+2.0*p-w_pool)/s + 1)
adds = c_in * h_out * w_out * (h_pool*w_pool - 1)
muls = 0 
divs = c_in * h_out * w_out

print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed