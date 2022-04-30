#include <iostream>
#include <string>

using namespace std;




bool process_date(string);

/**
 * @brief the main function
 * 
 * @return int 
 */
int main(){
    string full_date ;
    string dec;
    cout<< "Enter the date in the format mm/dd/yy :";
    getline(cin, full_date);
    bool processed_date = process_date(full_date);
    dec = processed_date ? "a ":" not a ";
    cout<< full_date + " is "<<dec <<"magic date."<<endl;
    return 0;
}


/**
 * @brief function to process the entered date and return if it is magic date
 * 
 * @param date 
 * @return true 
 * @return false 
 */
bool process_date(string date){
    string month= date.substr(0,date.find("/",0));
    string rem = date.substr(date.find(month)+month.length()+1);
    string day = rem.substr(0,rem.find("/",0));
    string year = rem.substr(rem.find("/",0)+1,rem.length());
    cout<<"Month is "<<month<<"\n"<<"Day is "<<day<<"\n"<<"Year is "<<year<<"\n"<<endl;
    
    return stoi(month)*stoi(day)==stoi(year);
    

}