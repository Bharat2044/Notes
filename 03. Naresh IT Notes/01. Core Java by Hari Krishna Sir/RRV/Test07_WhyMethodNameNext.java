import java.util.Scanner;
class  WhyMethodNameNext{
	public static void main(String[] args) {
		
		Scanner scn = new Scanner(System.in);
		
		System.out.print("Enter nums: ");
		int a = scn.nextInt();
		int b = scn.nextInt();
		int c = scn.nextInt();

		System.out.println("a: "+ a);
		System.out.println("b: "+ b);
		System.out.println("c: "+ c);
	}
}

/*
Case #1:  
 Enter nums: 10<-|
 20<-|
 30<-|


 Case #2 
 Enter nums: 10 20<-|
 30<-|

 Case #3:
 Enter nums: 10 20 30<-|

*/
