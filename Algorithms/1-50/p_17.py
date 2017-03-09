# Letter Combinations of a Phone Number
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        self.c_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        r = []
        d_len = len(digits)

        def search(i, cur_str):
            if i == d_len - 1:
                for l in self.c_dict[digits[i]]:
                    r.append(cur_str+l)
            else:
                for l in self.c_dict[digits[i]]:
                    search(i+1, cur_str+l)

        search(0, "")
        return r