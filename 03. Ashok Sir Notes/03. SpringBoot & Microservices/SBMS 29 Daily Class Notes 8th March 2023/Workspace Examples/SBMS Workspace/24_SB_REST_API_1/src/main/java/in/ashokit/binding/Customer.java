package in.ashokit.binding;

import javax.xml.bind.annotation.XmlRootElement;

@XmlRootElement
public class Customer {

	private String name;
	private String email;
	private String gender;

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getGender() {
		return gender;
	}

	public void setGender(String gender) {
		this.gender = gender;
	}

	@Override
	public String toString() {
		return "Customer [name=" + name + ", email=" + email + ", gender=" + gender + "]";
	}
	
	

}
