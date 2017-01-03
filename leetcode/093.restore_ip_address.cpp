class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> r;
        int len = s.length();
        if (len < 4 || len > 12)
            return r;
        string MAX = "255";
        string ip1, ip2, ip3, ip4;
        for (int i=1;i<=3 && i<=len-3;i++) {
            ip1 = s.substr(0, i);
            // r.push_back("ip1:"+ip1);
            if (i>1 && ip1[0] =='0' || i==3 && ip1>MAX)
                break;
            for (int j=1;j<=3 && j<=len-2-i;j++) {
                ip2 = s.substr(i, j);
                // r.push_back("ip2:"+ip2);
                if (j>1 && ip2[0] =='0' || j==3 && ip2>MAX)
                    break;
                for (int k=1;k<=3 && k<=len-1-i-j;k++) {
                    ip3 = s.substr(i+j, k);
                    // r.push_back("ip3:"+ip3);
                    if (k>1 && ip3[0] =='0' || k==3 && ip3>MAX)
                        break;
                    ip4 = s.substr(i+j+k, len-i-j-k);
                    // r.push_back("ip4:"+ip4);
                    if (len-i-j-k >1 && ip4[0] =='0' || len-i-j-k > 3 || len-i-j-k==3 && ip4 > MAX)
                        continue;
                    r.push_back(ip1+'.'+ip2+'.'+ip3+'.'+ip4);
                }
            }
        }
        return r;
    }
};
