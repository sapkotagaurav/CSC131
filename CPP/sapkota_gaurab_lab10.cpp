/*
A program to calculate the retail price of objects.
Name:Gaurab Sapkota
Class: CSC131
Section: Thursday lab section


*/


#include <iostream>
#include <string>
using namespace std;

float calculateMarkup(float,float);

int main(){
    string name;
    float markedPrice;
    float markupPc;
    cout<< "Enter the name of the item"<<endl;
    getline(cin,name);
    cout<<"You Entered " <<name<<endl;
    cout<< "Enter the wholesale price of the item"<<endl;
    cin>>markedPrice;
    cout<<"You Entered " <<markedPrice<<endl;
    cout<< "Enter the markup percentage of the item"<<endl;
    cin>>markupPc;
    cout<<"You Entered " <<markupPc<<endl;
    
    cout<<"The retail price is "<< calculateMarkup(markedPrice,markupPc)<<endl;
    


}

float calculateMarkup(float markedPrice, float markupPc){
 float   retailPrice = markedPrice + markedPrice *markupPc/100;
    return retailPrice;
}