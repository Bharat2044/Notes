import java.io.IOException;
class CustomDataReader {

	String readCompleteData() throws IOException{

		String value = new String();
		int data;
		while((data = System.in.read()) !=13) {
				value = value.concat(""+(char)data);
		}//while close
		System.in.read(); 

		return value;

	}//method close

}//class close
