#!/usr/bin/python3

import sys

def reverseInterval(caseList, i, j):
    while i < j:
        tmp = caseList[i]
        caseList[i] = caseList[j]
        caseList[j] = tmp
        i += 1
        j -= 1

    return caseList

def calculateCost(caseId, caseList):
    cost = 0

    for i in range(len(caseList) - 1):
        mVal = caseList[i]
        mIdx = i
        for j in range(i, len(caseList)):
            if caseList[j] < mVal:
                mVal = caseList[j]
                mIdx = j

        cost += mIdx - i + 1
        caseList = reverseInterval(caseList, i, mIdx)

    print("Case #" + str(caseId) + ":", cost)

def main():
    cases = int(input())

    for i in range(cases):
        caseLen = int(input())
        caseList = list(map(int, input().split(" ")))
        calculateCost(i + 1, caseList)

if __name__ == "__main__":
    main()
