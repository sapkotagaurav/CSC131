#include <iostream>
#include <cmath>
#include <iomanip>
#include <vector>

using namespace std;
double stndardDeviation(vector<double>);

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