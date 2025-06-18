package in.ashokit.dto;

import lombok.Data;

@Data
public class User {

	private Integer userid;
	private String username;
	private String userEmail;
	private String pwd;
	private String gender;
	private Long phno;

}
