# climbing stairs

# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


def climbingStairs(n):

    def climb(k):

        if k == 0:
            return 1
        if k < 0:
            return 0
        if k > 0: 
            return climb(k-1) + climb(k-2)

    return climb(n-1) + climb(n-2)

print( climbingStairs(5) )