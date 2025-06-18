import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  pokemonName: string = '';
  pokemonDetails: any;
  pokeArray:any[]=[]
  constructor(private hc: HttpClient) { }
  getData()
  {
    this.hc.get(`https://pokeapi.co/api/v2/pokemon/${this.pokemonName}`)
      .subscribe((val) => {
        this.pokemonDetails = val;
        this.pokeArray.push(this.pokemonDetails);
        console.log(this.pokeArray)
      })
  }
 
}
