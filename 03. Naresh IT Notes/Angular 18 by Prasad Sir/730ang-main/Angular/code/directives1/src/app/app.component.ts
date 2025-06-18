import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  isShow = false;
  fun1()
  {
    this.isShow=true
  }
  fun2() {
    this.isShow=false
  }
  isAdmin = false;
  day: number = 1;
  fruits=["apple","mango","banana","papaya"]







}
