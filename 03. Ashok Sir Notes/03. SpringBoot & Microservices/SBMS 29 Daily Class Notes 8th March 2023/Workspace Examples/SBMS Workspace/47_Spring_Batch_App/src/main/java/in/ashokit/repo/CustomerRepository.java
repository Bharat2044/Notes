package in.ashokit.repo;

import java.io.Serializable;

import org.springframework.data.jpa.repository.JpaRepository;

import in.ashokit.entity.Customer;

public interface CustomerRepository extends JpaRepository<Customer, Serializable> {

}
