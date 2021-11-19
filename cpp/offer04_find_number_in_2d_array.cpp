#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    bool binarySearch(vector<int> &col, int target, int left, int right)
    {
        while (left <= right)
        {
            int mid = (left+right)/2;
            if (col[mid] == target)
                return true;
            else if (col[mid] < target)
                left = mid + 1;
            else
                right = mid - 1;
        }
        return false;
    }
    bool findNumberIn2DArray1(vector<vector<int> > &matrix, int target)
    {
        int row_num = matrix.size();
        int col_num = 0;
        for (int r_i = 0; r_i < row_num; r_i++)
        {
            col_num = matrix[r_i].size();
            if (col_num == 0)
                break;
            int left = 0;
            int right = col_num - 1;
            vector<int> row = matrix[r_i];
            if (row[left] <= target && row[right] >= target)
            {
                if (binarySearch(row, target, left, right))
                {
                    return true;
                }
            }
        }
        return false;
    }

    bool findNumberIn2DArray(vector<vector<int> > &matrix, int target)
    {
        int row_num = matrix.size();
        int col_num = 0;
        if (row_num != 0)
            col_num = matrix[0].size();
        else
            return false;

        int row_i = 0; 
        int col_i = col_num - 1;

        while (row_i < row_num && col_i >= 0)
        {
            int value = matrix[row_i][col_i];
            if (value == target)
                return true;
            else if (value > target)
                col_i --;
            else
                row_i ++;
        }
        return false;
    }
};

int main()
{
    // int row_num = 10;
    // int col_num = 12;
    // vector<vector<int> > matrix(row_num, vector<int>(col_num, 0));
    vector<vector<int> > matrix = {
        {1,4,7,11,15},
        {2,5,8,12,19},
        {3,6,9,16,22},
        {10,13,14,17,24},
        {18,21,23,26,30}
    };
    Solution *s = new Solution();
    bool result = s->findNumberIn2DArray(matrix, 20);
    cout<<result;
    return 0;
}