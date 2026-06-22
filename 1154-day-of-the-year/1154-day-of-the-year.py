class Solution:
    def dayOfYear(self, date: str) -> int:
        # Parse the date string into year, month, and day components
        year, month, day = (int(s) for s in date.split('-'))
      
        # Determine if it's a leap year and set February days accordingly
        # Leap year conditions: divisible by 400 OR (divisible by 4 AND NOT divisible by 100)
        february_days = 29 if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) else 28
      
        # Days in each month (index 0 = January, index 1 = February, etc.)
        days_in_months = [31, february_days, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
      
        # Calculate the day of year by summing all days in previous months plus current day
        return sum(days_in_months[:month - 1]) + day
