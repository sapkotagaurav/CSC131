/**
 * 
 * @file sapkota_gaurab_lab12.cpp
 * @author Gaurab Sapkota
 * @brief Program to find standard deviation using arrays and vectors
 * @version 0.1
 * @date 2022-05-06
 * 
 * @copyright Copyright (c) 2022
 * 
 */

#include <iostream>
#include <cmath>
#include <iomanip>
#include <vector>

using namespace std;
//overloading the function
double stndardDeviation(vector<double>);


/**
 * @brief Using Array
 * 
 * @param arr 
 * @param arrSize 
 * @return double 
 */
double standardDeviation(double arr[], int arrSize ){
    double sum =0;
    double mean_deviation=0;
    for (int i = 0; i < arrSize; i++)
    {
        sum +=arr[i];
        
    }
    double mean = sum/arrSize;
    for (int i = 0; i < arrSize; i++)
    {
        mean_deviation += pow(arr[i]-mean,2);
        
    }
    double std_dev=sqrt(mean_deviation/arrSize);
    return std_dev;
    
}

/**
 * @brief Main function
 * 
 * @return int 
 */
int main(){
    
    double arr[20] ={2, 11, 4, 5, 9, 5, 4, 12, 7, 8, 9, 3, 7, 4, 12, 10, 9, 6, 9, 4};
    vector<double> vect;
    for (int i = 0; i < 20; i++)
    {
        vect.push_back(arr[i]);
    }
    

    cout<<fixed<<setprecision(2)<<standardDeviation(arr,20)<<endl;
    cout<<fixed<<setprecision(2)<<stndardDeviation(vect)<<endl;

}

/**
 * @brief Using vector
 * 
 * @param vect 
 * @return double 
 */

double stndardDeviation(vector<double> vect){
    double sum =0;
    double mean_deviation=0;
    for (size_t i = 0; i < vect.size(); i++)
    {
        sum += vect.at(i);
        
    }
    double mean = sum / vect.size();
    for (size_t i = 0; i < vect.size(); i++)
    {
        mean_deviation += pow(vect.at(i)-mean,2);
        
    }
    double std_dev=sqrt(mean_deviation/vect.size());
    return std_dev;

    
}