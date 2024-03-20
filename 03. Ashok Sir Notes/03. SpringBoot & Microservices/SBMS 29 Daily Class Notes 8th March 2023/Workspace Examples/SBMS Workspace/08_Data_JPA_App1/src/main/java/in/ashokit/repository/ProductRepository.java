package in.ashokit.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.jpa.repository.query.Procedure;
import org.springframework.transaction.annotation.Transactional;

import in.ashokit.entity.Product;

public interface ProductRepository extends JpaRepository<Product, Integer>{
	
	@Query(value="call getABC()", nativeQuery=true)
	public List<Product> getAllProducts();

}
