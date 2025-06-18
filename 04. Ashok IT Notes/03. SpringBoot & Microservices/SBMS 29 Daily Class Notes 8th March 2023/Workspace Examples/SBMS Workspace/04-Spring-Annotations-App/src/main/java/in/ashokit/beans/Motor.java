package in.ashokit.beans;

import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Component;

@Component
@Scope(value="prototype")
public class Motor {

	public Motor() {
		System.out.println("Motor :: Constructor");
	}
}