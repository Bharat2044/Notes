import java.util.ArrayList;

public class College3 {
	
	private ArrayList<Student> al;
	
	public College3() {
		al = new ArrayList<>();  
	}
	
	public void add(Student s) {
		al.add(s);  //#1: storing multiple objects
	}				//without size limitation	
	
	public void generateHallTickets() {
		Univesity u = new Univesity();
		u.generateHallTickets(al); //passing all objects
	}			//as argument to another class methods
				//with single parameter
	
	public String toString() {
		return al.toString(); 
	}
	
	
}
