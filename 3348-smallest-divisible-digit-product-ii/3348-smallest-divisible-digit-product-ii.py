class Solution:
    def smallestNumber(self, num: str, t: int) -> str:

        # prime factor contribution of every digit
        # order -> (2, 3, 5, 7)
        factors = [
            (0, 0, 0, 0),  # 0 - can't use
            (0, 0, 0, 0),  # 1
            (1, 0, 0, 0),  # 2
            (0, 1, 0, 0),  # 3
            (2, 0, 0, 0),  # 4
            (0, 0, 1, 0),  # 5
            (1, 1, 0, 0),  # 6
            (0, 0, 0, 1),  # 7
            (3, 0, 0, 0),  # 8
            (0, 2, 0, 0),  # 9
        ]

        # break t into powers of 2, 3, 5 and 7
        required = []

        for prime in (2, 3, 5, 7):
            count = 0

            while t % prime == 0:
                t //= prime
                count += 1

            required.append(count)

        # digits 1-9 can't create any prime other than 2,3,5,7
        if t != 1:
            return "-1"

        required = tuple(required)

        @lru_cache(None)
        def min_digits(a, b, c, d):
            """
            Minimum number of digits needed to get
            at least a twos, b threes, c fives and d sevens.
            """

            ans = float("inf")

            # digit 6 gives us one 2 and one 3 together
            # try using different numbers of 6s
            for sixes in range(min(a, b) + 1):

                twos_left = a - sixes
                threes_left = b - sixes

                # 8 = 2^3, so it is the best digit for covering 2s
                digits_for_twos = (twos_left + 2) // 3

                # 9 = 3^2, so it is the best digit for covering 3s
                digits_for_threes = (threes_left + 1) // 2

                # 5 and 7 need their own digits
                total = (
                    sixes
                    + digits_for_twos
                    + digits_for_threes
                    + c
                    + d
                )

                ans = min(ans, total)

            return ans

        def build_suffix(need, length):
            """
            Build the smallest possible suffix of given length
            that can still satisfy all remaining prime factors.
            """

            # not enough places left
            if min_digits(*need) > length:
                return None

            suffix = []

            for pos in range(length):

                places_left = length - pos - 1

                # always try smaller digits first
                for digit in range(1, 10):

                    contribution = factors[digit]

                    # remove whatever this digit gives us
                    next_need = tuple(
                        max(0, need[i] - contribution[i])
                        for i in range(4)
                    )

                    # choose this digit only if the remaining
                    # requirement can still fit afterwards
                    if min_digits(*next_need) <= places_left:
                        suffix.append(str(digit))
                        need = next_need
                        break

            return "".join(suffix)

        n = len(num)

        # prefix[i] tells us how many 2s,3s,5s,7s
        # are contributed by num[0:i]
        prefix = [(0, 0, 0, 0)]

        # also remember whether the prefix contains a zero
        prefix_valid = [True]

        current = [0, 0, 0, 0]
        valid = True

        for ch in num:

            digit = int(ch)

            if digit == 0:
                valid = False

            else:
                contribution = factors[digit]

                for j in range(4):
                    current[j] += contribution[j]

            prefix.append(tuple(current))
            prefix_valid.append(valid)

        # first check whether num itself already works
        if prefix_valid[n]:

            works = all(
                prefix[n][i] >= required[i]
                for i in range(4)
            )

            if works:
                return num

        # try changing the number from the right side first
        # changing a later digit gives us a smaller answer
        for i in range(n - 1, -1, -1):

            # everything before i stays unchanged,
            # so that prefix cannot contain zero
            if not prefix_valid[i]:
                continue

            current_digit = int(num[i])
            suffix_length = n - i - 1

            # this must be the first position where answer > num
            # so the new digit has to be larger
            for new_digit in range(current_digit + 1, 10):

                contribution = factors[new_digit]

                # see what prime factors are still missing
                remaining = tuple(
                    max(
                        0,
                        required[j]
                        - prefix[i][j]
                        - contribution[j]
                    )
                    for j in range(4)
                )

                # if the remaining positions are enough,
                # we found the smallest possible answer
                if min_digits(*remaining) <= suffix_length:

                    suffix = build_suffix(
                        remaining,
                        suffix_length
                    )

                    return (
                        num[:i]
                        + str(new_digit)
                        + suffix
                    )

        # no number of the same length worked
        # any longer number is automatically greater than num
        length = max(
            n + 1,
            min_digits(*required)
        )

        return build_suffix(required, length)