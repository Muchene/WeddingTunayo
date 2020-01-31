import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TunayoHeaderComponent } from './tunayo-header.component';

describe('TunayoHeaderComponent', () => {
  let component: TunayoHeaderComponent;
  let fixture: ComponentFixture<TunayoHeaderComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TunayoHeaderComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TunayoHeaderComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
