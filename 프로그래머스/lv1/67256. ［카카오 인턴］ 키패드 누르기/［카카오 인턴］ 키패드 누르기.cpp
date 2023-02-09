#include <string>
#include <vector>

using namespace std;

string solution(vector<int> numbers, string hand) {
    int left_loc = 10;     //*
    int right_loc = 12;    //#
    string answer = "";
    
    for (int i = 0; i < numbers.size(); i++) {
        if (numbers[i] == 1 || numbers[i] == 4 || numbers[i] == 7) {
            answer += 'L';
            left_loc = numbers[i];
        }
        else if (numbers[i] == 3 || numbers[i] == 6 || numbers[i] == 9) {
            answer += 'R';
            right_loc = numbers[i];
        }
        else {
            int a;
            int tmp = numbers[i];
            if (tmp != 0) a = (tmp-1) / 3;
            else {
                a = 3;
                tmp = 11;
            }
            int farL;
            int farR;
            if (left_loc % 3 == 1) {
                int l = a * 3 + 1;
                farL = left_loc - l;
                if (farL < 0) farL = (-farL)/3 + 1;
                else farL = farL/3+1;
            }
            else {
                farL = tmp - left_loc;
                if (farL < 0) farL = (-farL) / 3;
                else farL = farL / 3;
            }
            
            if (right_loc % 3 == 0) {
                int r = (a + 1) * 3;
                farR = right_loc - r;
                if (farR < 0) farR = (-farR)/3 + 1;
                else farR = farR/3+1;
            }
            else {
                farR = tmp - right_loc;
                if (farR < 0) farR = (-farR) / 3;
                else farR = farR / 3;
            }
            if (farL < farR) {
                answer += 'L';
                left_loc = tmp;
            }
            else if (farR < farL) { //오른손을 이동
                answer += 'R';
                right_loc = tmp;
            }
            else if (hand == "right") { //오른손을 이동
                answer += 'R';
                right_loc = tmp;
            }
            else {
                answer += 'L';
                left_loc = tmp;
            }
        }
    }
    
    
    return answer;
}