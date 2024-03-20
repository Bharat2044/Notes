package in.ashokit.beans;

public class DebitCardPayment implements IPayment {
	
	public DebitCardPayment() {
		System.out.println("DebitCardPayment :: Constructor");
	}

	public boolean processPayment(double billAmt) {

		// logic

		System.out.println("DebitCard Payment successfull...");
		
		return true;
	}

}
