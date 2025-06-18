
public class College1 {
	
	private Student s;
	
	public void add(Student s) {
		this.s = s;
	}
	
	public String toString() {
		
		return 
			s==null? 
			"No student is joined":
			s.toString();
	}
}
