import java.util.Scanner;
class ReadNumName {
	public static void main(String[] args) 	{
		Scanner scn = new Scanner(System.in);

		System.out.print("Enter num: ");
		int num = scn.nextInt();        scn.nextLine();

		System.out.print("Enter name: ");
		String name = scn.nextLine();

		System.out.println("\nYou have enteed");
		System.out.println("num : "+ num);
		System.out.println("name: "+ name);
	}
}
