import { Component,Input } from '@angular/core';

@Component({
  selector: 'app-books-child',
  templateUrl: './books-child.component.html',
  styleUrl: './books-child.component.css'
})
export class BooksChildComponent {
  @Input() count!: number;
  c1 = 0;
  incr() {
    this.c1++;
  }
  display()
  {
    alert("i'm from child")
  }
}
