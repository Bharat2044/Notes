//College.java
import java.util.Scanner;

class  College{
	public static void main(String[] args) {
		//1. create student instance
		Student s1 = new Student();
		
		//2. Connecting to kb
		Scanner scn = new Scanner(System.in);

		//3. read values from console by promting messege, and storing in this instance 
		System.out.print("Enter sno\t\t: " );
		s1.sno			= scn.nextInt();    scn.nextLine();

		System.out.print("Enter sname\t\t: " );
		s1.sname		= scn.nextLine();

		System.out.print("Enter course\t\t: " );
		s1.course		= scn.nextLine();

		System.out.print("Enter fee\t\t: " );
		s1.fee			= scn.nextDouble();

		System.out.print("Enter email\t\t: " );
		s1.email		= scn.next();

		System.out.print("Enter mobile\t\t: " );
		s1.mobile		= scn.nextLong();

		System.out.print("Enter gender\t\t: " );
		s1.gender		= scn.next().charAt(0);

		System.out.print("Enter studying\t\t: " );
		s1.studying	= scn.nextBoolean();

		//4. dispaly values
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
