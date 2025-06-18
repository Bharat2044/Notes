import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent {
  j: any;
  constructor(private hc: HttpClient) {
    this.hc.get('https://official-joke-api.appspot.com/random_joke')
      .subscribe(
        (data) => {
          this.j= data;
          console.log(this.j)
        })
  }
  }
 

