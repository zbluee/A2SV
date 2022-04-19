#Question -> https://leetcode.com/problems/k-closest-points-to-origin/
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # store the distance and points on list
        point_distance = [[v[0]**2 + v[1]**2,[ v[0],v[1]]] for v in points]
        #sort the list , using their distance from the origin 
        sorted_point_distance = sorted(point_distance, key = lambda item : item[0])
        #slice the sorted list from index 0 to k
        result = [point[1] for point in sorted_point_distance[0:k]]
        
        return result
        
