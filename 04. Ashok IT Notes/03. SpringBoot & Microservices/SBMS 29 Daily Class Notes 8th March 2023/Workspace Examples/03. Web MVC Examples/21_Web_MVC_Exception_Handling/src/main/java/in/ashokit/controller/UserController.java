package in.ashokit.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class UserController {
	

	@GetMapping("/user")
	public String getWishMsg(Model model) {
		String msgTxt = "Good Evening..!!";
		int i = 10/0;
		model.addAttribute("msg", msgTxt);
		return "index";
	}
	
}














