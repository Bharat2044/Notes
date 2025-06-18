package in.ashokit.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class DemoController {
	
	@GetMapping("/demo")
	@ResponseBody
	public String getDemoMsg() {
		String msg = "Good Evening..!!";
		String s = null;
		s.length();
		return msg;
	}
}
