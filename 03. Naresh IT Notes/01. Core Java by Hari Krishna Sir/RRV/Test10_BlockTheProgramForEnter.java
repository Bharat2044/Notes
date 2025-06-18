import java.util.Scanner;
class BlockTheProgramForEnter {

	public static void main(String[] args) 	{
		Scanner scn = new Scanner(System.in);

		System.out.print("Enter data: ");
		//int data = scn.nextInt();
		//String data = scn.next();
		String data = scn.nextLine();

		System.out.println("data: "+ data);
	}
}
