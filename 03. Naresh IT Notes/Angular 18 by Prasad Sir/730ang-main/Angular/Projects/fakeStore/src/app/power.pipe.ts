import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'power'
})
export class PowerPipe implements PipeTransform {

  transform(value: number, powerValue:number): number {
    return Math.pow(value,powerValue);
  }

}
