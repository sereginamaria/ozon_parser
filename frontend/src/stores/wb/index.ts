import { setMapStoreSuffix } from 'pinia'

declare module 'pinia' {
  export interface MapStoresCustomization {
    suffix: ''
  }
}

setMapStoreSuffix('')

export * from './verification_store';
export * from './product_store';
export * from './admin_panel_store';