import { Component } from '@angular/core';
import { CountCommonProductService } from '../count-common-product.service';
@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrl: './product.component.css',
})
export class ProductComponent {
  //Dependency Injection (DI) is a fundamental concept in Angular that allows you to provide dependencies to classes (like components, services, and directives) without them having to create those dependencies themselves.
  // you achieve it by creating an instance of service in the component constructor parameters
  pro = {
    img: 'https://5.imimg.com/data5/SELLER/Default/2022/11/YV/ZF/YO/116453489/white-casual-shoes-for-men.jpg',
    name: 'Shoes',
    price: 200,
  };
  constructor(private cs: CountCommonProductService) {}
  increase() {
    this.cs.incr();
    this.cs.getProduct(this.pro)
  }
}
