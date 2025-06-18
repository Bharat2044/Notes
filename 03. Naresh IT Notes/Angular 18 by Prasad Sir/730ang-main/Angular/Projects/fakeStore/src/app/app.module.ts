import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SquarePipe } from './square.pipe';
import { PowerPipe } from './power.pipe';

@NgModule({
  declarations: [
    AppComponent,
    SquarePipe,
    PowerPipe
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
