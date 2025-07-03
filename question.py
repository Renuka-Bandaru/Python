#You are given a list of intervals, where each interval is represented by a pair of start and end times.
#  Your task is to merge overlapping intervals. Write a function merge_intervals(intervals)
#  that takes a list of intervals as input and returns a new list of merged intervals.
# [(1,3),(2,6),(17,20),(8,10),(15,18)] --- input
# [(1,6),(8,10),(15,20)] ----- output

def mergeInterval(intervals):
    intervals.sort()
    print(intervals)
    current_interval = intervals[0]
    print(current_interval)
    result = []
    for rem_intervals in intervals[1:]:
        if (rem_intervals[0] <= current_interval[1]):
                current_interval = (current_interval[0], max(current_interval[1], rem_intervals[1]))
                print(current_interval,"current_interval")
        else:
             result.append(current_interval)
             current_interval = rem_intervals

    result.append(current_interval)
    return result




intervals = [(1,3), (2,6),(17,20),(8,10), (15,18)]
merged_interval = mergeInterval(intervals)

print(merged_interval,"merged_intervals")