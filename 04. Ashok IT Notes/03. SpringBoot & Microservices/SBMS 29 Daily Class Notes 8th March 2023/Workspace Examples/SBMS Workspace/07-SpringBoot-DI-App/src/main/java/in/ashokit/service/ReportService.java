package in.ashokit.service;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import in.ashokit.dao.IReportDao;
import in.ashokit.dao.ReportDaoImpl;

@Service
public class ReportService {
	
	@Value("${report.type}")
	private String type;
	
	private IReportDao reportDao;

	public ReportService(ReportDaoImpl dao) {
		this.reportDao = dao;
	}

	public void printName(Integer userId) {
		System.out.println("Report Type :: "+ type);
		String nameById = reportDao.getNameById(userId);
		System.out.println(nameById);
	}
}
