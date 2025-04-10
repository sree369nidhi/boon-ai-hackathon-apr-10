# TMS Conversion Evaluation Report

## Summary

- Total files evaluated: 85
- Average accuracy: 61.34%

## Field Accuracy

| Field | Accuracy |
|-------|----------|
| stop_type | 100.00% |
| state | 96.91% |
| equipment_type_id | 94.12% |
| total_charge | 92.94% |
| blnum | 91.76% |
| otherchargetotal | 87.06% |
| freight_charge | 85.88% |
| sched_arrive_early | 83.44% |
| sched_arrive_late | 71.88% |
| zip_code | 69.14% |
| address | 66.67% |
| temperature_min | 31.25% |
| temperature_max | 30.00% |
| location_name | 29.63% |
| city_name | 12.35% |
| customer_id | 0.00% |

## Detailed Results

### 8251619_tms.json (Accuracy: 25.00%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| blnum | None | 8251619 |
| customer_id | UNKNOWN | NFIICHNJ |
| freight_charge | None | 2200 |
| total_charge | None | 2200 |


### 503076074_tms.json (Accuracy: 37.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | ST | CHROBIIA |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address |  | 4696 CLOVERHAVEN STREET |
| city_name |  | DALLAS |
| state |  | TX |
| zip_code |  | 75227 |
| location_name | None | PRIME DISTRIBUTION DALLAS |


### 9968850_tms.json (Accuracy: 37.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | ST | LOADNENY |
| freight_charge | None | 700 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | SAN LEANDRO |
| zip_code | 14655 | 94577 |
| location_name | RCCB - SAN LEANDRO CA PRODUCTION | Reyes coca cola truck Entrance |
| sched_arrive_early | 20200209130000-0700 | 20250209130000-0700 |
| sched_arrive_late | 20200209130000-0700 | 20250209130000-0700 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 11900 CABERNET DRIVE FONTANA | 11900 Cabernet Dr |
| city_name |  | FONTANA |
| zip_code | 11900 | 92337 |
| location_name | RCCB - RANCHO CUCAMONGA CA SALES | Rccb |
| sched_arrive_early | 20200210123000-0700 | 20250210123000-0700 |
| sched_arrive_late | 20200210123000-0700 | 20250210123000-0700 |


### 1931823_tms.json (Accuracy: 42.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | CL | CIRCFOI1 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | Oakland | 9999 San Leandro St |
| city_name |  | OAKLAND |
| location_name | None | Cold Ice Inc |

#### Stop 2 (PU, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | San Jose | 1405 E 58th Pl |
| city_name |  | LOS ANGELES |
| zip_code | 95136 | 90001 |
| location_name | None | Aramark Cleanroom Services is Now Vestis |
| sched_arrive_early | 20250123080000-0700 | 20250124080000-0700 |
| sched_arrive_late | 20250123170000-0700 | 20250124170000-0700 |

#### Stop 3 (PU, Sequence 3) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | Los Angeles | 1145 N Ocean Cir |
| city_name |  | ANAHEIM |
| zip_code | 90001 | 92806 |
| location_name | None | Oliver Healthcare Packaging |
| sched_arrive_early | 20250124080000-0700 | 20250124083000-0700 |
| sched_arrive_late | 20250124170000-0700 | 20250124173000-0700 |

#### Stop 4 (SO, Sequence 5) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | Draper | 344 Life Science Way |
| city_name |  | DRAPER |
| location_name | None | Distribution Center - Edwards Lifescienc |
| sched_arrive_early | 20250127080000-0700 | 20250131090000-0700 |
| sched_arrive_late | 20250127103000-0700 | 20250131120000-0700 |


### 8354971_tms.json (Accuracy: 45.83%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | NT | NOLAROGA |
| freight_charge | None | 233 |
| total_charge | None | 233 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 2801 South Oak Grove Road | 4101 KNIGHTHURST ROAD |
| city_name |  | ENNIS |
| location_name | SCHIRM USA INC | SSI MAXIM / SCHIRM USA |
| sched_arrive_early | 20250306080000-0700 | 20250306090000-0700 |
| sched_arrive_late | 20250306140000-0700 | 20250306090000-0700 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | DALLAS |
| zip_code | 12111 | 75234 |


### 507337554_tms.json (Accuracy: 45.83%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | CR | CHROBIIA |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | Plainfield | 4241 Plainfield Rd Bldg 9 |
| city_name |  | PLAINFIELD |
| location_name | None | PRIME/CHROBINSON Warehouse |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | Grantsville | 929 NORTH STATE ROUTE 138 |
| city_name |  | GRANTSVILLE |
| location_name | Wal-Mart #7026 | WALMART DISTRIBUTION 7026 |


### 9938764_tms.json (Accuracy: 45.83%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| blnum | 405905693 | 9938764 |
| customer_id | ST | LOADNENY |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 4800 LANGDON ROAD SUITE 400 | 4800 LANGDON ROAD |
| city_name |  | DALLAS |
| location_name | NIAGARA BOTTLING | NIAGRA |
| sched_arrive_early | 20191213080000-0700 | 20241213080000-0700 |
| sched_arrive_late | 20191213080000-0700 |  |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | FORT WORTH |
| location_name | COCA-COLA SW BEVERAGES | 3400 Fossil Creek Blvd |
| sched_arrive_early | 20191213170000-0700 | 20241213170000-0700 |
| sched_arrive_late | 20191213170000-0700 |  |


### 8226477_tms.json (Accuracy: 45.83%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | NT | NOLAROGA |
| freight_charge | None | 700 |
| total_charge | None | 700 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | SAN LEANDRO |
| zip_code | 14655 | 94577 |
| location_name | RCCB - SAN LEANDRO CA PRODUCTION | Reyes coca cola truck Entrance |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | SANTA MARIA |
| zip_code | 93455-1512 | 93455 |
| location_name | RCCB - SANTA MARIA CA SALES | RCCB CA Sales |


### 9963291_tms.json (Accuracy: 45.83%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | UNKNOWN | LOADNENY |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | RENTON |
| zip_code | 98055 | 98057 |
| sched_arrive_early | 20250131000000-0700 | 20250203130000-0700 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 12634 S 265 W | 12634 SOUTH 265 WEST |
| city_name |  | DRAPER |
| zip_code | 12634 | 84020 |
| location_name | SWIRE DRAPER | SWIRE COCA COLA |
| sched_arrive_early | 20250203000000-0700 | 20250205110000-0700 |


### 505151336_tms.json (Accuracy: 45.83%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | UNKNOWN | CHROBIIA |
| freight_charge | 1255.0 | 942.99 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 191 RT 31 North | 191 NJ-31 |
| city_name |  | WASHINGTON |
| location_name | Albea Washington | Albea Americas, Inc |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 960 Wauhatchie Pike | For BOON Purposes - DO NOT USE |
| city_name |  | WELLSVILLE |
| state | TN | UT |
| zip_code | 37419-2432 | 84339 |
| location_name | Chattem | NEEDS ATTENTION |


### 9984413_tms.json (Accuracy: 45.83%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | ST | LOADNENY |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | RENTON |
| zip_code | 98055 | 98057 |
| sched_arrive_early | 20240317160000-0700 | 20250317160000-0600 |
| sched_arrive_late | 20240317160000-0700 |  |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 12634 S 265 W | 12634 SOUTH 265 WEST |
| city_name |  | DRAPER |
| zip_code | 12634 | 84020 |
| location_name | SWIRE DRAPER | SWIRE COCA COLA |
| sched_arrive_early | 20240319120000-0700 | 20250319120000-0600 |
| sched_arrive_late | 20240319120000-0700 |  |


### 61048221_tms.json (Accuracy: 45.83%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | MC | ECCOGLIL |
| temperature_min | 32.0 | None |
| temperature_max | 32.0 | None |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 20405 EAST BUSINESS PKWY | 20405 E Walnut Dr N |
| city_name |  | WALNUT |
| zip_code | 20405 | 91789 |
| location_name | TROPICANA DC WALNUT CA | Tropicana DC |

#### Stop 2 (SO, Sequence 4) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 9494 S PROSPERITY RD | 620 WEST 600 NORTH |
| city_name |  | NORTH SALT LAKE |
| zip_code | 84081 | 84054 |
| location_name | BWC SYSCO INTERMOUNT INC | ALBERTSONS  DISTRIBUTION CENTER |
| sched_arrive_early | 20250110110000-0700 | 20250110033000-0700 |
| sched_arrive_late | 20250110110000-0700 | 20250110033000-0700 |


### 506546815_tms.json (Accuracy: 45.83%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | ST | CHROBIIA |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | Union City | 7056 Goodson Rd |
| city_name |  | UNION CITY |
| location_name | None | C H ROBINSON warehouse |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | Grantsville | 929 NORTH STATE ROUTE 138 |
| city_name |  | GRANTSVILLE |
| location_name | Wal-Mart #7026 | WALMART DISTRIBUTION 7026 |


### 505337242_tms.json (Accuracy: 50.00%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | ST | CHROBIIA |
| otherchargetotal | 0 | 490.77 |


### 14342084_tms.json (Accuracy: 50.00%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | ST | SUNTBOFL |
| otherchargetotal | 250.0 | 0 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | LONGVIEW |
| location_name | FXI | FLEXIBLE FOAM |
| sched_arrive_early | 20250120060000-0700 | 20250120163000-0700 |
| sched_arrive_late | 20250120100000-0700 | 20250120230000-0700 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 2400 S 600 West | For BOON Purposes - DO NOT USE |
| city_name |  | WELLSVILLE |
| zip_code | 84115 | 84339 |
| location_name | FXI | NEEDS ATTENTION |


### 61814758_tms.json (Accuracy: 50.00%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | UNKNOWN | ECCOGLIL |
| temperature_min | 45.0 | None |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | TACOMA |
| zip_code | 12005 | 98444 |
| location_name | GATORADE DC TACOMA WA OVERFLOW | GATORADE DC TACOMA |
| sched_arrive_early | 20250311124500-0700 | 20250311124500-0600 |
| sched_arrive_late | 20250311124500-0700 | 20250311124500-0600 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | IDAHO FALLS |
| location_name | ADMIRAL BEV/OLD FAITHFUL | ADMIRAL BEVERAGE CORP |
| sched_arrive_early | 20250313070000-0700 | 20250313070000-0600 |
| sched_arrive_late | 20250313140000-0700 | 20250313140000-0600 |


### 3301224-1_tms.json (Accuracy: 50.00%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | RD | ARMSCONC |
| freight_charge | None | 1550 |


### 3376118-1_tms.json (Accuracy: 50.00%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | UNKNOWN | ARMSCONC |
| freight_charge | None | 1100 |


### 6347607_tms.json (Accuracy: 54.17%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| blnum | 0100211029 | 6347607 |
| customer_id | DT | ARRIAUTX |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 27255 SW 95TH AVE | 27255 SOUTH WEST 95TH AVENUE |
| city_name |  | WILSONVILLE |
| zip_code | 27255 | 97070 |
| location_name | FINISHED GOODS - PACIFIC FOODS | PACIFIC FOODS |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 500 SUGAR ST | 500 NORTH SUGAR STREET |
| city_name |  | LAYTON |
| location_name | SMITH'S - LAYTON DIST CNTR | SMITHS DISTRIBUTION CENTER |


### 3294690_tms.json (Accuracy: 54.17%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | KF | KNIGPHAZ |
| otherchargetotal | 250.0 | 0 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | CARSON |
| location_name | NOVA CONTAINER FREIGHT | Beme, Nova Container Freight Station |
| sched_arrive_late | 20241204160000-0700 |  |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | SALT LAKE CITY |
| state |  | UT |
| zip_code |  | 84116 |
| location_name | EXPEDITORS SALT LAKE CITY | EXPEDITORS INTERNATIONAL |


### 3072177_tms.json (Accuracy: 54.17%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | ST | CHEESUWA |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | LACEY |
| location_name | DART/SOLO CONTAINER | DART CONTAINOR CORP |
| sched_arrive_early | 20250317060000-0700 | 20250317060000-0600 |
| sched_arrive_late | 20250317170000-0700 | 20250317170000-0600 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | WEST JORDAN |
| location_name | BWC SYSCO INTERMOUNTAIN 005 | Sysco Intermountain - Food Distributor & |
| sched_arrive_early | 20250319060000-0700 | 20250319060000-0600 |
| sched_arrive_late | 20250319060000-0700 | 20250319060000-0600 |


### 505566798_tms.json (Accuracy: 54.17%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | CR | CHROBIIA |
| freight_charge | 1750.0 | 1488.01 |
| otherchargetotal | 0 | 261.99 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | FONTANA |
| zip_code | 13169 | 92337 |
| location_name | NRI Distribution | NRI 3PL (LC) |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 1630 S 5070 W | 1630 SOUTH 5070 WEST |
| city_name |  | SALT LAKE CITY |
| location_name | Pacific Flyway DC - Inbound | SPORTSMAN WAREHOUSE DISTRIBUTION |


### 3071726_tms.json (Accuracy: 54.17%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | CL | CHEESUWA |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | LACEY |
| location_name | DART/SOLO CONTAINER | DART CONTAINOR CORP |
| sched_arrive_early | 20250310060000-0700 | 20250311060000-0600 |
| sched_arrive_late | 20250310170000-0700 | 20250311170000-0600 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | WEST JORDAN |
| location_name | BWC SYSCO INTERMOUNTAIN 005 | Sysco Intermountain - Food Distributor & |
| sched_arrive_early | 20250312090000-0700 | 20250313091100-0600 |
| sched_arrive_late | 20250312090000-0700 |  |


### 9968821_tms.json (Accuracy: 54.17%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | ST | LOADNENY |
| freight_charge | None | 2550 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | OXNARD |
| location_name | EXEL LOGISTICS (P&G) | Procter & Gamble Paper Products |
| sched_arrive_early | 20200208130000-0700 | 20250208130000-0700 |
| sched_arrive_late | 20200208210000-0700 | 20250208210000-0700 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | BEAR RIVER CITY |
| sched_arrive_early | 20200210000100-0700 | 20250210000100-0700 |
| sched_arrive_late | 20200210235900-0700 | 20250210235900-0700 |


### 9979590_tms.json (Accuracy: 56.25%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | ST | LOADNENY |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | RENTON |
| zip_code | 98055 | 98057 |
| sched_arrive_early | 20240310130000-0700 | 20250310130000-0600 |
| sched_arrive_late | 20240310130000-0700 | 20250310130000-0600 |


### 506573704_tms.json (Accuracy: 58.33%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | CR | CHROBIIA |
| otherchargetotal | 16.81 | 0 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | DALLAS |
| location_name | Gatorade-Dallas | Gatorade |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | FORT WORTH |
| location_name | SILVERCREEK | Silver Creek Materials |


### 0100767_tms.json (Accuracy: 58.33%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | ST | MOUNTACO |
| freight_charge | 850.0 | 800 |
| total_charge | 850.0 | 800 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | KING SOOPERS AURORA | KING SOOPERS, INC. |
| sched_arrive_late | 20241203150000-0700 | 20241203100000-0700 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | UTDA - Eco Service - Salt Lake City | Eco Service |
| sched_arrive_early | 20241203090000-0700 | 20241204090000-0700 |


### 7363582_tms.json (Accuracy: 58.33%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | AL | ALLELACA |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | YUBA CITY |
| location_name | ARDENT MILLS LLC | Ardent Mills Yuba City Mill |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | MIRA LOMA |
| zip_code | 11600 | 91752 |
| location_name | MIRA LOMA DRY #960 | COSTCO DISTRIBUTION 960 |


### 70729538_tms.json (Accuracy: 58.33%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | ST | AVENCHIL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | FORNEY |
| state |  | TX |
| location_name | SMURFIT KAPPA/OCC | SMURFIT KAPPA COATING MILL |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | SPANISH FORK |
| state |  | UT |
| location_name | SMURFIT SPANISH FORK | WestRock / Smurfit |


### 506232608_tms.json (Accuracy: 58.33%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | UNKNOWN | CHROBIIA |
| otherchargetotal | 9.02 | 0 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | FORT WORTH |
| zip_code | 15200 | 76155 |
| location_name | Refresco - Ft. Worth, TX | Refresco Beverages |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | ROANOKE |
| location_name | RANDALLS FOOD & DRUG LP A SUB. OF ALBERTSONS COMPA | SAFEWAY/RANDALLS/THOM THUMB |


### 60866061_tms.json (Accuracy: 58.33%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | EG | ECCOGLIL |
| temperature_min | 50.0 | None |
| temperature_max | 50.0 | None |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | KENT |
| zip_code | 23028 | 98032 |
| sched_arrive_late | 20241226120000-0700 |  |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 5995 W 300 S | 5995 WEST  300 SOUTH |
| city_name |  | SALT LAKE CITY |
| location_name | COSTCO | COSTCO DISTRIBUTION 584 |
| sched_arrive_late | 20241228100000-0700 |  |


### 504104411_tms.json (Accuracy: 58.33%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | CR | CHROBIIA |
| otherchargetotal | 502.66 | 0 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | DALLAS |
| location_name | GREIF DALLAS - DBA MULTI CORRCHOICE | GREIF DALLAS |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 6195 S 300 W STE 300 | 6195 WEST 300 SOUTH SUITE 300 |
| city_name |  | SALT LAKE CITY |
| zip_code | 84104-6013 | 84104 |
| location_name | PREMIER PKG % INTERWEST TRANSPORTATION - IDSLC | INTERWEST TRANSPORTATION |


### 2001809674_tms.json (Accuracy: 58.33%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | ST | MOLOCHIL |
| equipment_type_id | V | VR |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 151 S. Walnut Rd. | 151 SOUTH WALNUT ROAD |
| city_name |  | TURLOCK |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | ANAHEIM |
| zip_code | 92806-1906 | 92806 |


### 0245658_tms.json (Accuracy: 62.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | FT | CASHWEUT |
| freight_charge | 2200.0 | 2400 |
| otherchargetotal | 200.0 | 0 |
| temperature_max | -10.0 | 0 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | ALBERTVILLE |
| location_name | Americold Logistics | AMERICOLD |
| sched_arrive_late | 20241220100000-0700 |  |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | SALT LAKE CITY |
| sched_arrive_late | 20241224090000-0700 |  |


### 1183886_tms.json (Accuracy: 62.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| blnum | S965843 | 1183886 |
| customer_id | CO | CENTREOR |
| equipment_type_id | V | R |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | MEDFORD |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | BRIGHAM CITY |


### 3945196_tms.json (Accuracy: 62.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | LI | LANDSTFL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | HAILEY |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 3110 S 900 W | 3110 SOUTH 900 WEST |
| city_name |  | SALT LAKE CITY |
| zip_code | 84101 | 84104 |
| location_name | Rocky Mtn. Recycling (South) | ROCKY MOUNTAIN RECYCLING |
| sched_arrive_early | 20241227073000-0700 | 20241224140000-0700 |


### 2001824215_tms.json (Accuracy: 62.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | MS | MOLOCHIL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | IRVING |
| sched_arrive_late | 20241213160000-0700 |  |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | KELLER |
| zip_code | 76248 | 76244 |
| location_name | The Kroger Co. - Kroger - Dallas-035C | Kroger Distribution Center Warehouse (Tr |
| sched_arrive_late | 20241213220000-0700 |  |


### 14446278_tms.json (Accuracy: 62.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | ST | SUNTBOFL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | LONGVIEW |
| location_name | FXI | FLEXIBLE FOAM |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 2400 South 600 W | For BOON Purposes - DO NOT USE |
| city_name |  | WELLSVILLE |
| zip_code | 84115 | 84339 |
| location_name | Salt Lake Mattress Co/ Serta | NEEDS ATTENTION |


### 8299332_tms.json (Accuracy: 62.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | UNKNOWN | NOLAROGA |
| freight_charge | None | 1500 |
| total_charge | None | 1500 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | ANNAPOLIS JCT |
| zip_code | 10925 | 20701 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | SALTILLO |


### 61578870_tms.json (Accuracy: 62.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | UNKNOWN | ECCOGLIL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | TACOMA |
| zip_code | 17613 | 98446 |
| location_name | LGE NG2 Warehouse | LGE US DC TACOMA |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | IDC/FREEPORT CENTER BUILDING D-7 FREEPORT CENTER | Freeport Center Building D7 |
| city_name |  | CLEARFIELD |
| location_name | R.C. WILLEY HOME FURNISHING | RC Willey |


### 504819841_tms.json (Accuracy: 62.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | UNKNOWN | CHROBIIA |
| otherchargetotal | 179.99 | 0 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 658 South 7th Street | 658 S 7th St |
| city_name |  | READING |
| location_name | UCI Mill / DS Smith | United Corrstack / Ds Smith |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | ASHEBORO |
| location_name | SOUTHCORR PACKAGING, LLC | DS Smith Asheboro |


### 61231181_tms.json (Accuracy: 62.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | EG | ECCOGLIL |
| equipment_type_id | V | R |
| temperature_min | 50.0 | None |
| temperature_max | 50.0 | None |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | KENT |
| zip_code | 23028 | 98032 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 5995 W 300 S | 5995 WEST  300 SOUTH |
| city_name |  | SALT LAKE CITY |
| location_name | COSTCO | COSTCO DISTRIBUTION 584 |


### 32617822_tms.json (Accuracy: 62.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | CL | COYOALGA |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | SALEM |
| zip_code | 97302 | 97301 |
| location_name | SLD Salem | KETTLE FOODS |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 500 SUGAR ST | 500 NORTH SUGAR STREET |
| city_name |  | LAYTON |
| location_name | Kroger- Smiths-RFG | KROGER / SMITH'S DAIRY |


### 61375773_tms.json (Accuracy: 62.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | UNKNOWN | ECCOGLIL |
| equipment_type_id | V | R |
| temperature_min | 50.0 | None |
| temperature_max | 50.0 | None |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | KENT |
| zip_code | 23028 | 98032 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 5995 W 300 S | 5995 WEST  300 SOUTH |
| city_name |  | SALT LAKE CITY |
| location_name | COSTCO SALT LAKE CITY #584 | COSTCO DISTRIBUTION 584 |


### 607273_tms.json (Accuracy: 65.00%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| blnum | #607273 | 607273 |
| customer_id | SL | SPARROIL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 15750 MERIDIAN PKWY RIVERSIDE | 15750 Meridian Pkwy |
| city_name |  | RIVERSIDE |
| zip_code | 15750 | 92518 |
| location_name | SYSCO RIVERSIDE | Sysco Riverside - Wholesale Restaurant F |

#### Stop 2 (PU, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | WALNUT |
| zip_code | 20701 | 91789 |

#### Stop 3 (PU, Sequence 3) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 6201 E CENTENNIAL PKWY Las Vegas | 6201 E CENTENNIAL PARKWAY |
| city_name |  | LAS VEGAS |

#### Stop 4 (SO, Sequence 4) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 9494 SOUTH PROSPERITY WAY WEST JORDAN | 9494 SOUTH PROSPERITY ROAD |
| city_name |  | WEST JORDAN |
| zip_code | 84081 | 84088 |


### 61174109_tms.json (Accuracy: 66.67%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | EG | ECCOGLIL |
| temperature_min | 50.0 | None |
| temperature_max | 50.0 | None |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | KENT |
| zip_code | 23028 | 98032 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 5995 W 300 S | 5995 WEST  300 SOUTH |
| city_name |  | SALT LAKE CITY |
| location_name | COSTCO SALT LAKE CITY #584 | COSTCO DISTRIBUTION 584 |


### 2001868099_tms.json (Accuracy: 66.67%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | MS | MOLOCHIL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | DALLAS |
| zip_code | 10409 | 75238 |
| location_name | Absopure Waters - Absopure - 03501657 | Hydration Source |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | ENNIS |
| location_name | CVS TEXAS DIST L P | CVS Health Distribution Center |


### 1353403_tms.json (Accuracy: 66.67%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | UNKNOWN | TASEMATX |
| otherchargetotal | 550.0 | 0 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | SHASTA LAKE |
| location_name | KNAUF INSULATION | Knauf Fiberglass |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | WASHINGTON |


### 31440-90145_tms.json (Accuracy: 66.67%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | JC | NEONSCAZ |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | LAS VEGAS |
| location_name | Johnstone Supply | Las Vegas Distribution Center |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | SPRINGVILLE |
| location_name | Supanaturals | MOUNTAINLAND SUPPLY CO |


### 2001828290_tms.json (Accuracy: 66.67%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | MS | MOLOCHIL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | GREENVILLE |
| zip_code | 75402-5713 | 75402 |
| location_name | ROYAL OAK #203 | PINE MOUNTAIN |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | ROANOKE |
| location_name | SAFEWAY DALLAS | SAFEWAY/RANDALLS/THOM THUMB |


### 3068716_tms.json (Accuracy: 66.67%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | CL | CHEESUWA |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | LACEY |
| location_name | DART/SOLO CONTAINER | DART CONTAINOR CORP |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 5400 W Hwy 83 | 5400 WEST HIGHWAY 83 |
| city_name |  | CORINNE |
| location_name | WALMART DC 6080 | WALMART DISTRIBUTION 6090 |


### 3071603_tms.json (Accuracy: 66.67%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | CL | CHEESUWA |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | DART/SOLO CONTAINER | DART CONTAINOR CORP |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 5995 W300S | 5995 WEST  300 SOUTH |
| location_name | COSTCO 584 | COSTCO DISTRIBUTION 584 |
| sched_arrive_early | 20250310050000-0700 | 20250310050000-0600 |
| sched_arrive_late | 20250310050000-0700 | 20250310050000-0600 |


### 507294874_tms.json (Accuracy: 66.67%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | CR | CHROBIIA |
| total_charge | 710.0 | 870.31 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | ALIQUIPPA |
| sched_arrive_late | 20250304213000-0700 | 20250304120000-0700 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | LOUISVILLE |
| location_name | The Royal Group | The Royal Group - Commerce Crossings |


### 4231282_tms.json (Accuracy: 66.67%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | SC | VISUWAIL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | Swire Coca-Cola | COCA-COLA BOTTLING CO. |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 12634 S 265 W | 12634 SOUTH 265 WEST |
| zip_code | 12634 | 84020 |


### 31483-42812_tms.json (Accuracy: 66.67%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | SF | CHROBIIA |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | GRAND PRAIRIE |
| location_name | POWER PACKAGING A DHL COMPANY | Power Packing of Texas Inc |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | FORT WORTH |


### 4006371285_tms.json (Accuracy: 66.67%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | ST | SCHNEIKY |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | LACEY |
| zip_code | 98516-7152 | 98516 |
| location_name | SOLO CUP CO | DART CONTAINOR CORP |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | NORTH SALT LAKE |
| zip_code | 84054-2124 | 84054 |


### 504102841_tms.json (Accuracy: 66.67%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | CR | CHROBIIA |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 658 South 7th Street | 658 S 7th St |
| city_name |  | READING |
| location_name | UCI Mill / DS Smith | United Corrstack / Ds Smith |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | ASHEBORO |
| location_name | SOUTHCORR PACKAGING, LLC | DS Smith Asheboro |


### 8665815_tms.json (Accuracy: 66.67%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | ST | TRINITDE |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | CLEBURNE |
| sched_arrive_late | 20241211090000-0700 |  |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | DALLAS |
| location_name | PAMACO INSULATION, LLC | Pamaco Inc. |
| sched_arrive_late | 20241211133000-0700 | 20241211130000-0700 |


### 2001836741_tms.json (Accuracy: 66.67%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | UNKNOWN | MOLOCHIL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | DALLAS |
| zip_code | 10409 | 75238 |
| location_name | Absopure Waters - Absopure | Hydration Source |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | ENNIS |
| location_name | CVS TEXAS DIST L P | CVS Health Distribution Center |


### 60752192_tms.json (Accuracy: 66.67%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | EG | ECCOGLIL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | LONGVIEW |
| location_name | LONGVIEW FIBRE PAPER - PACKAGING INC | KAPSTONE KRAFT PAPER |
| sched_arrive_late | 20241208130000-0700 |  |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 451 N 5600 W | 451 NORTH 5600 WEST |
| city_name |  | SALT LAKE CITY |


### 4233261_tms.json (Accuracy: 66.67%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | VP | VISUWAIL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | BELLEVUE |
| location_name | Swire Coca-Cola | COCA-COLA BOTTLING CO. |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 12634 S 265 W | 12634 SOUTH 265 WEST |
| city_name |  | DRAPER |
| zip_code | 12634 | 84020 |


### 31421-79757_tms.json (Accuracy: 68.75%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | NL | NEONSCAZ |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | RENTON |
| location_name | JAVA TRADING CO LLC | JAVA TRADING |


### 2001073484_tms.json (Accuracy: 68.75%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | WL | WERNOMNE |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | CORONA |
| location_name | Vegfresh | Veg-Fresh Farms |

#### Stop 2 (PU, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | FULLERTON |
| location_name | VegCool | Veg-land Inc |

#### Stop 3 (SO, Sequence 3) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 500 Sugar St | 500 NORTH SUGAR STREET |
| city_name |  | LAYTON |
| location_name | Smith's Food & Drug Centers | SMITHS DISTRIBUTION CENTER |


### 61666028_tms.json (Accuracy: 68.75%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | UNKNOWN | ECCOGLIL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 1613 132ND AVE E | 1613 132ND AVENUE #100 |
| location_name | CMS c/o MrPEX Systems | AMERICAN FALLS SOLAR |


### 60847782_tms.json (Accuracy: 68.75%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | EG | ECCOGLIL |
| temperature_min | 45.0 | None |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | TACOMA |
| location_name | QUAKER DC TACOMA | QUAKER |


### 6371326_tms.json (Accuracy: 70.83%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | AL | ARRIAUTX |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | BELLEVUE |
| location_name | SWIRE CCUSA BELLEVUE WA PROD CTR | COCA-COLA BOTTLING CO. |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | DRAPER |
| zip_code | 12634 | 84020 |


### 504798115_tms.json (Accuracy: 70.83%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | CR | CHROBIIA |
| otherchargetotal | 106.6 | 0 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | FORT WORTH |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | HOUSTON |
| zip_code | 10025 | 77029 |


### 61579102_tms.json (Accuracy: 70.83%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | MC | ECCOGLIL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | MODESTO |
| location_name | Gallo Winery | GALLO |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | LA HABRA |
| location_name | CVS | CVS ANNEX WHSE #H1L3 |


### 5001712233_tms.json (Accuracy: 70.83%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | PI | PRIMSPMO |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | CLOVIS |
| location_name | SOUTHWEST CHEESE | SWC CLOVIS POWDER STORE |
| sched_arrive_late | 20241217150000-0700 |  |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 780 W 1400 S | 780 WEST 1400 SOUTH |
| city_name |  | FILLMORE |
| sched_arrive_late | 20241219120000-0700 |  |


### 61550952_tms.json (Accuracy: 70.83%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | MC | ECCOGLIL |
| temperature_min | 45.0 | None |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | TACOMA |
| location_name | QUAKER DC TACOMA | QUAKER |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 531 W 600 N | 531 WEST 600 NORTH |
| city_name |  | SALT LAKE CITY |


### 6637008_tms.json (Accuracy: 70.83%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | DT | ARRIAUTX |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | WINLOCK |
| zip_code | 98596-9657 | 98596 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | SALT LAKE CITY |


### 60778077_tms.json (Accuracy: 70.83%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | EG | ECCOGLIL |
| temperature_min | 45.0 | None |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | TACOMA |
| location_name | QUAKER DC TACOMA | QUAKER |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 531 W 600 N | 531 WEST 600 NORTH |
| city_name |  | SALT LAKE CITY |


### 61217638_tms.json (Accuracy: 70.83%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | UNKNOWN | ECCOGLIL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | TACOMA |
| location_name | QUAKER DC TACOMA | QUAKER |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 531 W 600 N | 531 WEST 600 NORTH |
| city_name |  | SALT LAKE CITY |


### 32688939_tms.json (Accuracy: 70.83%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | ST | COYOALGA |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 489 N PRATT RD Monticello | 489 NORTH PRATT ROAD |
| city_name |  | MONTICELLO |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 331 JOINT PARK BLVD Tullahoma | 331 Joint Park Blvd |
| city_name |  | TULLAHOMA |


### 14530945_tms.json (Accuracy: 70.83%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | ST | SUNTBOFL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | LONGVIEW |
| location_name | FXI | FLEXIBLE FOAM |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | SALT LAKE CITY |
| location_name | Salt Lake Mattress Co/ Serta | SERTA MATTRESS |


### 14342080_tms.json (Accuracy: 70.83%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | ST | SUNTBOFL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | LONGVIEW |
| location_name | FXI | FLEXIBLE FOAM |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | SALT LAKE CITY |
| location_name | FXI | SERTA MATTRESS |


### 3070046_tms.json (Accuracy: 75.00%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | CL | CHEESUWA |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | DART/SOLO CONTAINER | DART CONTAINOR CORP |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 1635 S 5070 WEST STE B | 1635 SOUTH 5070 WEST |
| city_name | SALT LAKE CTY | SALT LAKE CITY |


### 61407132_tms.json (Accuracy: 75.00%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | UNKNOWN | ECCOGLIL |
| temperature_min | 50.0 | None |
| temperature_max | 50.0 | None |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| zip_code | 23028 | 98032 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 5995 W 300 S | 5995 WEST  300 SOUTH |
| location_name | COSTCO | COSTCO DISTRIBUTION 584 |


### 3607052_tms.json (Accuracy: 75.00%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | RM | REDWCHIL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | SANDSTON |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | SPRINGVILLE |
| location_name | Nestle Frozen Foods | NESTLE FOODS |


### 2365675_tms.json (Accuracy: 75.00%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| blnum | PO 7198720 | 2365675 |
| customer_id | UNKNOWN | HUBGROIL |
| equipment_type_id | V | VR |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 505 S BRENDA PLACE BLD 605 | 505 S Brenda Pl Blgd#605 Ste #1 |


### 3068411_tms.json (Accuracy: 75.00%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | CL | CHEESUWA |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | COOS BAY |
| zip_code | 63776 | 97420 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name |  | LINDON |


### 2145346_tms.json (Accuracy: 75.00%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| blnum | 4502378939 | 2145346 |
| customer_id | UNKNOWN | AXLEKNTN |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | Blue Ribbon | Blue Ribbon Delivery Inc |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | McCormick | Mc Cormick & Co Inc |


### 0148909_tms.json (Accuracy: 79.17%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | CT | COASDEIL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | Savannah Logistics Warehouse | MERCER DISTRIBUTION SERVICES |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | KIMBALL RENTALS LLC | Kimball Equipment Company |


### 61465411_tms.json (Accuracy: 79.17%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | EG | ECCOGLIL |
| temperature_min | 45.0 | None |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | QUAKER DC TACOMA | QUAKER |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 531 W 600 N | 531 WEST 600 NORTH |


### 3070085_tms.json (Accuracy: 79.17%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | ST | CHEESUWA |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | DART/SOLO CONTAINER | DART CONTAINOR CORP |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | BWC SYSCO INTERMOUNTAIN | Sysco Intermountain - Food Distributor & |


