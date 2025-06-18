import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class CartService {

  constructor(private hc: HttpClient) { 
    
  }
  getData() {
    return this.hc.get('https://dummyjson.com/products');
  }
  getSpecificData(id: any) {
    return this.hc.get(`https://dummyjson.com/products/${id}`);
  }
}
