import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PositComponent } from './posit.component';

describe('PositComponent', () => {
  let component: PositComponent;
  let fixture: ComponentFixture<PositComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PositComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PositComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
