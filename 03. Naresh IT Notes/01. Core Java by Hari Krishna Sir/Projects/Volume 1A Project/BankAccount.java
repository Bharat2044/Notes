//BankAccount.java
import static java.lang.System.out;		

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileNotFoundException;
import java.io.IOException;

public class  BankAccount{

		private static String bankName;
		private static String branchName;
		private static String ifsc;

		private long accNum;
		private String accHName;
		private double balance;

		static{
			out.println("\nBankAccount class is loaded");
			try{Thread.sleep(1000);}
			catch(InterruptedException e){ }

			out.println("SV memory allocated with default values");
			try{Thread.sleep(1000);}
			catch(InterruptedException e){ }

			out.println("Reading Static variables values from file and intializing them");
			try{Thread.sleep(1000);}
			catch(InterruptedException e){ }

			try {
				/*Connecting to file */
				BufferedReader fileReader = 
					new BufferedReader(new FileReader("bankdetails.txt"));

				/*Reading values file and storing in static variables*/
				bankName		= fileReader.readLine();
				branchName	= fileReader.readLine();
				ifsc					= fileReader.readLine();

				out.println("SV are initialized with file values \n");
				try{Thread.sleep(1000);}
				catch(InterruptedException e){ }

			}catch(FileNotFoundException e){
				out.println("Error: bankdetails.txt file is not found");
			}catch(IOException e){
				e.printStackTrace();
			}

			try{Thread.sleep(1000);}
			catch(InterruptedException e){ }

		}//staic block end

		public BankAccount(long accNum, String accHName, double balance){
			out.println("NSVs memory allocated with default values");
			try{Thread.sleep(1000);}
			catch(InterruptedException e){ }

			out.println("NSVs are being initialized with given values\n");
			try{Thread.sleep(1000);}
			catch(InterruptedException e){ }

			this.accNum		= accNum;
			this.accHName	= accHName;
			this.balance			= balance;

			out.println("NSVs are initialized with given object values\n");
			try{Thread.sleep(1000);}
			catch(InterruptedException e){ }

		}//constructor closed

		public static void setBankName(String bankName){
			BankAccount.bankName = bankName;
		}

		public static String getBankName(){
			return bankName;
		}

		public static void setBranchName(String branchName){
			BankAccount.branchName = branchName;
		}

		public static String getBranchName(){
			return branchName;
		}

		public static void setIfsc(String ifsc){
			BankAccount.ifsc = ifsc;
		}

		public String getIfsc(){
			return ifsc;
		}

		public long getAccNum(){
			return accNum;
		}

		public void setAccHName(String accHName){
			this.accHName = accHName;
		}

		public String getAccHName(){
			return accHName;
		}
		
		public double getBalance(){
			return balance; 
		}

		public void deposit(double amt){
			this.balance = this.balance + amt;
		}

		public void withdraw(double amt){
			this.balance = this.balance - amt;
		}

		public void currentBalance(){
			out.println(balance);
		}
		
		public String toString(){
			return	("\n  bankName\t: "+ bankName) + "\n" +
						("  branchName\t: "+ branchName) + "\n" +
						("  ifsc\t\t: "+ ifsc)  + "\n" +
						("  accNum\t: "+ accNum)  + "\n" +
						("  accHName\t: "+ accHName)  + "\n" +
						("  balance\t: "+ balance);
		}
}
