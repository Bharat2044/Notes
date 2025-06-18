import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent {
  name: string = "suresh";
  price = 25;
  isDisabled = false
  myClass=true
  fun()
  {
    if (this.myClass)
      this.myClass = false
    else
      this.myClass=true
  }
}
