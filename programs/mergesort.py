#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys


def mergesort(array):
    if len(array) <= 1:
        return array, 0
    mid = len(array) // 2

    left_list, left_inv = mergesort(array[:mid])
    right_list, right_inv = mergesort(array[mid:])
    merged_list, merge_inv = merge(left_list, right_list)

    total = left_inv + right_inv + merge_inv

    return merged_list, total


def merge(left, right):
    sorted_list = []
    i, j = 0, 0
    count_inv = 0

    left_len, right_len = len(left), len(right)

    for _ in range(left_len + right_len):
        if i < left_len and j < right_len:
            if left[i] <= right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                count_inv += left_len - i
                j += 1
        elif i == left_len:
            sorted_list.append(right[j])
            j += 1

        elif i == right_len:
            sorted_list.append(left[i])
            i += 1
    return sorted_list, count_inv


if __name__ == "__main__":
    array = input("Введите массив... ")

    if len(array) <= 1:
        print("Некорректные данные!", file=sys.stderr)
        exit(1)

    sorted_array, inversions = mergesort(array)

    print(f"Количество инверсий: {inversions}")
