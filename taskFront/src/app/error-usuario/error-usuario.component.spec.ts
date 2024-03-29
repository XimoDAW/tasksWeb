import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ErrorUsuarioComponent } from './error-usuario.component';

describe('ErrorUsuarioComponent', () => {
  let component: ErrorUsuarioComponent;
  let fixture: ComponentFixture<ErrorUsuarioComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ErrorUsuarioComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ErrorUsuarioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
