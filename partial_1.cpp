#include <iostream>
#define N 10
using namespace std;

int main(void){

    double u_old[N+1], u_new[N+1], lamb, rho, c, dx;

    lamb = 80.4;
    rho = 7874;
    c = 461;
    dx = 0.1;

    for(int i=1; i<N; i++) u_old[i] = 1000;
    u_old[0]=300;
    u_old[N]=300;

    for(int t=0;t<3600;t++){
        for(int i=1;i<N;i++){
            u_new[i] = u_old[i] + lamb/(rho*c*dx*dx)*(u_old[i+1] - 2*u_old[i] + u_old[i-1]);
        }
        for(int i=1; i<N; i++){
            u_old[i] = u_new[i];
        }
        if((t%10==0)&&(t%60==0)) {
            cout << t << "\t";
            for(int i=0; i<N+1; i++) cout << u_old[i] << "\t";
            cout << endl;
        }
    }
    return 0;
}