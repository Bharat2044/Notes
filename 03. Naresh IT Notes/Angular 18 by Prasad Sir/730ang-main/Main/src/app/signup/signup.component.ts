import { Component } from '@angular/core';
import { AuthService } from '../auth.service';
@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrl: './signup.component.css'
})
export class SignupComponent {
  em: any; pwd: any;
  constructor(private as: AuthService) { }
  signup() {
    this.as.register(this.em,this.pwd).then((res)=>console.log(res))
  }
}
