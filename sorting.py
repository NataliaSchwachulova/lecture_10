import csv
import os


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row_ind, row in enumerate(reader):
            if row_ind == 0:
                output = dict()
                for key in row:
                    output[key] = []
            for key in row:
                output[key].append(int(row[key]))
    return output


def selection_sort(list_of_nums, direction):
    for idx_start in range(0, len(list_of_nums)):
        idx_switch = idx_start
        for idx_searched in range(idx_start+1, len(list_of_nums)):
            if direction == "ascending":
                if list_of_nums[idx_searched] <= list_of_nums[idx_switch]:
                    idx_switch = idx_searched
            if direction == "descending":
                if list_of_nums[idx_searched] >= list_of_nums[idx_switch]:
                    idx_switch = idx_searched
        list_of_nums[idx_start], list_of_nums[idx_switch] = list_of_nums[idx_switch], list_of_nums[idx_start]
    return list_of_nums


def bubble_sort(list_of_nums):
    idx_end = len(list_of_nums)-1
    while idx_end != 0:
        for idx_search in range(0, idx_end):
            if list_of_nums[idx_search] > list_of_nums[idx_search+1]:
                list_of_nums[idx_search], list_of_nums[idx_search+1] = list_of_nums[idx_search+1], list_of_nums[idx_search]
        idx_end -= 1
    return list_of_nums


def insertion_sort(list_of_nums):
    idx_start = 0
    while idx_start != len(list_of_nums):
        for idx_search in range(idx_start+1, len(list_of_nums)):
            if list_of_nums[idx_search] < list_of_nums[idx_start]:
                list_of_nums[idx_search], list_of_nums[idx_search + 1] = list_of_nums[idx_search + 1], list_of_nums[
                    idx_search]
        idx_start += 1
    return list_of_nums


def main():
    nums = (read_data("numbers.csv"))
    list_of_nums = nums["series_1"]
    print(list_of_nums)
    print(selection_sort(list_of_nums, "descending"))
    print(bubble_sort(list_of_nums))
    print(insertion_sort(list_of_nums))


if __name__ == '__main__':
    main()
