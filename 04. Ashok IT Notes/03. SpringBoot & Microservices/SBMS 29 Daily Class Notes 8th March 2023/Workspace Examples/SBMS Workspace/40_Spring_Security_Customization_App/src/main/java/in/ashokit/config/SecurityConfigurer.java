package in.ashokit.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
@EnableWebSecurity
public class SecurityConfigurer {

	@Bean
	public SecurityFilterChain securityFilter(HttpSecurity http) throws Exception {
		
		// logic to customize security in our app
		
		http.authorizeHttpRequests( (request) -> request
						.antMatchers("/","/login-check", "/contact", "/swagger-ui.html").permitAll()
						.anyRequest().authenticated()
				).formLogin();
		
		return http.build();
	}
}







