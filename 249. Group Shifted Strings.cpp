// 249. Group Shifted Strings
// Medium
// 29952FavoriteShare
// Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:
// "abc" -> "bcd" -> ... -> "xyz"
// Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.
// Example:
// Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
// Output: 
// [
//   ["abc","bcd","xyz"],
//   ["az","ba"],
//   ["acef"],
//   ["a","z"]
// ]
class Solution {
public:
    vector<vector<string>> groupStrings(vector<string>& strings) {
        unordered_map<string,vector<string>> map;
        for (string x : strings){
            string temp = x;
            for (int i = 0; i < x.size();i++){
                if (x[i] < x[0]){
                    temp[i] = '0'+26 + x[i]-x[0];
                }
                else temp[i] = '0'+x[i]-x[0];
            }
            //cout<<temp<<endl;
            if (map.find(temp)!=map.end()){
                map[temp].push_back(x);
            }
            else map[temp] = vector<string>{x};
            
        }
        vector<vector<string>> result;
        for (auto it = map.begin();it != map.end();it++){
            result.push_back(it->second);
        }
        return result;
    }
};
