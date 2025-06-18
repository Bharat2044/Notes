
public class Test01 {
	public static void main(String[] args) {
		College1 c1 = new College1();
		System.out.println(c1); //c1.toString();
		
		Student s1 = new Student(101, "S1", "C1", 2000);
		c1.add(s1);
		System.out.println(c1); //c1.toString();

		Student s2 = new Student(102, "S2", "C2", 3000);
		c1.add(s2);
		System.out.println(c1); //c1.toString();
		
		
	}
}
