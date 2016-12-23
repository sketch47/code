#include <iostream>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

int len(char *str){ 
for(int i=0;i<256;i++)
if(str [i]=='\n') return i;
}
///////////////////////////////////////////////////////
//double f(double x0,double y0,double a, double b, double c, double d);
//double hf(double i,double t); 
double func(double a,double b, double c, double d, double x, double y);
///////////////////////////////////////////////////////
int main(){
//2x^2+y

int mark=1,method=1;
char s[256];
//printf("%f//",2.0000000);
double ih,x1,y1;
int delta;
double a=0,b=0,c=0,d=0,symbol[4];
int n,m;
int res[3];
double h,x,y,x0,y0;
double k1,k2,k3,k4;
double f,hf;		
setlocale(LC_ALL, "Russian");

while(method!=0){
	system("CLS");
	cout<<"Программа находит приближенное решение дифференциального \nуравнения первого порядка y'=f(x,y) \nметодом Эйлера и Рунге-Кнута"<<endl;
	cout<<"1 : Метод Эйлера"<<endl;
	cout<<"2 : Метод Рунге-Кутты"<<endl;
	cout<<"0 : Выход"<<endl;
	cin>>method;
	
	if(method==0) return 0;
	if(method==1 || method==2){ 
	system("CLS");
	cout<<"1: Ввод данных с клавиатуры"<<endl;
	cout<<"2: Случайные данные"<<endl;
	cout<<"0: Назад"<<endl;
	
	cin>>mark;
	
	system("CLS");
	switch (mark){
		case 1:
			
			cout<<"Введите уравнение вида ax^b+cy^d:"<<endl;
			fflush(stdin);
			fgets(s, 256, stdin);
			fflush(stdin);
				
		
			symbol[0]=1;
			symbol[1]=1;
			symbol[2]=1;
			symbol[3]=1;	
			//берем из строки коэффициэнты
			for(int i=0;i<256;i++){
				if(s[i]=='x' && a==0) {a=1; n=i;}
				if(s[i]=='x') {n=i; break;}
				if(s[i]=='-'){symbol[0]=-1; i++;
					if(s[i]=='x') {a=1; n=i; break;}
				}
				if(s[i]=='*') i++;
				a*=10;
				a+=int(s[i])-48;
			}
				
				a*=symbol[0];
				//cout<<a<<endl;
			
			if(s[n+1]=='^'){
				if(s[n+2]=='-') {symbol[2]=-1; 
					for(int i=n+3;i<256;i++){
						if(s[i]=='+' || s[i]=='\n' || s[i]=='-')break;
						b*=10;
						b+=int(s[i]-48);
						
						
						
					
					}
				}
				
				if(s[n+2]!='-'){
						for(int i=n+2;i<256;i++){
					 	if(s[i]=='+' || s[i]=='\n' || s[i]=='-')break;
						b*=10;
						b+=int(s[i]-48);
						}
						
				}
			}
			else b=1;
				b=symbol[2]*b;
				cout<<b<<" "<<endl;
			if(s[n+1]=='+' || s[n+1]=='-') {m=n+1; b=1;}
			//cout<<"m="<<m<<endl;;
			
			for(int i=m;i<256;i++){
				if(s[i]=='y' && c==0) {c=1; n=i;}
				if(s[i]=='y') {n=i; break;}
				if(s[i]=='-'){symbol[1]=-1; i++;
					if(s[i]=='y') {c=1; n=i; break;}
				}
				if(s[i]=='+') {i++;
				if(s[i]=='y') {c=1;n=i;break;}
				}
				c*=10;
				c+=int(s[i])-48;
				
			}
			//cout<<c<<endl;
			c*=symbol[1];
			//cout<<"n="<<n<<endl;
			if(s[n+1]=='^'){
				if(s[n+2]=='-') {symbol[3]=-1; 
					for(int i=n+3;i<256;i++){
						if(s[i]=='+' || s[i]=='\n' || s[i]=='-')break;
						d*=10;
						d+=int(s[i]-48);
					}
				}
				
				if(s[n+2]!='-'){
						for(int i=n+2;i<256;i++){
						 	if(s[i]=='+' || s[i]=='\n' || s[i]=='-')break;
							d*=10;
							d+=int(s[i]-48);
						}
				}
			}
			else d=1;
			d*=symbol[3];
			cout<<d<<endl;
			//std::cout<<a<<" "<<b<<" "<<c<<" "<<d<<" "<<std::endl;
			//конец
			cout<<"Введите шаг: "<<endl;
			cin>>h;
			cout<<"Введите начало отрезка: "<<endl;
			cin>>x;
			cout<<"Введите конец отрезка: "<<endl;
			cin>>y;	
			cout<<"Введите начальные значения x0 y0:"<<endl;
			cin>>x0>>y0;
		break;
		
		case 2:
			while(y!=11){
				srand(time(0));
				x=(rand() % 10);
				y=(rand() % 10);
				if(y>x) break;
			}
			cout<<x<<y<<"x=y="<<endl;
			while(y0!=11){
				
				x0=(rand()% 10);
				y0=(rand()% 10);
				if(y0>x0) break;
			}
			
				h=	1+ (rand()% int(y));
				
			h=h/10;
			a=-2 + (rand()% (5));
			b=-2 + (rand()% (5));
			c=-2 + (rand()% (5));
		 	d=-2 + (rand()% (5));
			cout<<"Конец отрезка ="<<y<<" "<<"Начало отрезка ="<<x<<endl;
			cout<<"Начальное значение x="<<x0<<" "<<"Начальное значение y="<<y0<<endl;
			cout<<"Шаг ="<<h<<endl;
			cout<<"a ="<<a<<" "<<"b ="<<b<<" "<<"c ="<<c<<" "<<"d ="<<d<<endl;
		break;
			
		default:
			break ;
	}
	
	
	
	delta=(y-x)/h;
	double xi[int(delta)],yi[int(delta)];
	ih=h;
	//cout<<"?//////////////////////?"<<endl;
	//cout<<r<<endl;
	xi[0]=x0; yi[0]=y0;
	
	if(mark==1 || mark==2){//если второе меню выбрано
		if(method==1){//и если выбран метод эйлера
		//cout<<xi[0]<<"       "<<yi[0]<<"       "<<a<<"       "<<b<<endl;
			cout<<"x[i]"<<"     "<<"y[i]"<<"       "<<"f"<<"       "<<"hf"<<endl;
			for(int i=1;i<=delta+1;i++){
				
				//f=pow(a*xi[i-1],b)+pow(c*yi[i-1],d);
				f= func(a,b,c,d,xi[i-1],yi[i-1]);
				//cout<<"F="<<pow(a*xi[i-1],b)<<endl;
				hf=f*h;
				if(f== HUGE_VAL) break;
				cout<<xi[i-1]<<"       "<<yi[i-1]<<"       "<<f<<"       "<<hf<<endl;
				yi[i]=yi[i-1]+hf;
				xi[i]=xi[i-1]+h;
				
			}
			
			system("PAUSE");
			system("CLS");
		}
	
		
			if(method==2){//если выбран метод Рунге-Кутты
			
			cout<<"x[i]"<<"     "<<"y[i]"<<"       "<<"K1=F"<<"       "<<"K2"<<"     "<<"K3"<<"       "<<"K4"<<"       "<<"delta(y)"<<endl;
			for(int i=1;i<=delta+1;i++){
				
				//f=pow(a*xi[i-1],b)+pow(c*yi[i-1],d);
				k1=func(a,b,c,d,xi[i-1],yi[i-1]);
				k2=func(a,b,c,d,xi[i-1]+h/2.0,yi[i-1]+(h*k1/2.0));
				k3=func(a,b,c,d,xi[i-1]+h/2.0,yi[i-1]+(h*k2/2.0));
				k4=func(a,b,c,d,xi[i-1]+h,yi[i-1]+(h*k3));
				hf=h/6*(k1+2*k2+2*k3+k4);//delta(y)
				
				if(f== HUGE_VAL  ) break;
				
				cout<<xi[i-1]<<"     "<<yi[i-1]<<"       "<<k1<<"       "<<k2<<"     "<<k3<<"       "<<k4<<"       "<<hf<<endl;
				
				yi[i]=yi[i-1]+hf;
				xi[i]=xi[i-1]+h;
				
			}
			
			system("PAUSE");
			system("CLS");
		}
	}

}
f=0;hf=0;
a=0;b=0;c=0;d=0;
}//end while

return 0;
}

double func(double a,double b, double c, double d, double x, double y){

return a*pow(x,b)+c*pow(y,d);
}

