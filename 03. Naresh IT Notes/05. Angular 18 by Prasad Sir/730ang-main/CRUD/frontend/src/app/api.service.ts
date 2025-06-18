import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private hc: HttpClient) { }
  getMovies()
  {
    return this.hc.get('http://localhost:3000/movies');
  }
  deleteData(id:any)
  {
    return this.hc.delete(`http://localhost:3000/movies/${id}`);
  }
  postData(obj: any) {
    return this.hc.post('http://localhost:3000/movies',obj);
  }
  putData(obj: any)
  {
    return this.hc.put(`http://localhost:3000/movies/${obj.id}`,obj);
  }
}
