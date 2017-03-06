# Median of Two Sorted Arrays
class Solution(object):
    def find_num(self, l, l_s, l_e, num):
        if l_s >= l_e:
            return l_s
        if l_e == l_s + 1:
            if l[l_s] == num:
                return l_s
            if l[l_e] <= num:
                return l_e
            return l_s
        mid = (l_s + l_e)/2
        if l[mid] <= num:
            return self.find_num(l, mid, l_e, num)
        elif l[mid] > num:
            return self.find_num(l, l_s, mid-1, num)

    def find_index(self, l1, l2, l1_s, l1_e, l2_s, l2_e, th):
        # print l1, l2, l1_s, l1_e, l2_s, l2_e, th
        l1_len = l1_e - l1_s + 1
        l2_len = l2_e - l2_s + 1
        if l1_len == 1 and l2_len == 1:
            if th == 1:
                if l1[l1_s] <= l2[l2_s]:
                    return l1, l1_s, l2, l2_s, True
                else:
                    return l2, l2_s, l1, l1_s, True
            else:
                if l1[l1_s] >= l2[l2_s]:
                    return l1, l1_s, l2, l2_s, False
                else:
                    return l2, l2_s, l1, l1_s, False
        if l1_len >= l2_len:
            mid = (l1_s + l1_e) / 2
            mid_num = l1[mid]
            if l2[l2_s] >= mid_num:
                front_num = mid - l1_s + 1
                if front_num >= th:
                    return l1, l1_s + th - 1, l2, l2_s, True
                else:
                    return self.find_index(l1, l2, mid + 1 if mid < l1_e else mid, l1_e,
                                           l2_s, l2_e, th - front_num)
            else:
                mid2 = self.find_num(l2, l2_s, l2_e, mid_num)
                front_num = (mid-l1_s+1) + (mid2-l2_s+1)
                if front_num == th:
                    return l1, mid, l2, mid2, False
                elif front_num < th:
                    th_new = th-front_num
                    if mid < l1_e:
                        l1_ss = mid + 1
                    else:
                        l1_ss = mid
                        th_new += 1
                    if mid2 < l2_e:
                        l2_ss = mid2 + 1
                    else:
                        l2_ss = mid2
                        th_new += 1
                    return self.find_index(l1, l2, l1_ss, l1_e, l2_ss, l2_e, th_new)
                else:
                    return self.find_index(l1, l2, l1_s, mid-1 if mid>l1_s else mid, l2_s, mid2, th)
        else:
            mid = (l2_s + l2_e) / 2
            mid_num = l2[mid]
            if l1[l1_s] >= mid_num:
                front_num = mid - l2_s + 1
                if front_num >= th:
                    return l2, l2_s + th - 1, l1, l1_s, True
                else:
                    return self.find_index(l1, l2, l1_s, l1_e, mid + 1 if mid < l2_e else mid, l2_e,
                                           th - front_num)
            else:
                mid2 = self.find_num(l1, l1_s, l1_e, mid_num)
                front_num = (mid - l2_s + 1) + (mid2 - l1_s + 1)
                if front_num == th:
                    return l2, mid, l1, mid2, False
                elif front_num < th:
                    th_new = th - front_num
                    if mid < l2_e:
                        l2_ss = mid + 1
                    else:
                        l2_ss = mid
                        th_new += 1
                    if mid2 < l1_e:
                        l1_ss = mid2 + 1
                    else:
                        l1_ss = mid2
                        th_new += 1
                    return self.find_index(l1, l2, l1_ss, l1_e, l2_ss, l2_e, th_new)
                else:
                    return self.find_index(l1, l2, l1_s, mid2, l2_s, mid-1 if mid>l2_s else mid, th)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        if nums1_len == 0:
            if nums2_len % 2 == 0:
                mid = nums2_len / 2 - 1
                return (nums2[mid] + nums2[mid+1])/2.0
            else:
                return nums2[nums2_len/2]
        if nums1_len == 1:
            if nums2_len % 2 == 0:
                mid = nums2_len / 2 - 1
                if nums2[mid] >= nums1[0]:
                    return nums2[mid]
                elif nums2[mid+1] <= nums1[0]:
                    return nums2[mid+1]
                else:
                    return nums1[0]
            else:
                mid = nums2_len / 2
                if nums1[0] <= nums2[mid]:
                    if mid > 0:
                        if nums2[mid-1] <= nums1[0]:
                            return (nums2[mid]+nums1[0])/2.0
                        else:
                            return (nums2[mid]+nums2[mid-1])/2.0
                    else:
                        return (nums2[mid]+nums1[0])/2.0
                else:
                    if mid+1 < nums2_len:
                        if nums2[mid+1] >= nums1[0]:
                            return (nums2[mid]+nums1[0])/2.0
                        else:
                            return (nums2[mid]+nums2[mid+1])/2.0
                    else:
                        return (nums2[mid]+nums1[0])/2.0
        nums_len = nums1_len + nums2_len
        l1, idx1, l2, idx2, is_abs = self.find_index(nums1, nums2, 0, nums1_len-1, 0, nums2_len-1, nums_len/2 if nums_len%2 == 0 else (nums_len/2 + 1))
        # print l1, idx1, l2, idx2, is_abs
        if is_abs:
            if nums_len%2 == 0:
                if idx1 < len(l1) - 1:
                    n1 = l1[idx1+1]
                    if n1 <= l2[idx2]:
                        return (n1+l1[idx1])/2.0
                    else:
                        return (l2[idx2] + l1[idx1]) / 2.0
                else:
                    return (l2[idx2] + l1[idx1]) / 2.0
            else:
                return l1[idx1]
        if l2[idx2] > l1[idx1]:
            l1, idx1, l2, idx2 = l2, idx2, l1, idx1
        if nums_len%2 == 0:
            n1 = None
            if idx1 < len(l1) - 1:
                n1 = l1[idx1+1]
            n2 = None
            if idx2 < len(l2) - 1:
                n2 = l2[idx2+1]
            if n1 is None and n2 is None:
                return (l1[idx1] + l2[idx2])/2.0
            if n1 is None:
                return (l1[idx1]+n2)/2.0
            elif n2 is None:
                return (l1[idx1]+n1)/2.0
            elif n1 < n2:
                return (l1[idx1] + n1) / 2.0
            else:
                return (l1[idx1]+n2)/2.0
        else:
            return l1[idx1]

