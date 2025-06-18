import { TestBed } from '@angular/core/testing';

import { CountCommonProductService } from './count-common-product.service';

describe('CountCommonProductService', () => {
  let service: CountCommonProductService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CountCommonProductService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
