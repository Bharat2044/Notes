package in.ashokit.entity;

import javax.persistence.EmbeddedId;
import javax.persistence.Entity;
import javax.persistence.Table;

import lombok.Data;

@Data
@Entity
@Table(name="account_tbl")
public class Account {

	private String holderName;

	private String branch;
	
	@EmbeddedId
	private AccountPK accountPk;

}



