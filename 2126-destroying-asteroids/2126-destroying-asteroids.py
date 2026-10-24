class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        asteroids.sort()
        for aestroid in asteroids:
            if mass>=aestroid:
                mass+=aestroid
            else:
                return False
        return True
        