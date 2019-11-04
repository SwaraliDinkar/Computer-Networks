#include<iostream>
#include<math.h>

using namespace std;
int main()
{
char ch;
do{

int arr[7]={0};
int temp[3]={0};
int check[3]={0};
int t1;

int choice;
cout<<"1.Generate the number.\n2.Check the number if error exists"<<endl;
cin>>choice;
switch(choice){
	case 1:
		cout<<"Enter the 4 digit number\n";
		cin>>arr[2]>>arr[4]>>arr[5]>>arr[6];

		temp[0]=arr[2]+arr[4]+arr[6];
			if(temp[0]%2==1)
			{
				arr[0]=1;
			}

		temp[1]=arr[2]+arr[5]+arr[6];
			if(temp[1]%2==1)
			{
				arr[1]=1;
			}

		temp[2]=arr[4]+arr[5]+arr[6];
			if(temp[2]%2==1)
			{
				arr[3]=1;
			}
		cout<<"Hamming code is: "<<endl;
		for(int i=0;i<7;i++)
		{
		cout<<arr[i]<<" ";
		}
break;

case 2:
		arr[7]={0};
		cout<<"\nEnter the 7-digit number:"<<endl;
		for(int j=0;j<7;j++)
		{
			cin>>arr[j];
		}

		check[0]=arr[0]+arr[2]+arr[4]+arr[6];
		check[1]=arr[1]+arr[2]+arr[5]+arr[6];
		check[2]=arr[3]+arr[4]+arr[5]+arr[6];
		
		t1=0;
		for(int k=0;k<=2;k++)
		{
			if(check[k]%2==1)
		{
			t1=t1+pow(2,k);
		}
		}
		cout<<"\n\n"<<t1-1<<" is the altered bit.";
break;
		default:
		cout<<"Invalid choice";
		break;

}
cout<<"\nDo you want to continue?"<<endl;
cin>>ch;
}while(ch!='n');

return 0;
}











