import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  myQuote: any;
   constructor(public hc: HttpClient) {
     this.hc.get('http://api.quotable.io/random')
       .subscribe(
         (val) => this.myQuote=val
       )
   }
}
