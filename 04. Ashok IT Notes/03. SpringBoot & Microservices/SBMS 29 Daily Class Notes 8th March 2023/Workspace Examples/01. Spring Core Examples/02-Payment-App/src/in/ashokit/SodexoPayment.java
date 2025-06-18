package in.ashokit;

public class SodexoPayment implements IPayment{
	
	@Override
	public boolean processPayment(double billAmt) {
		// logic
		System.out.println("Sodexo Payment Processed...");
		return true;
	}

}
