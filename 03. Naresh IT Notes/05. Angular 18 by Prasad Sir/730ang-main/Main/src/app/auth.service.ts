import { Injectable } from '@angular/core';
import {AngularFireAuth} from '@angular/fire/compat/auth'
import { Router } from '@angular/router';
import {  GoogleAuthProvider } from 'firebase/auth';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private af:AngularFireAuth,private router:Router) { 
  }
  async register(em: any, pwd: any) {
    try {
      const res = await this.af.createUserWithEmailAndPassword(em, pwd)
      console.log(res);
      this.router.navigate(['/dashboard'])
    }
    catch (err) {
      console.log(err)
    }
  }
  async login(em: any, pwd: any) {
      try {
        const res = await this.af.signInWithEmailAndPassword(em, pwd);
        console.log(res);
        this.router.navigate(['/dashboard']);
      } catch (err) {
        console.log(err);
      }
  }
  async logout() {
    await this.af.signOut();
    this.router.navigate(['/login']);
  }
  get isAuthenticated() {
    return this.af.authState;
  }
  async googleLogin(){
  try {
    const provider = new GoogleAuthProvider();
    const res = await this.af.signInWithPopup(provider)
    console.log(res);
    this.router.navigate(['/dashboard']);
  }
  catch (err) {
    console.log(err)
  }
  }
}
