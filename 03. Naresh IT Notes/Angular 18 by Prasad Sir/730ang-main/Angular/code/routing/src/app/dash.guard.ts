import { CanActivateFn } from '@angular/router';

export const dashGuard: CanActivateFn = (route, state) => {
  return false
};
