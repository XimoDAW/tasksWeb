import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ModifyPositComponent } from './modify-posit.component';

describe('ModifyPositComponent', () => {
  let component: ModifyPositComponent;
  let fixture: ComponentFixture<ModifyPositComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ModifyPositComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ModifyPositComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
