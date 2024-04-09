import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DeletePositComponent } from './delete-posit.component';

describe('DeletePositComponent', () => {
  let component: DeletePositComponent;
  let fixture: ComponentFixture<DeletePositComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DeletePositComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DeletePositComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
