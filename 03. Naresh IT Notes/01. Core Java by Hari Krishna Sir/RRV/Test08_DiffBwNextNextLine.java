import java.util.Scanner;
class DiffBwNextNextLine {
	public static void main(String[] args) 	{

				Scanner scn = new Scanner(System.in);

				System.out.print("Enter name: ");
				String name1 = scn.next();
				String name2 = scn.nextLine();

				System.out.println("Your entered name is: "+ name1);
				System.out.println("Your entered name is: "+ name2);
	}
}
