class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:

        def get_min_finish(start1, dur1, start2, dur2):

            min_end = min(s + d for s, d in zip(start1, dur1))

            return min(max(s, min_end) + d for s, d in zip(start2, dur2))

        land_then_water = get_min_finish(
            landStartTime, landDuration, waterStartTime, waterDuration
        )
        water_then_land = get_min_finish(
            waterStartTime, waterDuration, landStartTime, landDuration
        )

        return min(land_then_water, water_then_land)
