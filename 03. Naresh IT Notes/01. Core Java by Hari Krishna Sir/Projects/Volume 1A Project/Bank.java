//Bank.java
import java.util.Scanner;
import java.util.concurrent.atomic.AtomicLong;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.FileNotFoundException;
import java.io.IOException;


public class  Bank {
	private BankAccount[] accounts;
	private int                      size;

	private Scanner scanner;
	private AtomicLong accNumGenerator ;
	
	public Bank(){
		accounts					= new BankAccount[10];
	    size							= 0;
		scanner					= new Scanner(System.in);

		try{
		
			BufferedReader accNumReader = new BufferedReader(new FileReader("accNumSeq.txt"));
			long accNumSeq		= Long.parseLong(accNumReader.readLine());
			accNumGenerator  = new AtomicLong(accNumSeq);

		}catch(FileNotFoundException e){
			System.out.println("accNumSeq.txt is not found");
		}catch(IOException e){
			e.printStackTrace();
		}

	}//Bank() close

	private void pause(){
		try{Thread.sleep(2000);}
		catch(InterruptedException e ){ }
	}

	public void openAccount(){

		long accNum = accNumGenerator.incrementAndGet();

		System.out.print("Enter Account Holder Name: ");
		String accHName = scanner.nextLine();

		System.out.print("Enter balance: ");
		double balance = scanner.nextDouble(); scanner.nextLine();

		System.out.println("BankAccount object creation started....");
		pause();

		BankAccount account = new BankAccount(accNum, accHName, balance);
		System.out.println("BankAccount object is created");
		pause();

		accounts[size++] = account;
		System.out.println("BankAccount object is stored in Bank");
		pause();

		//saving account number in file
		try{
			FileWriter fw = new FileWriter("accNumSeq.txt");
			fw.write(""+accNum);
			fw.flush();
		}catch(FileNotFoundException e){
			 System.out.println("accNumSeq.txt file is not found");
		}catch(IOException e){
			e.printStackTrace();
		}
	}//openAccount() method close


	private BankAccount getAccount(long accNum) throws IllegalArgumentException{
		if(accNum <= 0)
			throw new IllegalArgumentException("Account number can not be -VE number and ZERO");

		System.out.println("Searching for given accountNumber  object");
		pause();	

		//Linear search algorithm 
		for(int i=0; i<size; i++){ //loop for finding BankAccount object for the given accnumber
			BankAccount account = accounts[i];

			if(account.getAccNum() == accNum)
				return account;
		}

		return null;				
	}

	private boolean amountZeroOrNegative(double amt) {
		return amt <= 0 ? true: false;			
	}

	private boolean amountGreaterThanBalance(BankAccount account, double amt) {
		return amt > account.getBalance() ? true: false;
	}

	public void deposit(long accNum, double amt) throws IllegalArgumentException{
		System.out.println("deposit operation start");
		pause();
		
		//retrieving the BankAccount object of the given account number
		BankAccount account = getAccount(accNum);		

		//checking account and balance valid or not
		if(account == null)		
			throw new IllegalArgumentException("Account is not found with the given details");
		 
		if(amountZeroOrNegative(amt))
			throw new IllegalArgumentException("Amount can not be -VE number ZERO");

		//depositing given amount in the given account
		account.deposit(amt);
		System.out.println("Cash RS "+ amt + " is credited to your account");

		pause();

	}//deposit close

	public void withdraw(long accNum, double amt) throws IllegalArgumentException{

		System.out.println("withdraw operation start");
		pause();
		
		//retrieving the BankAccount object of the given account number
		BankAccount account = getAccount(accNum);		

		//checking account and balance valid or not
		if(account == null)		
			throw new IllegalArgumentException("Account is not found with the given details");
		 
		if(amountZeroOrNegative(amt))
			throw new IllegalArgumentException("Amount can not be -VE number ZERO");

		if(amountGreaterThanBalance(account, amt))
			throw new IllegalArgumentException("Insufficient Funds");

		account.withdraw(amt);
		System.out.println("Cash Rs "+ amt + " is debited from your account");
		
		pause();

	}//withdraw close

	public void balanceEnquiry(long accNum) throws IllegalArgumentException{

		System.out.println("balance equiry operation start");
		pause();
		
		//retrieving the BankAccount object of the given account number
		BankAccount account = getAccount(accNum);		

		//checking account and balance valid or not
		if(account == null)		
			throw new IllegalArgumentException("Account is not found with the given details");

		System.out.print("Current Balance: ");
		account.currentBalance();

		pause();

	}//balanceEnquiry close

	public void transferMoney(long sourceAccNum, long destinationAccNum, double amt) 
																										throws IllegalArgumentException{
		System.out.println("transfer money operation start");
		pause();

		withdraw(sourceAccNum, amt);
		deposit(destinationAccNum, amt);

		System.out.println("transfer money operation end");
		pause();

	}//transferMoney close

	public void updateAccount(long accNum){
			//Think from bank point of view and develop update code by your own
	}

	public void closeAccount(long accNum) throws IllegalArgumentException{
		System.out.println("closeAccount operation start");
		pause();
						
		if(accNum <= 0)
			throw new IllegalArgumentException("Account can not be -VE number and ZERO");

		System.out.println("Searching for given accountNumber  object");
		pause();

		//Linear search algorithm 
		for(int i=0; i<size; i++){ //for finding BankAccount object for the given accnumber
			BankAccount account = accounts[i];

			if(account.getAccNum() == accNum){
				
				for(int j = i; j<size-1; j++){			//removing current location object
					accounts[j] = accounts[j+1];		//by moving next object one location LEFT	
				}

				accounts[size-1] = null;				//removing reference from last location
				size--;											//decreasing size by one

				System.out.println("account is deleted");
				pause();
				return;
			}
		}//for loop closed
		
		throw new IllegalArgumentException("Account is not found with the given details");

	} //closeAccount() end

	public void displayAccount(long accNum) throws IllegalArgumentException{
		System.out.println("\ndisplayAccount operation start");
		pause();
		
		//retrieving the BankAccount object of the given account number
		BankAccount account = getAccount(accNum);		

		//checking account and balance valid or not
		if(account == null)		
			throw new IllegalArgumentException("Account is not found with the given details");
		 
		System.out.println("Account details");
		System.out.println(account);

	}//displayAccount close

	public String toString(){
		StringBuilder accountsBuilder = new StringBuilder();

		if(size == 0)
			return "No accounts found";

		for(int i=0; i<size; i++){
			accountsBuilder.append("\naccount "+(i+1)+ " details: ");
			accountsBuilder.append(accounts[i]+"\n");
		}

		return accountsBuilder.toString();
	}

}
