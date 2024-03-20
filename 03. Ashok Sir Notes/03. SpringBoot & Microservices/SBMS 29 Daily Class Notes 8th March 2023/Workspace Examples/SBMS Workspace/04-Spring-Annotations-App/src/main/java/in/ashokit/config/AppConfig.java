package in.ashokit.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

import in.ashokit.beans.Robot;

@Configuration
@ComponentScan(basePackages = { "in.ashokit" , "com.ibm" })
public class AppConfig {

	public AppConfig() {
		System.out.println("AppConfig :: Constructor");
	}

	@Bean
	public Robot buildRobot() {
		//logic
		Robot r = new Robot();
		return r;
	}
}