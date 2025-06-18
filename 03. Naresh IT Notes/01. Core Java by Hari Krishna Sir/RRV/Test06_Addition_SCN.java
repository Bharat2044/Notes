import java.util.Scanner;
class  Addition_SCN {
	public static void main(String[] args) {

		Scanner scn = new Scanner(System.in);

		System.out.print("Enter FNO: ");
		int a = scn.nextInt();

		System.out.print("Enter SNO: ");
		int b = scn.nextInt();

		int c =  a + b;
		System.out.println("Result: " +c);
	}
}
