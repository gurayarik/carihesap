import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <div class="container">
      <h1>Hüseyin UÇAR - Cari Kart Yönetimi</h1>
      <app-cari-kart-form></app-cari-kart-form>
      <app-cari-kart-list></app-cari-kart-list>
    </div>
  `,
  styles: [
    `
      .container {
        max-width: 900px;
        margin: 40px auto;
        padding: 24px;
        font-family: Arial, sans-serif;
      }
    `,
  ],
})
export class AppComponent {}
