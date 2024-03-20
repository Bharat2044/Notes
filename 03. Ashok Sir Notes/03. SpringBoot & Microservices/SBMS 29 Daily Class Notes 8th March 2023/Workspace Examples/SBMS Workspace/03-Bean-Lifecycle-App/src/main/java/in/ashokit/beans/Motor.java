package in.ashokit.beans;

import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;

public class Motor {

	public Motor() {
		System.out.println("Motor :: Constructor");
	}

	@PostConstruct
	public void m1() throws Exception {
		System.out.println("motor started.....");
	}

	public void doWork() {
		System.out.println("Motor Pulling Water...");
	}

	@PreDestroy
	public void m2() throws Exception {
		System.out.println("motor stopped.....");
	}
}
