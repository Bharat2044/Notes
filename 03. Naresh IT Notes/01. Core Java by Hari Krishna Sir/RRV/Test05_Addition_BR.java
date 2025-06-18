import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

class Addition_BR {
	public static void main(String[] args) throws IOException{

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		System.out.print("Enter value1: ");
		int a = Integer.parseInt(br.readLine());

		System.out.print("Enter value2: ");
		int b = Integer.parseInt(br.readLine());	

		int c = a + b;
		System.out.println("\nAddition result: "+ c);
		System.out.println();


	}
}
