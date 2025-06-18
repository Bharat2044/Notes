import { Component } from '@angular/core';
import { AuthService } from '../auth.service';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  email: any;
  password: any;
  constructor(private as: AuthService) { }
  login() {
    this.as.login(this.email,this.password).then((res)=>console.log(res))
  }
  googlelogin() {
    this.as.googleLogin().then((res)=>console.log(res))
  }

}
