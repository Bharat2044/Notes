package in.ashokit.rest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import in.ashokit.models.AuthenticationRequest;
import in.ashokit.models.AuthenticationResponse;
import in.ashokit.security.MyUserDetailsService;
import in.ashokit.util.JwtUtil;

@RestController
public class MyRestController {

	@Autowired
	private AuthenticationManager authManager;

	@Autowired
	private MyUserDetailsService service;

	@Autowired
	private JwtUtil jwtUtil;

	@PostMapping("/authenticate")
	public ResponseEntity<?> authentication(@RequestBody AuthenticationRequest request) throws Exception {
		try {
			authManager.authenticate(
					new UsernamePasswordAuthenticationToken(request.getUsername(), request.getPassword()));

		} catch (Exception e) {
			throw new Exception("Invalid Credentials");
		}

		UserDetails userDetails = service.loadUserByUsername(request.getUsername());

		String jwt = jwtUtil.generateToken(userDetails);

		AuthenticationResponse response = new AuthenticationResponse(jwt);

		return new ResponseEntity<>(response, HttpStatus.OK);

	}

	@GetMapping("/hello")
	public String sayHello() {
		return "Hello World";
	}

}
