import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class CountCommonProductService {
  c = 0;
  pro1: any;
  constructor() { }
  incr()
  {
    this.c++;
  }
  getProduct(obj:any)
  {
    this.pro1 = obj;
  }
  getC()
  {
    return this.c;
  }
  printProduct()
  {
    alert(this.pro1.name+" is added successfully")
  }
}
