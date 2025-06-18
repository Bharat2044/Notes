package in.ashokit;

import java.util.Arrays;
import java.util.List;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ConfigurableApplicationContext;

@SpringBootApplication
public class Application {

	public static void main(String[] args) {
		ConfigurableApplicationContext context = SpringApplication.run(Application.class, args);
		
		EmpRepo empRepo = context.getBean(EmpRepo.class);
		AddrRepo addrRepo = context.getBean(AddrRepo.class);

		/*Employee e = new Employee();
		e.setName("Ashok");
		e.setSalary(1000.00);

		Address a1 = new Address();
		a1.setCity("Hyd");
		a1.setState("TG");
		a1.setCountry("India");
		a1.setEmp(e);

		Address a2 = new Address();
		a2.setCity("GNT");
		a2.setState("AP");
		a2.setCountry("India");
		a2.setEmp(e);

		List<Address> addressList = Arrays.asList(a1, a2);
		e.setAddr(addressList);
		empRepo.save(e);*/
		
		//empRepo.findById(10);
		addrRepo.findById(10);
		
		//empRepo.deleteById(1);
		//addrRepo.deleteById(9);
	}

}
