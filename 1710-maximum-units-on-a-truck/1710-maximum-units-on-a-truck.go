func maximumUnits(boxTypes [][]int, truckSize int) int {
    sort.Slice(boxTypes, func(i, j int) bool {
        return boxTypes[i][1] > boxTypes[j][1]
    })
    var sumbox, sumunit int = 0, 0
    for _, box := range boxTypes {
        if sumbox + box[0] <= truckSize {
            sumunit += box[1] * box[0]
            sumbox += box[0]
        } else {
            sumunit += box[1] * (truckSize - sumbox)
            break
        }
    }
    return sumunit
}