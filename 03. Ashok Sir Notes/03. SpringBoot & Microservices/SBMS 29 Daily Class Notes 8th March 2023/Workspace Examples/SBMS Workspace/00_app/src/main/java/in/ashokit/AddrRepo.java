package in.ashokit;

import java.io.Serializable;

import org.springframework.data.jpa.repository.JpaRepository;

public interface AddrRepo extends JpaRepository<Address, Serializable>{

}
