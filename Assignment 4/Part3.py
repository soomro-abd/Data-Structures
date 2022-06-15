from Part2 import *
from Part1_A import merge_sort
from Part1_B import insertion_sort

# return list of printing job strings
def job_string_maker (printing_jobs):
    result = []

    for job in printing_jobs:
        result += [job[3][0:2] + job[3][3:] + str(job[0]) + job[1]]

    return result

# return list of sorted printing jobs
# mention the reason for choosing a particular sorting algorithm here -----?
""" 
Merge sort is O(nlogn) so it runs much faster than Selection sort which is O(n^2)
"""
def job_string_sorter (job_strings):
    return merge_sort(job_strings)

# return list of printing jobs with assigned properties
def assign_priorities (sorted_job_strings, printing_jobs):
    
    job_string = job_string_maker(printing_jobs)

    for i, job in enumerate(sorted_job_strings):
        index = job_string.index(job)
        printing_jobs[index][2] = i + 1
    
    # print(printing_jobs)
    return printing_jobs

# return list of document names in correct printing order    
def create_heap(prioritized_printing_jobs):

    result = []
    length = len(prioritized_printing_jobs)

    myHeap = minHeap(length)

    for job in prioritized_printing_jobs:
        myHeap.insert_node(job[2], job[1])
    
    for i in range(length):
        result += myHeap.extract_min().doc_title

    return result

if __name__ == '__main__':
    job_1 = [8, "D", -1, "11:30"]
    job_2 = [2, "B", -1, "19:15"]
    job_3 = [8, "A", -1, "21:50"]
    job_4 = [8, "F", -1, "09:20"]
    job_5 = [8, "M", -1, "04:20"]
    job_6 = [5, "E", -1, "09:30"]
    job_7 = [8, "C", -1, "23:59"]
    job_8 = [8, "G", -1, "00:00"]
    job_9 = [8, "H", -1, "01:30"]
    job_10 = [8, "I", -1, "11:22"]
    job_11 = [8, "D", -1, "19:27"]
    job_12 = [2, "B", -1, "21:19"]
    job_13 = [8, "A", -1, "15:18"]
    job_14 = [8, "F", -1, "17:02"]
    job_15 = [8, "M", -1, "07:20"]
    job_16 = [5, "E", -1, "19:00"]
    job_17 = [8, "C", -1, "01:14"]
    job_18 = [8, "G", -1, "21:31"]
    job_19 = [8, "H", -1, "17:22"]
    job_20 = [8, "I", -1, "16:47"]
    job_21 = [8, "M", -1, "22:30"]
    job_22 = [2, "B", -1, "21:15"]
    job_23 = [8, "A", -1, "10:00"]
    job_24 = [8, "F", -1, "21:00"]
    job_25 = [8, "M", -1, "14:50"]
    job_26 = [5, "E", -1, "16:05"]
    job_27 = [8, "C", -1, "17:55"]
    job_28 = [8, "G", -1, "12:30"]
    job_29 = [8, "H", -1, "11:40"]
    job_30 = [8, "I", -1, "09:15"]
    job_31 = [8, "M", -1, "01:15"]
    job_32 = [2, "B", -1, "01:45"]
    job_33 = [8, "A", -1, "20:05"]
    job_34 = [8, "F", -1, "18:50"]
    job_35 = [8, "M", -1, "17:40"]
    job_36 = [5, "E", -1, "16:20"]
    job_37 = [8, "C", -1, "15:30"]
    job_38 = [8, "G", -1, "17:10"]
    job_39 = [8, "H", -1, "18:40"]
    job_40 = [8, "I", -1, "19:10"]
    job_41 = [8, "M", -1, "10:25"]
    job_42 = [2, "B", -1, "22:25"]
    job_43 = [8, "A", -1, "23:25"]
    job_44 = [8, "F", -1, "23:59"]
    job_45 = [8, "M", -1, "22:53"]
    job_46 = [5, "E", -1, "16:53"]
    job_47 = [8, "C", -1, "17:43"]
    job_48 = [8, "G", -1, "13:20"]
    job_49 = [8, "H", -1, "13:40"]
    job_50 = [8, "I", -1, "14:40"]

    printing_jobs = [
        job_1, job_2, job_3, job_4, job_5, job_6, job_7, job_8, job_9, job_10,
        job_11, job_12, job_13, job_14, job_15, job_16, job_17, job_18, job_19, job_20,
        job_21, job_22, job_23, job_24, job_25, job_26, job_27, job_28, job_29, job_30,
        job_31, job_32, job_33, job_34, job_35, job_36, job_37, job_38, job_39, job_40,
        job_41, job_42, job_43, job_44, job_45, job_46, job_47, job_48, job_49, job_50
                    ]

    sorted_jobs = job_string_sorter(job_string_maker(printing_jobs))
    priority_jobs = assign_priorities(sorted_jobs, printing_jobs)

    print(create_heap(priority_jobs))