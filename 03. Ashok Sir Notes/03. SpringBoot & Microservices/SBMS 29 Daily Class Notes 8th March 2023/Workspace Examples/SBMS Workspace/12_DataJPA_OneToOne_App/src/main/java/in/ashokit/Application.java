package in.ashokit;

import java.time.LocalDate;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ConfigurableApplicationContext;

import in.ashokit.entity.Passport;
import in.ashokit.entity.Person;
import in.ashokit.repository.PassportRepository;
import in.ashokit.repository.PersonRepository;

@SpringBootApplication
public class Application {

	public static void main(String[] args) {
		ConfigurableApplicationContext context = SpringApplication.run(Application.class, args);

		PersonRepository personRepo = context.getBean(PersonRepository.class);

		PassportRepository passportRepo = context.getBean(PassportRepository.class);

		/*Person person = new Person();
		person.setPersonName("Ashok");
		person.setPersonGender("Male");

		Passport passport = new Passport();
		passport.setPassportNum("KV7979HKI");
		passport.setIssuedDate(LocalDate.now());
		passport.setExpiryDate(LocalDate.now().plusYears(10));

		person.setPassport(passport);
		passport.setPerson(person);
		
		personRepo.save(person);*/
		
		//personRepo.findById(1);
		
		personRepo.deleteById(1);

	}
}
