package in.ashokit.repo;

import org.springframework.data.jpa.repository.JpaRepository;

import in.ashokit.entity.Account;
import in.ashokit.entity.AccountPK;

public interface AccountRepo
		extends JpaRepository<Account, AccountPK>{
}
