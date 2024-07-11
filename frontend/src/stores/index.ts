import { setMapStoreSuffix } from 'pinia'

declare module 'pinia' {
  export interface MapStoresCustomization {
    suffix: ''
  }
}

setMapStoreSuffix('')

export * from './gallery_store';