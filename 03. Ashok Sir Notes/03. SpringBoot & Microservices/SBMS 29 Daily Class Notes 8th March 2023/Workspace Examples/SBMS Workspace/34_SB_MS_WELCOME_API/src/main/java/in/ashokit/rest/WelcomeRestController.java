package in.ashokit.rest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.env.Environment;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import in.ashokit.GreetFiegnClient;

@RestController
public class WelcomeRestController {

	@Autowired
	private GreetFiegnClient greetClient;

	@Autowired
	private Environment env;

	@GetMapping("/welcome")
	public String getWelcomeMsg() {

		String port = env.getProperty("server.port");

		String welcomeMsg = "Welcome to Ashok IT (" + port + ")";

		String greetMsg = greetClient.invokGreetApi();

		return greetMsg + ", " + welcomeMsg;
	}
}
