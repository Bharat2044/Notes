/*
Meta Characters
==========================================================================
1) reading all values for kw
2) for loop
3) if condition

4) passing diff characters and digits and numbers
5) passing diff special characters
6) some charactrs are meta characters, they have meaning in command prompt software
7) ^ * .\* ..\* ..\..\* \* & | < >  "  are meta characters
8) if we want to remove the special meaning to the above meta characters we must place them in ""
*/
class ReadingAllValues {
	public static void main(String[] args) 	{

		if(args.length==0){
			System.out.println("You did not pass values");
			return;
		}
		
		for(int i=0; i<args.length; i++){
			System.out.println("args["+i+"]: "+ args[i]);
		}


/*
9) For Reading all values in for loop we use args[i] --> all values we will get
10) For Reading all values in for loop we use args[0] --> 0 index value will come multiple times
11) For Reading all values in for loop we use args[i] with condition <=  --> all values are dispaly with AIOOBE at end
12) For Reading all values in for loop we use args[i] with condition <= with -1 --> all values are dispaly without AIOOBE at end
13) For Reading all values in for loop we use args[i] with condition < with -1 --> last value is not displayed
*/
		//for(int i=0; i<args.length; i++){
		//for(int i=0; i<=args.length; i++){
		//for(int i=0; i<=args.length-1; i++){
		//for(int i=0; i<args.length-1; i++){
		//	System.out.println("args["+0+"]: "+ args[0]);
		//	System.out.println("args["+i+"]: "+ args[i]);
		//}

	}
}