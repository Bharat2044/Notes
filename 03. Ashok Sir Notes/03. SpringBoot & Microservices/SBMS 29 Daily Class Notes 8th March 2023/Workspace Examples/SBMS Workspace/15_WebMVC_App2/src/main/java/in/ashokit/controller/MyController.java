package in.ashokit.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class MyController {
	
	@GetMapping("/welcome")
	public ModelAndView getWelcomeMsg(@RequestParam String name) {

		String msgTxt = name + ", Welcome to Ashok IT..";

		ModelAndView mav = new ModelAndView();
		mav.addObject("msg", msgTxt);

		mav.setViewName("index");

		return mav;
	}
	
	
	@GetMapping("/greet")
	public String getGreetMsg(@RequestParam String name, Model model) {
		
		model.addAttribute("msg", name+", Good Evening...!!");
		
		return "index";
	}
}
