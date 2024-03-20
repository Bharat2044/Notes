package in.ashokit;

public class CreditCardPayment implements IPayment {

	@Override
	public boolean processPayment(double billAmt) {
		// logic
		System.out.println("Credit Card Payment Processed..");
		return true;
	}

}
