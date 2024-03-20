package in.ashokit.beans;

import org.springframework.stereotype.Repository;

@Repository
public class UserDao {
	
	public UserDao() {
		System.out.println("UserDao :: Constructor");
	}
}
