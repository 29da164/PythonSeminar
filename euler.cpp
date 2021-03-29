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
            y += a[j]*pow(x,j)*dx;
        }
        x += dx;
    }
    return 0;
}