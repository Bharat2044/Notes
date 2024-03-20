package in.ashokit.repository;

import javax.transaction.Transactional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;

import in.ashokit.entity.Student;

//@Repository
public interface StudentRepository extends JpaRepository<Student, Integer> {
	
	@Query("update Student set gender=:gender where id=:sid")
	@Modifying
	@Transactional
	public Integer updateStudent(Integer sid, String gender);

}