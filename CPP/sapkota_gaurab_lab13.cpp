/**
 * @file sapkota_gaurab_lab13.cpp
 * @author Gaurab Sapkota
 * @brief 
 * @version 0.1
 * @date 2022-05-12
 * 
 * @copyright Copyright (c) 2022
 * 
 */

#include <iostream>
#include <string>

using namespace std;


double average(double*, int);
void addThree(int *ptr);
/**
 * @brief Main function
 * 
 * @return int 
 */
int main(){
    
    string num;
    double n;
    string length;
    int l;
    int count=0;

    cout<<"Enter the number of doubles:"<<endl;
    getline(cin,length);
    l = stoi(length);
    double *arr = new double(l);

    while (count<l)
    {
        cout<<"Enter a Number:"<<endl;
        getline(cin,num);
        arr[count] = stod(num);
        count = count+1;
    }
    
    cout<<average(arr,l)<<endl;
    delete[] arr; // delete the memory allocation
    

    string three_num ;
    cout<<"Enter your number: ";
    cin>>three_num;
    int t_n = stoi(three_num);
    addThree(&t_n);
    cout<<"After adding three: "<<t_n<<endl;
    
}

/**
 * @brief Function to take dynamic array and return the average
 * 
 * @param arr 
 * @param count 
 * @return double 
 */

double average(double arr[],int count){
    double sum=0;
    for (int i = 0; i < count; i++){
        sum = sum+arr[i];
        
    }
    
    
    return sum/count;

    
}


/**
 * @brief Add three to the pointer 
 * 
 * @param ptr 
 */
void addThree(int *ptr){
    *ptr = *ptr+3;
}