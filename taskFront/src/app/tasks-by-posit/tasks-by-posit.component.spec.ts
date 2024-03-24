import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TasksByPositComponent } from './tasks-by-posit.component';

describe('TasksByPositComponent', () => {
  let component: TasksByPositComponent;
  let fixture: ComponentFixture<TasksByPositComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TasksByPositComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TasksByPositComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
