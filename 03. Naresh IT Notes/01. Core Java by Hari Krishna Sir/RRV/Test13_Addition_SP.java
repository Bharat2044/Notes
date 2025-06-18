class  Addition {
	public static void main(String[] args) {
		
		String fno = System.getProperty("fno");
		String sno = System.getProperty("sno");

		int a = Integer.parseInt(fno);
		int b = Integer.parseInt(sno);
		int c = a + b;

		System.out.println("Result: "+ c);
	}
}

/*
>javac Test13_Addition_SP.java

>java -Dfno=10 -Dsno=20 Addition
Result: 30
*/
