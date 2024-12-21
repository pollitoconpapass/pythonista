import torch
import torch.nn as nn


def memory_stats():
    print(torch.cuda.memory_allocated()/1024**2)
    print(torch.cuda.memory_cached()/1024**2)


def allocate():
    torch.randn(1024*1024, device='cuda')
    memory_stats()
    
    
memory_stats()
# 0.0
# 0.0

allocate()
# 4.0 # allocated inside the function
# 20.0 # used cache

memory_stats()
# 0.0 # local tensor is free
# 20.0 # cache is still alive

torch.cuda.empty_cache()
memory_stats()
# 0.0
# 0.0 # cache is free again

x = torch.randn(1024, 1024, device='cuda')
memory_stats()
# 4.0
# 20.0

# store referece
y = x

del x # this does not free the memory of x since y still points to it
memory_stats() 
# 4.0  
# 20.0

del y # this allows PyTorch to free the memory and reuse it in the cache
memory_stats()
# 0.0
# 20.0

torch.cuda.empty_cache()
memory_stats() 
# 0.0
# 0.0