func singleNumber(nums []int) int {
    var one int = 0
    var two int = 0
    
    for _, n := range nums {
        one = (^two) & (one ^ n)
        two = (^one) & (two ^ n)
    }
    return one
}
