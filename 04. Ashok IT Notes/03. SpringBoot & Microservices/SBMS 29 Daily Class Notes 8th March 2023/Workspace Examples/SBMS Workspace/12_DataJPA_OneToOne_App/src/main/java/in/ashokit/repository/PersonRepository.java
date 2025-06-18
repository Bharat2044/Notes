package in.ashokit.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import in.ashokit.entity.Person;

public interface PersonRepository extends JpaRepository<Person, Integer>{

}
