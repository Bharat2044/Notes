package in.ashokit.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import in.ashokit.entity.Book;

public interface BookRepository 
		extends JpaRepository<Book, Integer>{

}
