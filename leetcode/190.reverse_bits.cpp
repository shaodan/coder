class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t r = 0;
        for (int i=32;i>0;i--) {
            r = (r<<1) + (n&1);
            n = n>>1;
        }
        return r;
    }
};
