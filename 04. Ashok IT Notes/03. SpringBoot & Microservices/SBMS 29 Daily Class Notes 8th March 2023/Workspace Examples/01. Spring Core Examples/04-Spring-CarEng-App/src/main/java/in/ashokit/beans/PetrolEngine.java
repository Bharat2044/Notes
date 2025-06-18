package in.ashokit.beans;

public class PetrolEngine implements IEngine {

	public PetrolEngine() {
		System.out.println("PetrolEngine.Constructor....");
	}

	public int start() {
		System.out.println("PetrolEngine Started...");
		return 1;
	}

}
