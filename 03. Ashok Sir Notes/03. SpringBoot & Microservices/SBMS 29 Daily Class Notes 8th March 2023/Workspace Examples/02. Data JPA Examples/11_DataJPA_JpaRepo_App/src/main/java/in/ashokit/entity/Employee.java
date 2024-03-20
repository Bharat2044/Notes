package in.ashokit.entity;

import java.time.LocalDate;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.Table;

import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@Table(name = "emp_tbl")
@Data
@AllArgsConstructor
@NoArgsConstructor
public class Employee {

	@Id
	@GeneratedValue
	private Integer empId;
	private String empName;
	private Double empSalary;
	private String empGender;
	private String dept;

	@CreationTimestamp
	@Column(name = "date_created", updatable = false)
	private LocalDate dateCreated;

	@UpdateTimestamp
	@Column(name = "last_updated", insertable = false)
	private LocalDate lastUpdated;

}
