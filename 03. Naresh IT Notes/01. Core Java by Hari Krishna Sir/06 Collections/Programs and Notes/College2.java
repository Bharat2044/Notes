import java.util.Arrays;

public class College2 {
	
	private Student[] sa;
	private int index; 
	
	public College2() {
		sa = new Student[5]; //default capacity
	}
	
	public College2(int capacity) {
		sa = new Student[capacity]; //passed capacity
	}
	
	public void add(Student s) {
		//sa[0] = s;
		sa[index] = s;
		index++;
	}
	
	public String toString() {
		return Arrays.toString(sa);
	}
	
}
