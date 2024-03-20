package in.ashokit.rest;

import java.util.Random;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.netflix.hystrix.contrib.javanica.annotation.HystrixCommand;
import com.netflix.hystrix.contrib.javanica.annotation.HystrixProperty;

@RestController
public class DataRestController {

	@GetMapping("/data")
	@HystrixCommand(
			fallbackMethod="getDataFromDB",
			commandProperties= {
				@HystrixProperty(name="circuitBreaker.requestVolumeThreshold", value="5"),
				@HystrixProperty(name="circuitBreaker.sleepWindowInMilliseconds",value="10000")
			}
	)
	public String getDataFromRedis() {
		System.out.println("**Redis() method called**");
		
		if (new Random().nextInt(10) <= 10) {
			throw new RuntimeException("Redis Server Is Down");
		}
		// logic to access data from redis
		return "data accessed from redis (main logic) ....";
	}

	public String getDataFromDB() {
		System.out.println("**DB() method called**");
		// logic to access data from db
		return "data accessed from database (fall back logic) ....";
	}
}
