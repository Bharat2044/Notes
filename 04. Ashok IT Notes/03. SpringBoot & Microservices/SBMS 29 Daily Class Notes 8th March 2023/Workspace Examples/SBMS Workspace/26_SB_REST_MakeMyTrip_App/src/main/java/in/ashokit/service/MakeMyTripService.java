package in.ashokit.service;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Service;
import org.springframework.web.reactive.function.BodyInserters;
import org.springframework.web.reactive.function.client.WebClient;

import in.ashokit.request.Passenger;
import in.ashokit.response.Ticket;

@Service
public class MakeMyTripService {

	@Value("${irctc.endpoint.book.ticket}")
	private String IRCTC_BOOK_TICKET_URL;

	@Value("${irctc.endpoint.get.ticket}")
	private String IRCTC_GET_TICKET_URL;

	public Ticket getTicketInfo(String ticketId) {
		
		 WebClient webClient = WebClient.create(); // get WeClient instance
		
		 Ticket ticket = webClient.get() // represents HTTP GET request
								  .uri(IRCTC_GET_TICKET_URL, ticketId) // ENDPOINT URL
								  .accept(MediaType.APPLICATION_JSON)
								  .retrieve() // take resp from response body
								  .bodyToMono(Ticket.class) // bind resp body data to java obj
								  .block(); // make sync call
		 if(ticket!=null) { 
			 return ticket;
		 }

		return null;
	}

	public Ticket processTicketBooking(Passenger passenger) {
		
		 WebClient webClient = WebClient.create(); // get WeClient instance
		 
		 Ticket ticket = webClient.post()
		 		  				  .uri(IRCTC_BOOK_TICKET_URL)
		 		  				  .body(BodyInserters.fromValue(passenger))
		 		  				  .header("Content-Type","application/json")
		 		  				  .accept(MediaType.APPLICATION_JSON)
		 		  				  .retrieve()
		 		  				  .bodyToMono(Ticket.class)
		 		  				  .block();
		 if(ticket!=null) { 
			 return ticket;
		 }
		return null;
	}
}












