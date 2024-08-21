import { setMapStoreSuffix } from 'pinia'

declare module 'pinia' {
  export interface MapStoresCustomization {
    suffix: ''
  }
}

setMapStoreSuffix('')

export * from './gallery_store';
export * from './product_store';
export * from './admin_panel_store';
export * from './auth_store'