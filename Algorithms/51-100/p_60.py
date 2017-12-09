# Permutation Sequence
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        seq = list(range(1, n + 1))
        jc = [None for _ in range(n + 1)]
        jc[1] = 1
        for index in range(2, n):
            jc[index] = jc[index - 1] * index
        permutation = []
        for i in reversed(range(1, n)):
            tmp = jc[i]
            num = k // tmp
            if k % tmp:
                k = k % tmp
            else:
                num -= 1
                k = tmp
            permutation.append(seq[num])
            del seq[num]
        permutation.append(seq[0])
        """
        permutation = list(range(1, n + 1))

        while k > 1:
            index = n - 2
            while index >= 0:
                if permutation[index] < permutation[index + 1]:
                    index2 = n - 1
                    while True:
                        if permutation[index2] > permutation[index]:
                            permutation[index], permutation[index2] = permutation[index2], permutation[index]
                            s = index + 1
                            e = n - 1
                            while s < e:
                                permutation[s], permutation[e] = permutation[e], permutation[s]
                                s += 1
                                e -= 1
                            break
                        index2 -= 1
                    break
                index -= 1
            else:
                break
            k -= 1
        """
        return ''.join(map(str, permutation))
