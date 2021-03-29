#include <iostream>
#include <math.h>

using namespace std;

int main(void){
    double x, y, dx, a[10];
    int N;

    cin >> N;
    cin >> dx;
    cin >> x  >> y;
    for(int i=0;i<N+1;i++){
        cout << x << "\t" << y << endl;
        y += pow(cos(x),-2)*dx;
        x += dx;
    }
    return 0;
}