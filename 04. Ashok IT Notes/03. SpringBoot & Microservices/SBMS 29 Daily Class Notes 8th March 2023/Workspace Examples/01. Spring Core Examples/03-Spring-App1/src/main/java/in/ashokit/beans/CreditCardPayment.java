package in.ashokit.beans;

public class CreditCardPayment implements IPayment {

	public CreditCardPayment() {
		System.out.println("CreditCardPayment :: Constructor");
	}

	public boolean processPayment(double billAmt) {
		// logic

		System.out.println("CreditCard Payment successfull...");

		return true;
	}

}
