package in.ashokit.beans;

public class Car {

	private IEngine eng;
	
	public Car() {
		System.out.println("Car :: Constructor");
	}

	public void setEng(IEngine eng) {
		System.out.println("setEng ( ) method called...");
		this.eng = eng;
	}

	public void drive() {
		int status = eng.start();
		if (status >= 1) {
			System.out.println("Journey Started..");
		} else {
			System.out.println("Engine Trouble..");
		}
	}
}
