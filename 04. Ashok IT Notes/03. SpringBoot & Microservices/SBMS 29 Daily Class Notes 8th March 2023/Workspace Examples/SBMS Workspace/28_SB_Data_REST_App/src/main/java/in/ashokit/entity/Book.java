package in.ashokit.entity;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

import lombok.Data;

@Entity
@Table(name = "book_tbl")
@Data
public class Book {

	@Id
	private Integer id;
	private String name;
	private Double price;

}
