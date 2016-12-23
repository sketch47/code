#include<iostream>
#include <cmath>
using namespace std;
void func(double& Xi, double& Yi,double kx, double ky, double h);
int main()
{
double h,Xi,Yi,Xkon,kx,ky;
int n;
cout<<"\t"<<"\t"<<"******************************* *****************n";
cout<<"\t"<<"\t"<<"* * "<<"\n";
cout<<"\t"<<"\t"<<"* Reshenie difurov 1 poryadka methodom Eulera *"<<"\n"; 
cout<<"\t"<<"\t"<<"******************************* ******************" ;
cout<<endl;
cout<<"Vvedite nachaloe znachenie intervala [a,b]=";
cin>>Xi;
cout<<"Vvedite konechoe znachenie intervala [a,b]=";
cin>>Xkon;
cout<<"Vvedite chislo shagov=";
cin>>n;
h=(Xkon- Xi)/n;
cout<<endl;
cout<<"Vvedite nachalnoe uslovie y=";
cin>>Yi;
cout<<"Vvedite koefitsient pri x=";
cin>>kx;
cout<<"Vvedite koefitsient pri y=";
cin>>ky;
cout<<"|Interval|Chislo shagov|Shag prirasheniya|Nacalnoe Y|Uravnenie vida:| "<<"\n";
cout<<"|--------|-------------|-----------------|----------|---------------|"<<"\n";
cout<<"|"<<"["<<Xi<<","<<Xkon<<"]" <<" |"<<n<<" |"<<h<<" |"<<Yi<<" |"<<"y'="<<kx<<"x"<<"+"<<ky<<"y"<<" |"<<"\n";
cout<<endl;
cout<<endl;
for (int i=1;i<=n;i++)
{ 
func(Xi,Yi,kx,ky,h);
cout<<"\n";
}
return 0;
}
 
void func(double& Xi, double& Yi, double kx, double ky, double h)
{
double f1,Yprom,a,Xprom;
f1=(pow(Xi,2.0))+(ky*Yi);
Yprom=Yi+f1*(h/2);
Xprom=Xi+h/2;
a=kx*Xprom-Yprom;
Yi=Yi+a*h;
cout<<"\t"<<"\t"<<"Interval x="<<Xi<<"\t"<<" Resultat y="<<Yi;
Xi=Xi+h;
}
