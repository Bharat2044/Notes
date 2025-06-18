package in.ashokit.util;

import java.io.FileReader;

import com.google.gson.Gson;

import in.ashokit.bindings.Passenger;

public class JsonToJava {
	
	public static void main(String[] args) throws Exception{
		/*ObjectMapper mapper = new ObjectMapper();
		Passenger passenger = mapper.readValue(new File("passenger.json"), Passenger.class);
		System.out.println(passenger);*/
		
		Gson gson = new Gson();
		Passenger p = gson.fromJson(new FileReader("passenger.json"), Passenger.class);
		System.out.println(p);
		
	}
}
