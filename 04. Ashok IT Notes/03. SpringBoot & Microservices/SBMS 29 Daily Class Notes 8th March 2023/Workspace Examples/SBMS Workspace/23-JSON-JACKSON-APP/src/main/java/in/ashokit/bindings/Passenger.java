package in.ashokit.bindings;

public class Passenger {

	private String name;
	private String from;
	private String to;
	private String gender;

	private Address addr;

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getFrom() {
		return from;
	}

	public void setFrom(String from) {
		this.from = from;
	}

	public String getTo() {
		return to;
	}

	public void setTo(String to) {
		this.to = to;
	}

	public String getGender() {
		return gender;
	}

	public void setGender(String gender) {
		this.gender = gender;
	}

	public Address getAddr() {
		return addr;
	}

	public void setAddr(Address addr) {
		this.addr = addr;
	}

	@Override
	public String toString() {
		return "Passenger [name=" + name + ", from=" + from + ", to=" + to + ", gender=" + gender + ", addr=" + addr
				+ "]";
	}

}
