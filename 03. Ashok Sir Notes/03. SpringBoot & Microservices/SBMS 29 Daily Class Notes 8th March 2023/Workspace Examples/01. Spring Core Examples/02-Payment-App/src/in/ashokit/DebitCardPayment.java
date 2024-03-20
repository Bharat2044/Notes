package in.ashokit;

public class DebitCardPayment implements IPayment {

	@Override
	public boolean processPayment(double billAmt) {
		// logic
		System.out.println("Debit Card Payment Processed...");
		return true;
	}

}
