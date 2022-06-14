class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        mergedIntervals = []
        
        intervals.sort(key=lambda a: a[0])
        
        for interval in intervals:
            
            if not mergedIntervals:
                mergedIntervals.append(interval)
                            
            elif (mergedIntervals[-1][0] <= interval[0] <= mergedIntervals[-1][1]):
                mergedIntervals[-1][1] = max(mergedIntervals[-1][1], interval[1]) 
            
            else:
                mergedIntervals.append(interval)
                
        return mergedIntervals
                             

