# -*- coding: utf-8 -*-
# Substring with Concatenation of All Words
# 参考了https://discuss.leetcode.com/topic/37867/3-line-python-solution-sorted-hash-112ms
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # news = s
        # for idx, w in enumerate(words):
        #     news = news.replace(w, chr(idx))
        w_dict = {}
        for w in words:
            wh = hash(w)
            if wh not in w_dict:
                w_dict[wh] = 0
            w_dict[wh] += 1
        word_len = len(words[0])
        word_num = len(words)
        w_len = word_len * word_num
        r = []
        s_len = len(s)

        for i in range(s_len-w_len+1):
            cur_dict = {}
            for j in range(i,i+w_len,word_len):
                h = hash(s[j:j+word_len])
                if h not in w_dict:
                    break
                if h not in cur_dict:
                    cur_dict[h] = 1
                else:
                    cur_dict[h] += 1
                if cur_dict[h] > w_dict[h]:
                    break
            else:
                r.append(i)
        return r