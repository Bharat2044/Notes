package in.ashokit.dao;

import org.springframework.beans.factory.InitializingBean;
import org.springframework.stereotype.Component;

@Component("userdao")
public class UserDao implements InitializingBean {

	@Override
	public void afterPropertiesSet() throws Exception {
		System.out.println("get data from db...");
		System.out.println("store data into redis...");
	}

}
