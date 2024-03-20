package in.ashokit.rest;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class BankRestController {

	@GetMapping("/balance")
	public String balance() {
		// logic to check balance
		return "Your Balance :: 7898.90 INR";
	}

	@GetMapping("/transfer")
	public String amtTransfer() {
		// logic to check balance
		return "Your Amount Transfer Successfull";
	}

	@GetMapping("/login-check")
	public String login() {
		// logic to check balance
		return "Your Login Success";
	}

	@GetMapping("/contact")
	public String getContactInfo() {
		return "Contact US :: abc@bank.com";
	}

}
