#include <iostream>

using namespace std;

int main(void){
    double x, y, dydx, dx;
    int i;
    x = 0;
    y = 1;
    dx = 0.001;
    dydx = 0;

    for(i=0;i<300;i++){
        dydx += -y*dx;
        y += dydx;
        x += dx;
        cout << x << " " << y << endl;
    }

    return 0;
    
}
