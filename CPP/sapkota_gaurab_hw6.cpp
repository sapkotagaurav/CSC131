#include <iostream>
#include <string>
using namespace std;


string milTime(string);

int main(){
    string s;
    cout<<"Enter the time"<<endl;
    getline(cin,s);
    cout<<"Corresponding Military Time is "<<milTime(s)<<"Hours";

    
}

string milTime(string s){
    string am_pm = s.substr(s.find(" ",1)+1,s.length());
    string hour = s.substr(0,s.find(":",0));
    string min = s.substr(s.find(":",0)+1,s.length()-s.find(" "));
    int h = stoi(hour);
    int m = stoi(min);
    

    if (am_pm =="pM" || am_pm =="PM" || am_pm == "Pm" || am_pm=="pm")
    {
        if (h!=12)
        {
            h = h+12;
        }
        

        
        
    }else
    {
        if (h==12)
        {
            h=0;
        }
        
    }
    
    
   return h<10 ?  "0"+ to_string(h)+min : to_string(h)+min;
}