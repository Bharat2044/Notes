import { Component } from '@angular/core';
import { CartService } from '../cart.service';
@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrl: './products.component.css'
})
export class ProductsComponent {
  products:any[]=[]
  constructor(private cs: CartService) {
    this.cs.getData().subscribe((res:any)=>this.products=res.products)
  }
}
