package in.ashokit.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import in.ashokit.reports.IReport;

@Service("reportService")
public class ReportService {

	@Autowired
	private IReport excelreport;

	public void generate() {
		System.out.println("Injected :: " + excelreport.getClass().getName());
		excelreport.generateReport();
	}
}