import { TestBed } from '@angular/core/testing';

import { PositServiceService } from './posit-service.service';

describe('PositServiceService', () => {
  let service: PositServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PositServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
