package in.ashokit;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/welcome")
public class WelcomeController {

	// http://localhost:8081/welcome/hello

	@GetMapping(value = { "/hi", "/hello", "/" })
	public String welcomeMsg(Model model) {
		model.addAttribute("msg", "Hello, Good Evening");
		return "index";
	}
}
