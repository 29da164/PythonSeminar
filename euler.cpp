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
        for(int j=0;j<n+1;j++){
            y += a[j]*pow(x,j)*dx;
        }
        cout << x << "\t" << y << endl;
        x += dx;
    }

    return 0;
    
}