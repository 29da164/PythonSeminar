#include <iostream>
#include <math.h>

using namespace std;

int main(void){
    double x, y, dx, a[10];
    int n, N;

    cin >> N;
    cin >> dx;
    cin >> x  >> y;
    for(int i=0;i<N+1;i++){
        y += (cos(10*x)*exp(-x))*dx;
        cout << x << "\t" << y << endl;
        x += dx;
    }

    return 0;
    
}