import { Component, ViewChild } from '@angular/core';
import { BooksChildComponent } from '../books-child/books-child.component';

@Component({
  selector: 'app-books',
  templateUrl: './books.component.html',
  styleUrl: './books.component.css'
})
export class BooksComponent {
  @ViewChild(BooksChildComponent) child!:BooksChildComponent
  c = 0;
  k = 0;
  fun()
  {
    this.child.display()
  }
  incr()
  {
    this.c++;
  }

  ngAfterViewInit()
  {
    this.k= this.child.c1
  }

}
