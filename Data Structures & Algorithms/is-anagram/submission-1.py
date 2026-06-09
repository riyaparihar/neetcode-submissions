class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        

        # method 1
       # tc: nlogn+nlogn = nlogn
       # sc: n+n= 2n = n

       # sort temp space(timsort) => n
        # s_list = list(s)
        # s_list.sort()

        # t_list = list(t)
        # t_list.sort()

        # return s_list == t_list


        # method 2
        #tc: n+n+n= n
        # sc: 26 => 1 o constant space(lowercase English letters.)
        count= {}
        for i in range(len(s)):
            count[s[i]]= count.get(s[i], 0) + 1
            count[t[i]] = count.get(t[i], 0) -1

        for v in count.values():
            if v != 0:
                return False
        return True



