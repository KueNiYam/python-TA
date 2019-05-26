def primes(n: int) -> [int]:
    """
    에라토스테네스의 체

    : description: n까지의 소수를 반환
    """
    nums = [False, False] + [True] * (n-1)
    sqrt_nums = n ** 0.5
    for i, v in enumerate(nums):
        if i > sqrt_nums:
            break
        if v:
            nums[i*2::i] = [False] * len(nums[i*2::i])
    return [i for i, v in enumerate(nums) if v]

if __name__ == '__main__':
    print(primes(100))
    