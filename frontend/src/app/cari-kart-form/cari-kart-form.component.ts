import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { CariKartService } from '../services/cari-kart.service';

@Component({
  selector: 'app-cari-kart-form',
  templateUrl: './cari-kart-form.component.html',
  styleUrls: ['./cari-kart-form.component.css'],
})
export class CariKartFormComponent {
  form: FormGroup;
  isSubmitting = false;

  constructor(private fb: FormBuilder, private service: CariKartService) {
    this.form = this.fb.group({
      cari_kodu: ['', Validators.required],
      unvan1: ['', Validators.required],
      unvan2: [''],
      yurt_ici_dis: ['YURT İÇİ'],
      cari_turu: ['TOPTAN'],
      sahis_tuzel: ['TÜZEL'],
      tc_no_vergi_no: [''],
      vergi_dairesi: [''],
      il: [''],
      ilce: [''],
      mahalle: [''],
      cadde: [''],
      sokak: [''],
      kapino: [''],
      posta_kodu: [''],
      bolge: [''],
      ulke: ['TÜRKİYE'],
      sorumlu_kisi: [''],
      cep_telefon: [''],
      email: [''],
      yetkili_kisi: [''],
      yetkili_telefon: [''],
      web_adresi: [''],
      bakiye: [0, Validators.required],
      aciklama: [''],
    });
  }

  submit(): void {
    if (this.form.invalid) {
      return;
    }

    this.isSubmitting = true;
    this.service.create(this.form.value).subscribe({
      next: () => {
        this.form.reset({
          cari_kodu: '',
          unvan1: '',
          unvan2: '',
          yurt_ici_dis: 'YURT İÇİ',
          cari_turu: 'TOPTAN',
          sahis_tuzel: 'TÜZEL',
          tc_no_vergi_no: '',
          vergi_dairesi: '',
          il: '',
          ilce: '',
          mahalle: '',
          cadde: '',
          sokak: '',
          kapino: '',
          posta_kodu: '',
          bolge: '',
          ulke: 'TÜRKİYE',
          sorumlu_kisi: '',
          cep_telefon: '',
          email: '',
          yetkili_kisi: '',
          yetkili_telefon: '',
          web_adresi: '',
          bakiye: 0,
          aciklama: '',
        });
        this.isSubmitting = false;
        window.dispatchEvent(new Event('cariKartCreated'));
      },
      error: () => {
        this.isSubmitting = false;
      },
    });
  }
}
