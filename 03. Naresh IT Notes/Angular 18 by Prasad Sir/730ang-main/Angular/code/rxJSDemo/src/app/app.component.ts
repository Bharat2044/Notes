import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { from, Observable, of, Subject ,map} from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'rxJSDemo';
  obs!: any;
  msg!: any;
  subj= new Subject()
  constructor(private hc:HttpClient) {
    this.obs = new Observable((sub) => {
      sub.next(1);
      sub.next(10);
      sub.error("my error")
      sub.next(100);
    
            sub.complete();
      sub.next(1000);
    });
    this.msg = this.hc.get('https://official-joke-api.appspot.com/random_joke');
    this.subj.subscribe({
      next: (val) => console.log(val),
      error: () => console.log("error"),
      complete: () => console.log("completed")
    });
    of(5, 6, 7, 9).subscribe((val) => console.log(val));
    of(1, 2, 3).pipe(map((val)=> val * 2)).subscribe(val=>console.log(val));
    from([ 5, 8, 10, 11 ]).subscribe((val) => console.log(val));
  }
  ngOnInit()
  {
    this.obs.subscribe((val: any) => console.log(val));
    this.subj.next(25);
    this.subj.next(55);
    this.subj.complete()
  }
  }
