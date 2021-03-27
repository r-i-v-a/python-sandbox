#!/usr/bin/python3

import sys

def calculateCost(caseId, caseList):
    print("--> Case id", caseId)
    for x in caseList:
        print(x)

def main():
    cases = int(input())

    for i in range(cases):
        caseLen = int(input())
        caseList = map(int, input().split(" "))
        calculateCost(i + 1, caseList)

if __name__ == "__main__":
    main()
