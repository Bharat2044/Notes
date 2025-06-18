
public class Test02 {
	public static void main(String[] args) {
		
		College2 c2 = new College2();
		System.out.println(c2); //c2.toString();
		
		Student s1 = new Student(101, "S1", "C1", 2500);
		Student s2 = new Student(102, "S2", "C1", 2500);
		Student s3 = new Student(103, "S3", "C1", 2500);
		Student s4 = new Student(104, "S4", "C1", 2500);
		Student s5 = new Student(105, "S5", "C1", 2500);
		
		c2.add(s1);
		c2.add(s2);
		c2.add(s3);
		c2.add(s4);
		c2.add(s5);
		
		System.out.println(c2);
		
		Student s6 = new Student(106, "S6", "C1", 2500);
		c2.add(s6);
		
		System.out.println(c2);
		
	}
}
