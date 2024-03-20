package in.ashokit.util;

import java.io.File;

import javax.xml.bind.JAXBContext;
import javax.xml.bind.Unmarshaller;

import in.ashokit.binding.Person;

public class UnmarshalDemo {
	
	public static void main(String[] args) throws Exception {
		
		JAXBContext context = JAXBContext.newInstance(Person.class);
		
		Unmarshaller unmarshaller = context.createUnmarshaller();
		
		Person p  = (Person) unmarshaller.unmarshal(new File("person.xml"));
		
		System.out.println(p);
	}
}
