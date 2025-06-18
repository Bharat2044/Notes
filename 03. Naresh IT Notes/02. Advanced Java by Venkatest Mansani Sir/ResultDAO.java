package mvc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class ResultDAO {
	Result r;
	Result getResult(int hno)
	{
		try {
			Class.forName("oracle.jdbc.driver.OracleDriver");
			Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","tiger");
			PreparedStatement pstmt=con.prepareStatement("select * from result where hno=?");
			pstmt.setInt(1, hno);
			ResultSet rs=pstmt.executeQuery();
			rs.next();
			r=new Result();
			r.setHno(rs.getInt(1));
			r.setName(rs.getString(2));
			r.setMarks(rs.getInt(3));
			return r;
		} catch (ClassNotFoundException | SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return r;
	}
}
