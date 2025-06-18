import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'starRating'
})
export class StarRatingPipe implements PipeTransform {

  transform(rating: number, maxStars: number=5): string {
    const fullStar = '⭐'
    const halfStar = '\u2605';
    const emptyStar = '\u2606;';
    const fullStars = Math.floor(rating);
    const hasHAlfStar = rating % 1 !== 0;
    const emptyStars = maxStars - fullStars - (hasHAlfStar ? 1 : 0)
    console.log(fullStar.repeat(fullStars), halfStar, emptyStar);
    return fullStar.repeat(fullStars) + emptyStar.repeat(emptyStars);

  }

}
