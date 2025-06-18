import java.io.IOException;
class SystemDotIn {
	public static void main(String[] args) throws IOException{

		System.out.print("Enter value1: ");		//abc

//		int data = System.in.read();
//		System.out.println(data);
//		System.out.println((char)data);
		
//		System.out.println(System.in.read());  //a		-> 97
//		System.out.println(System.in.read());	//b	-> 98		//number of characters + 2
//		System.out.println(System.in.read());	//c		-> 99
//		System.out.println(System.in.read());	//enter -> 13	
//		System.out.println(System.in.read());	//enter -> 10

//		int data ;
//		while((data = System.in.read()) !=13){
//			System.out.println(data);
//		}///while close

		String value1 = new String();
		int data;
		while((data = System.in.read()) !=13) {
				//value1.concat((char)data); //CE
				//value1.concat(""+(char)data);
				value1 = value1.concat(""+(char)data);
		}//while close
		System.in.read(); //reading enter key char 10 and making "in" object fully empty

		System.out.print("Enter value2: ");
		String value2 = new String();
		while((data = System.in.read()) !=13) {
				value2 = value2.concat(""+(char)data);
		}//while close
		System.in.read(); 

		System.out.println("\nYou entered: ");
		System.out.println("  value1: "+ value1);
		System.out.println("  value2: "+ value2);

		//System.out.println(value1 + value2);

		int a = Integer.parseInt(value1);	
		int b = Integer.parseInt(value2);	
		int c = a + b;
		System.out.println("\nAddition result: "+ c);

	}//main close
}//class close
