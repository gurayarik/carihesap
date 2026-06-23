import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { CariKartListComponent } from './cari-kart-list/cari-kart-list.component';
import { CariKartFormComponent } from './cari-kart-form/cari-kart-form.component';

@NgModule({
  declarations: [AppComponent, CariKartListComponent, CariKartFormComponent],
  imports: [BrowserModule, HttpClientModule, FormsModule, ReactiveFormsModule],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
