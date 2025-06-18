//Addition.java
//Command line arguments application
class Addition {
     public static void main(String[] args) {
			
		int a = Integer.parseInt(args[0]);
		int b = Integer.parseInt(args[1]);
		int c = a + b;
		System.out.println("Result: "+ c);
			

     }
}

/*
D:\01CJ\RRV>javac Addition.java

D:\01CJ\RRV>java Addition  10  20 <-|
							Addition.main(new String[]{"10", "20"});

*/