package in.ashokit.beans;

import org.springframework.stereotype.Service;

@Service
public class ReportService {

	private ReportDao dao;

	public ReportService(ReportDao dao) {
		System.out.println("ReportService:: Param - Constructor");
		this.dao = dao;
	}

	public void generateReport() {
		dao.getData();
		System.out.println("Report Generated.....");
	}
}
