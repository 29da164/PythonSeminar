#include <iostream>
#include <math.h>
using namespace std;

double simp(int d, int n, double x1, double x2, double *a){

    double s, x, h;

    s = 0;
    x = x1;
    h = (x2-x1)/(2*n);

    for(int i=0;i<2*n-1;i=i+2){
        x = x1+h*i;
        for(int j=0;j<d+1;j++){
            s += a[j]*pow(x    ,j)*h/3.0;
            s += a[j]*pow(x+h  ,j)*h/3.0*4.0;
            s += a[j]*pow(x+h*2,j)*h/3.0;
        }
    }
    return s;

}

double exact(int d, double x1, double x2, double *a){

    double theory = 0;
    for(int i=0;i<d+1;i++) theory += a[i]/(i+1)*(pow(x2,i+1)-pow(x1,i+1));
    return theory;

}

int main(void){

    int d, n;
    double x1, x2, a[10], calc_result, theory_result;

    cin >> x1 >> x2;
    cin >> d >> n;
    for(int i=0;i<d+1;i++) cin >> a[i];

    calc_result = simp(d, n, x1, x2, a);
    theory_result = exact(d, x1, x2, a);

    cout << "approx.:" << "\t" << calc_result << endl;
    cout << "exact:"<< "\t\t" << theory_result << endl;
    cout << "error:"<< "\t\t" << theory_result - calc_result << "\t(";
    cout << (calc_result -  theory_result)/theory_result*100 << "%)" << endl;

    return 0;

}