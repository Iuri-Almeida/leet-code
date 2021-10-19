class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sym = {'I': 1,
               'V': 5,
               'X': 10,
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000
               }
        e = {'IV': 4,
             'IX': 9,
             'XL': 40,
             'XC': 90,
             'CD': 400,
             'CM': 900
             }
        c = 0
        while s:
            current = s[:2]
            verf = e if current in e.keys() else sym
            for k, v in verf.items():
                if k == (current if verf == e else current[0]):
                    c += v
                    s = s[2:] if verf == e else s[1:]
                    break
        return c
