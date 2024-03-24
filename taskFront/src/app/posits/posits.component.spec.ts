import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PositsComponent } from './posits.component';

describe('PositsComponent', () => {
  let component: PositsComponent;
  let fixture: ComponentFixture<PositsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PositsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PositsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
