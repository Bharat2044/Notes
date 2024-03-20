package in.ashokit;

public class App {

	public static void main(String[] args) {

		IPayment p1 = new CreditCardPayment();

		// constructor injection
		PaymentService ps = new PaymentService(p1);

		ps.doPayment(100.00);

	}
}
