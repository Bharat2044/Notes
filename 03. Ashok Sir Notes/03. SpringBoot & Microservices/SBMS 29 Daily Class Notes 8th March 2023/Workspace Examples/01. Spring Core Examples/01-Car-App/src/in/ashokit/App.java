package in.ashokit;

public class App {

	public static void main(String[] args) {
		Car c = new Car(new PetrolEngine());
		c.drive();
	}
}
