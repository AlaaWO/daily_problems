class Solution:
    def romanToInt(self, s: str) -> int:
        output = 0
        i = 0
        while i < len(s):
            match s[i] :
                case 'C':
                    if i < len(s) -1 and s[i+1] == 'D':
                        output += 400
                        i +=2
                    elif i < len(s) -1 and s[i+1] == 'M':
                        output += 900
                        i +=2
                    else:
                        output += 100
                        i += 1
                case 'X':
                    if i < len(s) -1 and s[i+1] == 'L':
                        output += 40
                        i +=2
                    elif i < len(s) -1 and s[i+1] == 'C':
                        output += 90
                        i +=2
                    else:
                        output += 10
                        i += 1
                case 'I':
                    if i < len(s) -1 and s[i+1] == 'V':
                        output += 4
                        i +=2
                    elif i < len(s) -1 and s[i+1] == 'X':
                        output += 9
                        i +=2
                    else:
                        output += 1
                        i += 1
                case 'M':
                    output +=1000
                    i += 1
                case 'D':
                    output += 500
                    i += 1
                case 'L':
                    output += 50
                    i += 1
                case 'V':
                    output += 5
                    i += 1
        return output        