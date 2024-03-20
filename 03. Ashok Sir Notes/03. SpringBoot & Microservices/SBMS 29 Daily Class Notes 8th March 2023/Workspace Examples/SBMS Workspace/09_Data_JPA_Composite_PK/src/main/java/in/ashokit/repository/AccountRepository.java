package in.ashokit.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import in.ashokit.entity.Account;
import in.ashokit.entity.AccountPK;

public interface AccountRepository extends JpaRepository<Account, AccountPK> {

}