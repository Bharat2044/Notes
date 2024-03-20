<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
	<h2>Get Your Ticket Info</h2>
	<form action="searchTicket">
		Ticket ID : <input type="text" name="ticketId"> <input
			type="submit" value="Search" />
	</form>
	<hr />

	<table>
		<tr>
			<td>Ticket ID :</td>
			<td>${ticket.ticketId}</td>
		</tr>
		<tr>
			<td>Ticket Status :</td>
			<td>${ticket.ticketStatus}</td>
		</tr>
		<tr>
			<td>Ticket Cost :</td>
			<td>${ticket.tktCost}</td>
		</tr>
		<tr>
			<td>From :</td>
			<td>${ticket.from}</td>
		</tr>
		<tr>
			<td>To :</td>
			<td>${ticket.to}</td>
		</tr>
		<tr>
			<td>Train Number :</td>
			<td>${ticket.trainNum}</td>
		</tr>
	</table>

	<a href="/">Go Back</a>

</body>
</html>