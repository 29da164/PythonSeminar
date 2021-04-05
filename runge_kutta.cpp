#include <iostream>
#include <math.h>

using namespace std;

int main(void){
    double x, y, dx, a[10];
    int n, N;

    cin >> n >> N;
    cin >> dx;
    cin >> x  >> y;
    for (int i=0;i<n+1;i++){
        cin >> a[i];
    }

    for(int i=0;i<N+1;i++){
        cout << x << "\t" << y << endl;
        for(int j=0;j<n+1;j++){
            y += a[j]*pow(x,     j)/6*1*dx;
            y += a[j]*pow(x+dx/2,j)/6*4*dx;
            y += a[j]*pow(x+dx,  j)/6*1*dx;
        }
        x += dx;
    }

    return 0; 
}