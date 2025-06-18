package in.ashokit.test;

import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

import in.ashokit.AppConfig;

public class Test {
	
	public static void main(String[] args) {
		
		ApplicationContext ctxt = 
				new AnnotationConfigApplicationContext(AppConfig.class);
		
	}
}
