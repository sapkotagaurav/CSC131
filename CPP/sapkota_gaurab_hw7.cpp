/**
 * @file sapkota_gaurab_hw7.cpp
 * @author Gaurab Sapkota
 * @brief 
 * @version 0.1
 * @date 2022-04-30
 * 
 * @copyright Copyright (c) 2022
 * 
 */

#include <iostream>
#include <fstream>
#include <string>

using namespace std;
int last_digit(string);
int to_digit(char ch);

int main(){
    ifstream file("isbn.txt"); // file is in the same directory named isbn.txt
    string isbn;
    while (getline(file,isbn))
    {
        cout<<last_digit(isbn)<<endl;
    }
    file.close();
    
    

}

/**
 * @brief takes the twelve digit of isbn as string and returns the last digit
 * 
 * @param isbn 
 * @return int 
 */
int last_digit(string isbn){
    int checksum;
    for (int i = 0; i < isbn.length(); i++)
    {
        
        checksum = i%2==0? checksum +to_digit(isbn[i]) : checksum+to_digit(isbn[i])*3; 
        
    }
    
    checksum =10 - checksum %10;

    return checksum ==10?0:checksum;
    


}

/**
 * @brief takes character converts it to digit
 * 
 * @param ch 
 * @return int 
 */
int to_digit(char ch){
    
    return ch-'0';
}
/**
 * test file: isbn.txt
 * 978013213079
978032156384
978007063546
978032126817
978145169885
978013213080
978160469555
978032133487
978147926720


output:
0
2
3
4
5
6
7
9
0
 * 
 */