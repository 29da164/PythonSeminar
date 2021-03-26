#include <iostream>
#include <math.h>

using namespace std;

int main(void){
    double x, y, dx, a[10];
    int n, N;

    cin >> n >> N;
    cin >> dx;
    cin >> x  >> y;
    /*
    for (int i=0;i<n+1;i++){
        cin >> a[i];
    }
*/
    for(int i=0;i<N+1;i++){
        y += cos(x)*dx;
        cout << x << "\t" << y << endl;
        x += dx;
    }

    return 0;
    
}