package in.ashokit.entity;

import java.io.Serializable;

import javax.persistence.Embeddable;

import lombok.Data;

@Data
@Embeddable
public class AccountPK implements Serializable{

	private Long accNum;

	private String accType;

}











