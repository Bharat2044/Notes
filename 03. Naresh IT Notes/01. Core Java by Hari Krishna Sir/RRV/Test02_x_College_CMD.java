//College.java
class  College{
	public static void main(String[] args) {
		//1. create student instance
		Student s1 = new Student();

		//2. read values from cmd line, converting to PV and storing in this instance
		s1.sno			= Integer.parseInt(args[0]);
		s1.sname		= args[1];
		s1.course		= args[2];
		s1.fee			= Double.parseDouble(args[3]);
		s1.email		= args[4];
		s1.mobile		= Long.parseLong(args[5]);
		s1.gender		= args[6].charAt(0);
		s1.studying	= Boolean.parseBoolean(args[7]);

		//3. Read and dispaly values
		System.out.println("Student object values");
		System.out.println("   s1.sno\t\t: "			+ s1.sno);
		System.out.println("   s1.sname\t\t: "	+ s1.sname);
		System.out.println("   s1.course\t\t: "	+ s1.course);
		System.out.println("   s1.fee\t\t: "			+ s1.fee);
		System.out.println("   s1.email\t\t: "		+ s1.email);
		System.out.println("   s1.mobile\t\t: "	+ s1.mobile);
		System.out.println("   s1.gender\t\t: "	+ s1.gender);
		System.out.println("   s1.studying\t\t: "	+ s1.studying);
	}
}
