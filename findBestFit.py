import json
import ioUtils
import handleColor
import heapq

NSMALLEST = 3
TOPSCORE = 3 * (256 ** 2)

def findBestFit(color):
    learned = ioUtils.getLearned()
    distances = {}
    for colorType in learned:
        distances[colorType] = []
        for c in learned[colorType]:
            cOther = handleColor.colorDecompact(c[0])
            distance = getDistance(color, cOther)
            heapq.heappush(distances[colorType], distance)
    fits = {}
    for colorType in distances:
        topSmallest = []
        distHeap = distances[colorType]
        for i in range(min(len(distHeap), NSMALLEST)):
            topSmallest.append(heapq.heappop(distHeap))
        avg = sum(topSmallest) / min(max(1, len(distHeap)), NSMALLEST)
        fits[colorType] = TOPSCORE / (avg + 1) # + 1 to avoid the possibility of dividing by 0

    fitsRanked = sorted(fits.items(), key=lambda x: x[1], reverse=True)
    return fitsRanked[0][0]




def getDistance(color, other):
    rRes = color[0] - other[0]
    gRes = color[1] - other[1]
    bRes = color[2] - other[2]
    return (rRes ** 2) + (gRes ** 2) + (bRes ** 2)

