package in.ashokit.rest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.env.Environment;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class GreetRestController {

	@Autowired
	private Environment env;

	@GetMapping("/greet")
	public String greetMsg() {

		// in which server our app is running, get that server port number
		String port = env.getProperty("server.port");

		return "Good Evening (" + port + ")";
	}
}
