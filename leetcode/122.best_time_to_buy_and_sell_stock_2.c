int maxProfit(int* prices, int pricesSize) {
    int i;
    int profit=0;
    int up;
    for (i=1;i<pricesSize;i++) {
        up=prices[i]-prices[i-1];
        if (up>0) {
            profit += up;
        }
    }
    return profit;
}
