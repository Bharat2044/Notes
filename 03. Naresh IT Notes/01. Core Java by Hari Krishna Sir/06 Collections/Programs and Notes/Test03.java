
public class Test03 {
	public static void main(String[] args) {
		
		College3 c3 = new College3();
		System.out.println(c3);
		
		Student s1 = new Student(101, "S1", "C1", 2500);
		Student s2 = new Student(102, "S2", "C1", 2500);
		Student s3 = new Student(103, "S3", "C1", 2500);
		Student s4 = new Student(104, "S4", "C1", 2500);
		Student s5 = new Student(105, "S5", "C1", 2500);
		
		c3.add(s1);	
		c3.add(s2);	
		c3.add(s3);	
		c3.add(s4);	
		c3.add(s5);
		
		System.out.println(c3);

		Student s6 = new Student(106, "S6", "C1", 2500);
		for(int i=1; i<=100; i++)
			c3.add(s6);
			
		System.out.println(c3);
		
		
	}
}
