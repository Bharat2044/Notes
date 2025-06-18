package in.ashokit;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ConfigurableApplicationContext;

import in.ashokit.entity.Employee;
import in.ashokit.repo.EmployeeRepository;

@SpringBootApplication
public class Application {

	public static void main(String[] args) {
		ConfigurableApplicationContext context = SpringApplication.run(Application.class, args);

		EmployeeRepository repository = context.getBean(EmployeeRepository.class);

		Employee emp = new Employee();
		
		emp.setEmpName("Mohan");
		emp.setDept("Sales");
		emp.setEmpGender("Male");
		
		emp = repository.save(emp);
		
		System.out.println("record inserted...");
		
	}
}










