import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TunayoHeaderComponent } from './tunayo-header/tunayo-header.component';



@NgModule({
  declarations: [TunayoHeaderComponent],
  imports: [
    CommonModule
  ],
  exports:[
    TunayoHeaderComponent
  ]
})
export class SharedModule { }
