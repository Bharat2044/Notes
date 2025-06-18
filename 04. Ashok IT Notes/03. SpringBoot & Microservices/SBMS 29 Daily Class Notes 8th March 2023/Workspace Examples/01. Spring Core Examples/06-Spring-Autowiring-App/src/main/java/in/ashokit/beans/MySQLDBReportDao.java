package in.ashokit.beans;

import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Repository;

@Repository("mysqlDao")
public class MySQLDBReportDao implements ReportDao {

	public void getData() {
		System.out.println("getting data from mysql db...");
	}
}
