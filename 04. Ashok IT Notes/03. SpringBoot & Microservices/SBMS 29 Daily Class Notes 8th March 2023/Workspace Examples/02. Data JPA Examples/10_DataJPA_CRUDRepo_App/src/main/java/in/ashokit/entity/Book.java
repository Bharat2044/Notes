package in.ashokit.entity;

import javax.persistence.Entity;
import javax.persistence.Id;

import lombok.Data;

@Data
@Entity
public class Book {

	@Id
	private Integer bookId;
	private String bookName;
	private Double bookPrice;
}