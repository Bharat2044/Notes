import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BooksChildComponent } from './books-child.component';

describe('BooksChildComponent', () => {
  let component: BooksChildComponent;
  let fixture: ComponentFixture<BooksChildComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [BooksChildComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BooksChildComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
