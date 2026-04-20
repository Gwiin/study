#include <iostream>
#include <string>
using namespace std;


class WordUtility{
private:
    /* data */
public:
    static int wordCount(string word);
    static string getWord(string line, int n);

    WordUtility(/* args */);
    ~WordUtility();
};

int WordUtility::wordCount(string line){
    int cnt = 0;
    bool inword = false; // inword => 단어안에 있는지 공백에 있는지 상태

    for(int i = 0 ; i < line.length()+1 ; i++){
        if(line[i] == ' ' || line[i] == '\t' || line[i] == '\0'){ //line[i]가 공백일때
            inword = false;
        }
        else{
            if(!inword){ // line[i] 값이 공백이 아니고 line[i-1]의 값이 공백이었을때 == 현재 index부터 단어의 시작
                cnt++;
                inword = true;
            }
        }
    }
    return cnt;
}

string WordUtility::getWord(string line, int n){
    string word = "";
    int cnt = 0;
    bool inword = false;

    for(int i = 0 ; i < line.length()+1 ; i++){
        if(line[i] == ' ' || line[i] == '\t' || line[i] == '\0'){ //line[i]가 공백일 때
            if(inword){ //line[i]가 공백이고 이전 index의 값이 공백이 아닐때 == 이전index로 단어하나가 끝났을때
                if(cnt == n){
                    return word;
                }
                inword = false;
            }
        }
        else {
            if(!inword){
                cnt++;
                inword = true;
            }
            if(cnt == n){
                word += line[i];
            }
        }
    }
    return "";
}

WordUtility::WordUtility(/* args */){}
WordUtility::~WordUtility(){}
  

int main(void){
    int n = WordUtility::wordCount("I love C++");
    cout << "단어 개수는" << n << endl;
    string word = WordUtility::getWord("I love C++", 3);
    if(word == "")
        cout << "3번째 단어는 없습니다." << endl;
    else
        cout << "3번째 단어는 " << word << endl;

    return 0;
}