import java.io.DataInputStream;
import java.io.IOException;

class Addition_DIS {
	public static void main(String[] args) throws IOException{

		DataInputStream dis = new DataInputStream(System.in);

		System.out.print("Enter value1: ");
		int a = Integer.parseInt(dis.readLine());

		System.out.print("Enter value2: ");
		int b = Integer.parseInt(dis.readLine());	

		int c = a + b;
		System.out.println("\nAddition result: "+ c);
		System.out.println();


	}
}
