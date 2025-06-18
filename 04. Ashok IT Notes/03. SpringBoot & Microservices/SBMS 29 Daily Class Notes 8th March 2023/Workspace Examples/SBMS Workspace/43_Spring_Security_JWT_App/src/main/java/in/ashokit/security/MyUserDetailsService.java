package in.ashokit.security;

import java.util.ArrayList;

import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.stereotype.Service;

@Service
public class MyUserDetailsService implements UserDetailsService{
	
	@Override
	public UserDetails loadUserByUsername(String s) {
		return new User("admin","$2a$12$LKrFNAHNdv7r2Lx7xeg9HuB47Hq8G1LSKXur8icj.LIE8gBK8ftbO",new ArrayList<>());
	}

}
