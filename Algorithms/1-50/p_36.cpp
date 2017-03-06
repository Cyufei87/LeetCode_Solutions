// Valid Sudoku
// 直接枚举判断三种类型的情况，我是用二进制位存储了某一种情况的当前状态
class Solution {
public:
    bool isValidSudoku(vector<vector<char> >& board) {
        for(int i=0; i<9; i++){
            int status = 0;
            int status2 = 0;
            for(int j=0; j<9; j++){
                int digit, key;
                if(board[i][j]!='.'){
                    digit = board[i][j] - '0';
                    key = (1<<digit);
                    if((status&key)>0){
                        return false;
                    }
                    status |= key;
                }
                if(board[j][i]!='.'){
                    digit = board[j][i] - '0';
                    key = (1<<digit);
                    if((status2&key)>0){
                        return false;
                    }
                    status2 |= key;
                }
            }
        }
        for(int i=0; i<9; i+=3){
            for(int j=0; j<9; j+=3){
                int status = 0;
                for(int m=i; m<i+3; m++){
                    for(int n=j; n<j+3; n++){
                        if(board[m][n]!='.'){
                            int digit = board[m][n] - '0';
                            int key = (1<<digit);
                            if((status&key)>0){
                                return false;
                            }
                            status |= key;
                        }
                    }
                }
            }
        }
        return true;
    }
};
