class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        def solve(n: int) -> int:
            if n <= 0:
                return 0
            
            s = str(n)
            
            @lru_cache(None)
            def dfs(pos: int, tight: bool, started: bool, prev2: int, prev1: int):
                """
                Returns:
                count = number of valid numbers that can be formed
                total = total waviness from those numbers
                """
                
                if pos == len(s):
                    if started:
                        return 1, 0
                    return 0, 0
                
                limit = int(s[pos]) if tight else 9
                
                total_count = 0
                total_waviness = 0
                
                for digit in range(limit + 1):
                    new_tight = tight and (digit == limit)
                    
                    # Case 1: still skipping leading zeroes
                    if not started and digit == 0:
                        child_count, child_waviness = dfs(
                            pos + 1,
                            new_tight,
                            False,
                            -1,
                            -1
                        )
                        
                        total_count += child_count
                        total_waviness += child_waviness
                    
                    # Case 2: we place a real digit
                    else:
                        add = 0
                        
                        # We can check whether prev1 is peak/valley
                        # only if prev2 exists.
                        if started and prev2 != -1:
                            is_peak = prev1 > prev2 and prev1 > digit
                            is_valley = prev1 < prev2 and prev1 < digit
                            
                            if is_peak or is_valley:
                                add = 1
                        
                        if not started:
                            new_prev2 = -1
                            new_prev1 = digit
                        else:
                            new_prev2 = prev1
                            new_prev1 = digit
                        
                        child_count, child_waviness = dfs(
                            pos + 1,
                            new_tight,
                            True,
                            new_prev2,
                            new_prev1
                        )
                        
                        total_count += child_count
                        total_waviness += child_waviness + add * child_count
                
                return total_count, total_waviness
            
            count, total = dfs(0, True, False, -1, -1)
            return total
        
        return solve(num2) - solve(num1 - 1)