package in.ashokit;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@Configuration
@ComponentScan
public class AppConfig {

	public AppConfig() {
		System.out.println("AppConfig::Constructor");
	}

	@Bean
	public Engine getEngine() {
		Engine eng = new Engine();
		// logic
		return eng;
	}
}






