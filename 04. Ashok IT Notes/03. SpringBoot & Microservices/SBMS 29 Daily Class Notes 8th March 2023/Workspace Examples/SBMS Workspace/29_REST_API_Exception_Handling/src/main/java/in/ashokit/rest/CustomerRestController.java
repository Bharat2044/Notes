package in.ashokit.rest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import in.ashokit.service.CustomerService;

@RestController
public class CustomerRestController {

	@Autowired
	private CustomerService service;

	@GetMapping("/customer/{customerId}")
	public String getCustomerName(@PathVariable Integer customerId) throws Exception {
		return service.getCustomerNameById(customerId);
	}
	
}
