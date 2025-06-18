package in.ashokit.repo;

import java.util.List;

import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;

import in.ashokit.entity.Book;

public interface BookRepository extends CrudRepository<Book, Integer> {

	@Query(value = "select * from book", nativeQuery = true)
	public List<Book> getAllBooks();
	
	@Query("from Book")
	public List<Book> getBooks();

}










