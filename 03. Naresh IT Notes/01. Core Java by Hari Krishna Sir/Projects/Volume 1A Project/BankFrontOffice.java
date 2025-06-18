//BankFrontOffice.java
import java.util.Scanner;
public class BankFrontOffice {
	public static void main(String[] args) {

		Bank hdfcBank = new Bank();
		Scanner scn = new Scanner(System.in);

		loop: while(true) {
			System.out.println("\nChoose one option");
			System.out.println("  1. OpenAccount");
			System.out.println("  2. Account details");
			System.out.println("  3. Deposit");
			System.out.println("  4. Withdraw");
			System.out.println("  5. Balance Enquiry");
			System.out.println("  6. Transfer Money");
			System.out.println("  7. Display all accounts");
			System.out.println("  8. Exit");

			System.out.print("Enter option: ");
			int option = scn.nextInt(); scn.nextLine();

			try{
				switch(option){
					case 1: {//OpenAccount
						hdfcBank.openAccount();
						break;
					}
					case 2: {//Account details 
						System.out.print("Enter account number: ");
						long accNum = scn.nextLong();  scn.nextLine();
						hdfcBank.displayAccount(accNum); 
						break;
					}
					case 3:{ //Deposit
						System.out.print("Enter account number: ");
						long accNum = scn.nextLong(); scn.nextLine();

						System.out.print("Enter deposit amount: ");
						double amt = scn.nextDouble(); scn.nextLine();

						hdfcBank.deposit(accNum, amt);
						break;
					}
					case 4: {//Withdraw
						System.out.print("Enter account number: ");
						long accNum = scn.nextLong(); scn.nextLine();

						System.out.print("Enter withdraw amount: ");
						double amt = scn.nextDouble(); scn.nextLine();

						hdfcBank.withdraw(accNum, amt);

						break;
					}
					case 5: {//Balance Enquiry
						System.out.print("Enter account number: ");
						long accNum = scn.nextLong(); scn.nextLine();

						hdfcBank.balanceEnquiry(accNum);

						break;
					}
					case 6: {//Transfer Money
						System.out.print("Enter source account number: ");
						long srcAccNum = scn.nextLong(); scn.nextLine();

						System.out.print("Enter dest account number: ");
						long destAccNum = scn.nextLong(); scn.nextLine();

						System.out.print("Enter deposit amount: ");
						double amt = scn.nextDouble(); scn.nextLine();

						hdfcBank.transferMoney(srcAccNum, destAccNum, amt);

						break;
					}
					case 7: {//Display all accounts
						System.out.println(hdfcBank);
						break;
					}
					case 8: //Exit
						System.out.println("_/\\__/\\__/\\_ Thank You, Please Visit Again _/\\__/\\__/\\_");
						break loop;

					default:
						System.out.println("Invalid option");

				}//switch end

			}catch(IllegalArgumentException e){
				System.out.println("Error: "+e.getMessage());
			}
		}//while(true) end

	}//main close
}//class close
