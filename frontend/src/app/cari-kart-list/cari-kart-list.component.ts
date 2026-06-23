import { Component, OnDestroy, OnInit } from '@angular/core';
import { Subject, takeUntil } from 'rxjs';
import { CariKart } from '../models/cari-kart';
import { CariKartService } from '../services/cari-kart.service';

@Component({
  selector: 'app-cari-kart-list',
  templateUrl: './cari-kart-list.component.html',
  styleUrls: ['./cari-kart-list.component.css'],
})
export class CariKartListComponent implements OnInit, OnDestroy {
  kartlar: CariKart[] = [];
  private destroy$ = new Subject<void>();
  private refreshListener = () => this.loadKartlar();

  constructor(private service: CariKartService) {}

  ngOnInit(): void {
    this.loadKartlar();
    window.addEventListener('cariKartCreated', this.refreshListener);
  }

  ngOnDestroy(): void {
    this.destroy$.next();
    this.destroy$.complete();
    window.removeEventListener('cariKartCreated', this.refreshListener);
  }

  loadKartlar(): void {
    this.service
      .list()
      .pipe(takeUntil(this.destroy$))
      .subscribe((data) => (this.kartlar = data));
  }

  deleteKart(id: number): void {
    this.service.delete(id).subscribe(() => this.loadKartlar());
  }
}
