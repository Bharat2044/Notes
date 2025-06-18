import { Component } from '@angular/core';
import { ApiService } from './api.service';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent {
  movies: any[] = [];
  mTitle: string = '';
  mYear!: number;
  updateValue = {
    Title: '',
    Year: '',
  };
  isUpdate = false;
  constructor(private api: ApiService) {
    this.api.getMovies().subscribe((val: any) => (this.movies = val));
  }
  deleteMovie(id: any) {
    let x = window.confirm('Are you sure to delete?');
    if (x) {
      this.api.deleteData(id).subscribe((val) => {
        console.log(val);
        window.location.reload();
      });
    }
  }
  sendData() {
    let data = {
      Title: this.mTitle,
      Year: this.mYear,
    };
    this.api.postData(data).subscribe((val) => {
      console.log(val);
      window.location.reload();
    });
  }
  update(x: any) {
    this.updateValue = x;
    this.isUpdate = true
  }
  updateData()
  {
    this.api.putData(this.updateValue)
      .subscribe((val) => {
        console.log(val);
        window.location.reload()
      })
  }
}
