import java.io.Console;

class LoginValidator {
	public static void main(String[] args) {
		
		Console cns = System.console();
	
		System.out.print("Enter Username: ");
		String usn = cns.readLine();

		System.out.print("Enter Password: ");
		char[] pwd = cns.readPassword();

		System.out.println("\nYou entered");
		System.out.println("   Username: "+usn);
		System.out.println("   Password: "+new String(pwd));

	}
}
