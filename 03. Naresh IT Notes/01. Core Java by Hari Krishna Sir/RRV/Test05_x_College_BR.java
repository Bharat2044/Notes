//College.java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

class  College_BR{
	public static void main(String[] args) throws IOException {
		//1. create student instance
		Student s1 = new Student();
		
		//2. read values from console by promting messege, converting to PV and storing in this instance 
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		System.out.print("Enter sno\t\t: " );
		s1.sno			= Integer.parseInt(br.readLine());

		System.out.print("Enter sname\t\t: " );
		s1.sname		= br.readLine();

		System.out.print("Enter course\t\t: " );
		s1.course		= br.readLine();

		System.out.print("Enter fee\t\t: " );
		s1.fee			= Double.parseDouble(br.readLine());

		System.out.print("Enter email\t\t: " );
		s1.email		= br.readLine();

		System.out.print("Enter mobile\t\t: " );
		s1.mobile		= Long.parseLong(br.readLine());

		System.out.print("Enter gender\t\t: " );
		s1.gender		= br.readLine().charAt(0);

		System.out.print("Enter studying\t\t: " );
		s1.studying	= Boolean.parseBoolean(br.readLine());

		//3. Read and dispaly values
		System.out.println("\nStudent object values");
		System.out.println("   s1.sno\t\t: "			+ s1.sno);
		System.out.println("   s1.sname\t\t: "	+ s1.sname);
		System.out.println("   s1.course\t\t: "	+ s1.course);
		System.out.println("   s1.fee\t\t: "			+ s1.fee);
		System.out.println("   s1.email\t\t: "		+ s1.email);
		System.out.println("   s1.mobile\t\t: "	+ s1.mobile);
		System.out.println("   s1.gender\t\t: "	+ s1.gender);
		System.out.println("   s1.studying\t\t: "	+ s1.studying);
	}
}
