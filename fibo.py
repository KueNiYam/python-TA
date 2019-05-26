"""
피보나치 수열에 관한 모듈
"""

def fib(n: int) -> [int]:
    nums = [1, 1]
    
    for i in range(3, n):
        nums.append(nums[-1] + nums[-2])
        
    return nums