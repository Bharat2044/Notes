import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  movieName: string = '';
  movieURL: string = '';
  mn = ''; mu = '';
  isShow = false;
  update()
  {
    this.isShow=true
    this.movieName = this.mn;
    this.movieURL=this.mu
  }
}
