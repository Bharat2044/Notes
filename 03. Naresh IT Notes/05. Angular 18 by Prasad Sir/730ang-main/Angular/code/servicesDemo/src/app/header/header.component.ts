import { Component } from '@angular/core';
import { CountCommonProductService } from '../count-common-product.service';
@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrl: './header.component.css'
})
export class HeaderComponent {
  c = 0;
  constructor(private cs:CountCommonProductService){}
  getData()
   {
    this.c = this.cs.getC()
    this.cs.printProduct()
   }
}
