class Solution:
    def countDaysTogether(
        self,
        arriveAlice: str,
        leaveAlice: str,
        arriveBob: str,
        leaveBob: str
    ) -> int:

        days = [31, 28, 31, 30, 31, 30,
                31, 31, 30, 31, 30, 31]

        def day_of_year(date):
            month = int(date[:2])
            day = int(date[3:])

            return sum(days[:month - 1]) + day

        a_start = day_of_year(arriveAlice)
        a_end = day_of_year(leaveAlice)

        b_start = day_of_year(arriveBob)
        b_end = day_of_year(leaveBob)

        start = max(a_start, b_start)
        end = min(a_end, b_end)

        return max(0, end - start + 1)