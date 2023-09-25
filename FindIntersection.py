import sys
"""
Have the function FindIntersection(strArr) 
1. read the array of strings stored in strArr 
    which will contain 2 elements: 
    the first element will represent a list of comma-separated numbers sorted in ascending order, 
    the second element will represent a second list of comma-separated numbers (also sorted). 
Your goal is to 
2. return a comma-separated string containing the numbers that occur in elements of strArr in sorted order. 
3. If there is no intersection, return the string false.

example input:
["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]
["1, 3, 5, 7, 9", "2, 4, 6, 8, 10"]
"""

def FindIntersection(strArr):
    dict = {item.strip(): 1 for item in strArr[0].split(",")}
    dict = {item.strip(): 2 for item in strArr[1].split(",") if item.strip() in dict}
    
    result = [key for key, val in dict.items() if val == 2]
    out = ""
    for x, val in enumerate(result):
        out += str(val)
        if x < len(result) - 1:
            out += ", "
    return out if len(result) > 0 else "false"

if __name__ == "__main__":
    print(FindIntersection(sys.argv[1:]))
