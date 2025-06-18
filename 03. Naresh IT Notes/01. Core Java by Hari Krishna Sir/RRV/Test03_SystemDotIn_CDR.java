import java.io.IOException;
class SystemDotIn_CDR {
	public static void main(String[] args) throws IOException{


		CustomDataReader cdr = new CustomDataReader();

		System.out.print("Enter value1: ");		
		String value1 =  cdr.readCompleteData();

		System.out.print("Enter value2: ");
		String value2 =  cdr.readCompleteData();

		System.out.println("\nYou entered: ");
		System.out.println("  value1: "+ value1);
		System.out.println("  value2: "+ value2);

		int a = Integer.parseInt(value1);	
		int b = Integer.parseInt(value2);	
		int c = a + b;
		System.out.println("\nAddition result: "+ c);
		System.out.println();
	}//main close
}//class close
