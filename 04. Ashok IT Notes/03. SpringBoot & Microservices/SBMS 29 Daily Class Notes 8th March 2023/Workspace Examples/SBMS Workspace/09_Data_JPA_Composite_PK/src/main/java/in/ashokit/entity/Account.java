package in.ashokit.entity;

import javax.persistence.EmbeddedId;
import javax.persistence.Entity;

@Entity
public class Account {

	private String holderName;
	private String branch;

	@EmbeddedId
	private AccountPK accountPk;

	public String getHolderName() {
		return holderName;
	}

	public void setHolderName(String holderName) {
		this.holderName = holderName;
	}

	public String getBranch() {
		return branch;
	}

	public void setBranch(String branch) {
		this.branch = branch;
	}

	public AccountPK getAccountPk() {
		return accountPk;
	}

	public void setAccountPk(AccountPK accountPk) {
		this.accountPk = accountPk;
	}

	@Override
	public String toString() {
		return "Account [holderName=" + holderName + ", branch=" + branch + ", accountPk=" + accountPk + "]";
	}

}
