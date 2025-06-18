import { Component, OnInit,OnChanges,DoCheck,AfterContentInit,AfterContentChecked,AfterViewInit,AfterViewChecked } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent implements OnInit,OnChanges,DoCheck {
  title = 'lifeCycle';
  count = 0;
  constructor() {
    console.log("constructor started")
  }
  incr() {
    this.count++;
  }
  ngOnChanges() {
    console.log("on changes triggered")
  }
  ngOnInit() {
    console.log('Init started')
  }
  ngDoCheck() {
    console.log("do check called") /* it will run when changes happen in component*/
  }
  ngAfterContentInit() {
    console.log("AfterContentInit called")
  }
  ngAfterContentChecked()
  {
    console.log(' ngAfterContentChecked called');

  }
  ngAfterViewInit() {
       console.log('  ngAfterViewInit called');
  }
  ngAfterViewChecked() {
     console.log('  ngAfterViewChecked called');
  }
  ngOnDestroy()
  {
    console.log('destroy called')
  }

}
