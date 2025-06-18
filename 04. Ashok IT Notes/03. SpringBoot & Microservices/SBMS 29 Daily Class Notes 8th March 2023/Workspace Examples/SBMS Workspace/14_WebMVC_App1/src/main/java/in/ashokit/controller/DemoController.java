package in.ashokit.controller;

import java.time.LocalDate;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class DemoController {

	@GetMapping("/date")
	public ModelAndView getTodayDate() {

		ModelAndView mav = new ModelAndView();

		LocalDate now = LocalDate.now();

		String msgTxt = "Today's Date Is :: " + now;

		mav.addObject("msg", msgTxt);

		mav.setViewName("index");

		return mav;
	}
}
