class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def date_to_day_of_year(date_str: str) -> int:
            month = int(date_str[:2])
            day = int(date_str[3:])
            # Sum days of all preceding months + current day
            return sum(days_in_months[:month - 1]) + day

        # Find overlapping start and end dates
        overlap_start = max(arriveAlice, arriveBob)
        overlap_end = min(leaveAlice, leaveBob)
        
        # If start is after end, there is no overlap
        if overlap_start > overlap_end:
            return 0
            
        start_day = date_to_day_of_year(overlap_start)
        end_day = date_to_day_of_year(overlap_end)
        
        return end_day - start_day + 1