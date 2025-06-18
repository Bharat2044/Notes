package in.ashokit.test;

import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

import in.ashokit.AppConfig;

public class App {

	public static void main(String[] args) {

		ApplicationContext ctx = 
				new AnnotationConfigApplicationContext(AppConfig.class);
	}

}
