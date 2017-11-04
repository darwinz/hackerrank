"""
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00 AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

Input Format

A single string containing a time in 12-hour clock format (i.e.: hh:mm:ssAM or hh:mm:ss), where 01 <= hh <= 12 and 00 <= mm. ss <= 59

Output Format

Convert and print the given time in 24-hour format, where 00 <= hh <= 23.

Sample Input

07:05:45PM
Sample Output

19:05:45
"""

def timeConversion(s):
    time_split = s.split(":")
    if "PM" in s:
        time_split[0] = int(time_split[0]) + 12
        if int(time_split[0]) == 24:
            time_split[0] = "12"
        time_joined = ":".join(map(str, time_split))
        return time_joined.replace('PM','')
    else:
        if int(time_split[0]) == 12:
            time_split[0] = "00"
        time_joined = ":".join(map(str, time_split))
        return time_joined.replace('AM','')


s = raw_input().strip()
result = timeConversion(s)
print(result)
