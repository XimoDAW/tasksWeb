import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddPositComponent } from './add-posit.component';

describe('AddPositComponent', () => {
  let component: AddPositComponent;
  let fixture: ComponentFixture<AddPositComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddPositComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AddPositComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
