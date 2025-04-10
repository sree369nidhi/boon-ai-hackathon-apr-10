# LLM-based TMS Conversion Evaluation Report

## Summary

- Total files evaluated: 85
- Average accuracy: 61.35%

## Field Accuracy

| Field | Accuracy |
|-------|----------|
| stop_type | 100.00% |
| equipment_type_id | 95.12% |
| state | 94.19% |
| blnum | 89.41% |
| total_charge | 89.02% |
| zip_code | 88.39% |
| sched_arrive_early | 78.06% |
| otherchargetotal | 78.05% |
| freight_charge | 73.17% |
| sched_arrive_late | 63.23% |
| address | 50.97% |
| city_name | 45.81% |
| location_name | 28.39% |
| customer_id | 2.35% |
| temperature_min | 0.00% |
| temperature_max | 0.00% |

## Detailed Results

### 2001828290_tms.json (Accuracy: 12.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | UNKNOWN | MOLOCHIL |


### 3607052_tms.json (Accuracy: 12.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | UNKNOWN | REDWCHIL |


### 506232608_tms.json (Accuracy: 12.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | UNKNOWN | CHROBIIA |


### 8251619_tms.json (Accuracy: 16.67%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| blnum | ORDER0001 | 8251619 |
| customer_id | UNKNOWN | NFIICHNJ |
| freight_charge | 0 | 2200 |
| total_charge | 0 | 2200 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | UNKNOWN | 4877 N Cotton Ln |
| city_name | UNKNOWN | GOODYEAR |
| state | UNKNOWN | AZ |
| zip_code | 00000 | 85395 |
| location_name | UNKNOWN | REI Distribution Center |
| sched_arrive_early | 20231015000000-0700 | 20250219160000-0700 |
| sched_arrive_late | 20231015010000-0700 | 20250219160000-0700 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | UNKNOWN | 3285 E 3300 S |
| city_name | UNKNOWN | SALT LAKE CITY |
| state | UNKNOWN | UT |
| zip_code | 00000 | 84109 |
| location_name | UNKNOWN | REI |
| sched_arrive_early | 20231015020000-0700 | 20250221070000-0700 |
| sched_arrive_late | 20231015030000-0700 | 20250221070000-0700 |


### 3301224-1_tms.json (Accuracy: 29.17%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | RD | ARMSCONC |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | Unknown Pickup Address | 4326 86TH AVENUE EAST |
| city_name | Unknown City | PUYALLUP |
| state | Unknown State | WA |
| zip_code | 00000 | 98371 |
| location_name | Unknown Pickup Location | LSI |
| sched_arrive_early | 20231010120000-0700 | 20250129140000-0700 |
| sched_arrive_late | 20231010140000-0700 | 20250129140000-0700 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | Unknown Delivery Address | 1375 MOUNTAIN SPRINGS PARKWAY |
| city_name | Unknown City | SPRINGVILLE |
| state | Unknown State | UT |
| zip_code | 00000 | 84663 |
| location_name | Unknown Delivery Location | PET IQ |
| sched_arrive_early | 20231011120000-0700 | 20250131100000-0700 |
| sched_arrive_late | 20231011140000-0700 | 20250131100000-0700 |


### 3376118-1_tms.json (Accuracy: 29.17%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | UNKNOWN | ARMSCONC |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | UNKNOWN | 2777 USA PARKWAY |
| city_name | UNKNOWN | SPARKS |
| state | UNKNOWN | NV |
| zip_code | UNKNOWN | 89434 |
| location_name | UNKNOWN | PROPAK |
| sched_arrive_early | 20231010120000-0700 | 20250306130000-0700 |
| sched_arrive_late | 20231010140000-0700 |  |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | UNKNOWN | 2850 SOUTH 900 WEST |
| city_name | UNKNOWN | SALT LAKE CITY |
| state | UNKNOWN | UT |
| zip_code | UNKNOWN | 84119 |
| location_name | UNKNOWN | UPDIKE DISTRIBUTION |
| sched_arrive_early | 20231011120000-0700 | 20250307110000-0700 |
| sched_arrive_late | 20231011140000-0700 |  |


### 503076074_tms.json (Accuracy: 31.25%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | SHARPTRI | CHROBIIA |
| freight_charge | 3316.4 | 2295 |
| otherchargetotal | 0 | 1021.4 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | Unknown | 4696 CLOVERHAVEN STREET |
| city_name | Unknown | DALLAS |
| state | Unknown | TX |
| zip_code | Unknown | 75227 |
| location_name | Unknown | PRIME DISTRIBUTION DALLAS |
| sched_arrive_early |  | 20250129160000-0700 |


### 505337242_tms.json (Accuracy: 41.67%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | SHARPTRI | CHROBIIA |
| otherchargetotal | 0 | 490.77 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | P.O. Box 3470, Chicago, IL 60654 | 9450 Burleson Cardinal Rd |
| city_name | Chicago | FORT WORTH |
| state | IL | TX |
| zip_code | 60654 | 76140 |
| location_name | Sharp Transportation, Inc. | Ft.Worth Logistics Hub- Samsung |
| sched_arrive_early | 20231011000000-0700 | 20250217060000-0700 |
| sched_arrive_late | 20231011000000-0700 | 20250217060000-0700 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 5995 West 300 South, Salt Lake City, UT 84104 | 5995 WEST  300 SOUTH |
| city_name | Salt Lake City | SALT LAKE CITY |
| location_name | COSTCO WHOLESALE #584 DEPOT | COSTCO DISTRIBUTION 584 |


### 507337554_tms.json (Accuracy: 41.67%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | CR | CHROBIIA |
| freight_charge | 3976.5 | 3195 |
| otherchargetotal | 0 | 781.5 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | Plainfield, IN 46168 | 4241 Plainfield Rd Bldg 9 |
| city_name | Plainfield | PLAINFIELD |
| location_name | Plainfield Pickup | PRIME/CHROBINSON Warehouse |
| sched_arrive_early |  | 20250314120000-0600 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | Grantsville, UT 84029 | 929 NORTH STATE ROUTE 138 |
| city_name | Grantsville | GRANTSVILLE |
| location_name | Wal-Mart #7026 | WALMART DISTRIBUTION 7026 |
| sched_arrive_early |  | 20250316030000-0600 |
| sched_arrive_late |  | 20250317230000-0600 |


### 9963291_tms.json (Accuracy: 41.67%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | UNKNOWN | LOADNENY |
| freight_charge | 1608.77 | 1277.38 |
| otherchargetotal | 0 | 331.39 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name | Renton | RENTON |
| zip_code | 98055 | 98057 |
| sched_arrive_early | 20250131000000-0700 | 20250203130000-0700 |
| sched_arrive_late | 20250131000000-0700 |  |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 12634 S 265 W | 12634 SOUTH 265 WEST |
| city_name | Draper | DRAPER |
| location_name | SWIRE DRAPER | SWIRE COCA COLA |
| sched_arrive_early | 20250203000000-0700 | 20250205110000-0700 |
| sched_arrive_late | 20250203000000-0700 |  |


### 505151336_tms.json (Accuracy: 41.67%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | UNKNOWN | CHROBIIA |
| freight_charge | 1255.0 | 942.99 |
| total_charge | 1567.01 | 1255 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 191 RT 31 North, Washington, NJ 07882 | 191 NJ-31 |
| city_name | Washington | WASHINGTON |
| location_name | Albea Washington | Albea Americas, Inc |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 960 Wauhatchie Pike, CHATTANOOGA, TN 37419-2432 | For BOON Purposes - DO NOT USE |
| city_name | CHATTANOOGA | WELLSVILLE |
| state | TN | UT |
| zip_code | 37419 | 84339 |
| location_name | Chattem | NEEDS ATTENTION |
| sched_arrive_late |  | 20250213080000-0700 |


### 9984413_tms.json (Accuracy: 41.67%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | SHARPTRI | LOADNENY |
| freight_charge | 1617.27 | 1277.38 |
| otherchargetotal | 0 | 339.89 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name | Renton | RENTON |
| zip_code | 98055 | 98057 |
| sched_arrive_early | 20240317160000-0700 | 20250317160000-0600 |
| sched_arrive_late | 20240317160000-0700 |  |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 12634 S 265 W | 12634 SOUTH 265 WEST |
| city_name | Draper | DRAPER |
| location_name | SWIRE DRAPER | SWIRE COCA COLA |
| sched_arrive_early | 20240319120000-0700 | 20250319120000-0600 |
| sched_arrive_late | 20240319120000-0700 |  |


### 506546815_tms.json (Accuracy: 41.67%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | SHARPTRI | CHROBIIA |
| freight_charge | 4576.06 | 3597.88 |
| otherchargetotal | 0 | 978.18 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | Union City, GA 30291 | 7056 Goodson Rd |
| city_name | Union City | UNION CITY |
| location_name | Union City Pickup | C H ROBINSON warehouse |
| sched_arrive_early |  | 20250303130000-0700 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | Grantsville, UT 84029 | 929 NORTH STATE ROUTE 138 |
| city_name | Grantsville | GRANTSVILLE |
| location_name | Wal-Mart #7026 | WALMART DISTRIBUTION 7026 |
| sched_arrive_early |  | 20250306030000-0700 |
| sched_arrive_late |  | 20250307230000-0700 |


### 9979590_tms.json (Accuracy: 43.75%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | SHARPTRI | LOADNENY |
| freight_charge | 1617.27 | 1277.38 |
| otherchargetotal | 0 | 339.89 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name | Renton | RENTON |
| zip_code | 98055 | 98057 |
| sched_arrive_early | 20240310130000-0700 | 20250310130000-0600 |
| sched_arrive_late | 20240310130000-0700 | 20250310130000-0600 |


### 9938764_tms.json (Accuracy: 45.83%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| blnum | 405905693 | 9938764 |
| customer_id | SHARPTRI | LOADNENY |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 4800 LANGDON ROAD SUITE 400 | 4800 LANGDON ROAD |
| city_name | Dallas | DALLAS |
| location_name | NIAGARA BOTTLING | NIAGRA |
| sched_arrive_early | 20191213080000-0700 | 20241213080000-0700 |
| sched_arrive_late | 20191213080000-0700 |  |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name | Fort Worth | FORT WORTH |
| location_name | COCA-COLA SW BEVERAGES | 3400 Fossil Creek Blvd |
| sched_arrive_early | 20191213170000-0700 | 20241213170000-0700 |
| sched_arrive_late | 20191213170000-0700 |  |


### 0100767_tms.json (Accuracy: 50.00%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | SHARPTRI | MOUNTACO |
| freight_charge | 850.0 | 800 |
| total_charge | 850.0 | 800 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 1933 TOWER ROAD, AURORA CO 80011 | 1933 TOWER ROAD |
| location_name | KING SOOPERS AURORA | KING SOOPERS, INC. |
| sched_arrive_late | 20241203150000-0700 | 20241203100000-0700 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 3175 W 500 S, SALT LAKE CITY UT 84104 | 3175 W 500 S |
| location_name | UTDA - Eco Service - Salt Lake City | Eco Service |
| sched_arrive_early | 20241203090000-0700 | 20241204090000-0700 |
| sched_arrive_late | None |  |


### 9968850_tms.json (Accuracy: 50.00%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | SHARPTRI | LOADNENY |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name | San Leandro | SAN LEANDRO |
| location_name | RCCB - SAN LEANDRO CA PRODUCTION | Reyes coca cola truck Entrance |
| sched_arrive_early | 20200209130000-0700 | 20250209130000-0700 |
| sched_arrive_late | 20200209130000-0700 | 20250209130000-0700 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 11900 CABERNET DRIVE FONTANA | 11900 Cabernet Dr |
| city_name | Fontana | FONTANA |
| location_name | RCCB - RANCHO CUCAMONGA CA SALES | Rccb |
| sched_arrive_early | 20200210123000-0700 | 20250210123000-0700 |
| sched_arrive_late | 20200210123000-0700 | 20250210123000-0700 |


### 32617822_tms.json (Accuracy: 50.00%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | CL | COYOALGA |
| freight_charge | 1650.0 | 1324.92 |
| otherchargetotal | 0 | 325.08 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 1610 14TH ST SE, Salem, OR 97302 | 1610 14TH STREET SE |
| city_name | Salem | SALEM |
| zip_code | 97302 | 97301 |
| location_name | SLD Salem | KETTLE FOODS |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 500 SUGAR ST, Layton, UT 84041 | 500 NORTH SUGAR STREET |
| city_name | Layton | LAYTON |
| location_name | Kroger- Smiths-RFG | KROGER / SMITH'S DAIRY |


### 9968821_tms.json (Accuracy: 50.00%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | SHARPTRI | LOADNENY |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 800 N Rice Ave, Oxnard, CA 93030 | 800 Rice Ave |
| city_name | Oxnard | OXNARD |
| location_name | EXEL LOGISTICS (P&G) | Procter & Gamble Paper Products |
| sched_arrive_early | 20200208130000-0700 | 20250208130000-0700 |
| sched_arrive_late | 20200208210000-0700 | 20250208210000-0700 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 5000 N. IOWA STRING ROAD, Bear River City, UT 84301 | 5000 IOWA STRING ROAD |
| city_name | Bear River City | BEAR RIVER CITY |
| sched_arrive_early | 20200210000100-0700 | 20250210000100-0700 |
| sched_arrive_late | 20200210235900-0700 | 20250210235900-0700 |


### 8354971_tms.json (Accuracy: 54.17%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | SOARSAUT | NOLAROGA |
| freight_charge | 0 | 233 |
| total_charge | 0 | 233 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 2801 South Oak Grove Road | 4101 KNIGHTHURST ROAD |
| city_name | Ennis | ENNIS |
| location_name | SCHIRM USA INC | SSI MAXIM / SCHIRM USA |
| sched_arrive_early | 20250306080000-0700 | 20250306090000-0700 |
| sched_arrive_late | 20250306140000-0700 | 20250306090000-0700 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name | Dallas | DALLAS |


### 14342084_tms.json (Accuracy: 54.17%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | ST | SUNTBOFL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name | Longview | LONGVIEW |
| location_name | FXI | FLEXIBLE FOAM |
| sched_arrive_early | 20250120060000-0700 | 20250120163000-0700 |
| sched_arrive_late | 20250120100000-0700 | 20250120230000-0700 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 2400 S 600 West | For BOON Purposes - DO NOT USE |
| city_name | Salt Lake City | WELLSVILLE |
| zip_code | 84115 | 84339 |
| location_name | FXI | NEEDS ATTENTION |


### 2001824215_tms.json (Accuracy: 54.17%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | MS | MOLOCHIL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 1331 E. Airport Freeway, Irving, TX 75062 | 1331 E Airport Fwy |
| city_name | Irving | IRVING |
| sched_arrive_late | 20241213160000-0700 |  |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 5801 Kroger Drive, Keller, TX 76248 | 5801 Kroger Dr |
| city_name | Keller | KELLER |
| zip_code | 76248 | 76244 |
| location_name | The Kroger Co. - Kroger - Dallas-035C | Kroger Distribution Center Warehouse (Tr |
| sched_arrive_late | 20241213220000-0700 |  |


### 507294874_tms.json (Accuracy: 54.17%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | CR | CHROBIIA |
| total_charge | 710.0 | 870.31 |
| otherchargetotal | 0 | 160.31 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 5000 Woodlawn Rd, Aliquippa, PA 15001 | 5000 Woodlawn Rd |
| city_name | Aliquippa | ALIQUIPPA |
| sched_arrive_late | 20250304213000-0700 | 20250304120000-0700 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 4600 Commerce Crossings Dr, Louisville, KY 40229 | 4600 Commerce Crossings Dr |
| city_name | Louisville | LOUISVILLE |
| location_name | The Royal Group | The Royal Group - Commerce Crossings |


### 3072177_tms.json (Accuracy: 54.17%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | SHARPTRI | CHEESUWA |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name | Lacey | LACEY |
| location_name | DART/SOLO CONTAINER | DART CONTAINOR CORP |
| sched_arrive_early | 20250317060000-0700 | 20250317060000-0600 |
| sched_arrive_late | 20250317170000-0700 | 20250317170000-0600 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name | West Jordan | WEST JORDAN |
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
| address | 13169 Slover Ave Suite A, Fontana, CA 92337 | 13169 Slover Ave |
| city_name | Fontana | FONTANA |
| location_name | NRI Distribution | NRI 3PL (LC) |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 1630 S 5070 W, Salt Lake City, UT 84104 | 1630 SOUTH 5070 WEST |
| city_name | Salt Lake City | SALT LAKE CITY |
| location_name | Pacific Flyway DC - Inbound | SPORTSMAN WAREHOUSE DISTRIBUTION |


### 3071726_tms.json (Accuracy: 54.17%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | CL | CHEESUWA |
| freight_charge | 1850.0 | 1700 |
| otherchargetotal | 0 | 150 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | DART/SOLO CONTAINER | DART CONTAINOR CORP |
| sched_arrive_early | 20250310060000-0700 | 20250311060000-0600 |
| sched_arrive_late | 20250310170000-0700 | 20250311170000-0600 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | BWC SYSCO INTERMOUNTAIN 005 | Sysco Intermountain - Food Distributor & |
| sched_arrive_early | 20250312090000-0700 | 20250313091100-0600 |
| sched_arrive_late | 20250312090000-0700 |  |


### 3945196_tms.json (Accuracy: 58.33%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | LI | LANDSTFL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 110 Ohio Gulch Rd, Hailey, ID 83333 | 110 OHIO GULCH ROAD |
| city_name | Hailey | HAILEY |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 3110 S 900 W, Salt Lake City, UT 84101 | 3110 SOUTH 900 WEST |
| city_name | Salt Lake City | SALT LAKE CITY |
| zip_code | 84101 | 84104 |
| location_name | Rocky Mtn. Recycling (South) | ROCKY MOUNTAIN RECYCLING |
| sched_arrive_early | 20241227073000-0700 | 20241224140000-0700 |


### 6347607_tms.json (Accuracy: 58.33%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| blnum | 0100211029 | 6347607 |
| customer_id | DT | ARRIAUTX |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 27255 SW 95TH AVE | 27255 SOUTH WEST 95TH AVENUE |
| city_name | Wilsonville | WILSONVILLE |
| location_name | FINISHED GOODS - PACIFIC FOODS | PACIFIC FOODS |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 500 SUGAR ST | 500 NORTH SUGAR STREET |
| city_name | Layton | LAYTON |
| location_name | SMITH'S - LAYTON DIST CNTR | SMITHS DISTRIBUTION CENTER |


### 2001809674_tms.json (Accuracy: 58.33%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | SHARPTRI | MOLOCHIL |
| equipment_type_id | V | VR |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 151 S. Walnut Rd., Turlock, CA 95380 | 151 SOUTH WALNUT ROAD |
| city_name | Turlock | TURLOCK |
| sched_arrive_late | 20241204140000-0700 |  |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 3110 E Miraloma Ave, Anaheim, CA 92806-1906 | 3110 E Miraloma Ave |
| city_name | Anaheim | ANAHEIM |
| sched_arrive_late | 20241205070000-0700 |  |


### 2001868099_tms.json (Accuracy: 62.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | MS | MOLOCHIL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 10409 Sanden Drive, Dallas, TX 75238 | 10409 Sanden Dr |
| city_name | Dallas | DALLAS |
| location_name | Absopure Waters | Hydration Source |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 700 CVS DRIVE, ENNIS, TX 75119 | 700 Coves Dr |
| city_name | Ennis | ENNIS |
| location_name | CVS TEXAS DIST L P | CVS Health Distribution Center |


### 31440-90145_tms.json (Accuracy: 62.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | JC | NEONSCAZ |
| freight_charge | 1100.0 | 800 |
| otherchargetotal | 0 | 300 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name | Las Vegas | LAS VEGAS |
| location_name | Johnstone Supply | Las Vegas Distribution Center |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name | Springville | SPRINGVILLE |
| location_name | Supanaturals | MOUNTAINLAND SUPPLY CO |


### 506573704_tms.json (Accuracy: 62.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | CR | CHROBIIA |
| total_charge | 286.81 | 270 |
| otherchargetotal | 16.81 | 0 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name | Dallas | DALLAS |
| location_name | Gatorade-Dallas | Gatorade |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name | Fort Worth | FORT WORTH |
| location_name | SILVERCREEK | Silver Creek Materials |


### 14446278_tms.json (Accuracy: 62.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | ST | SUNTBOFL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name | Longview | LONGVIEW |
| location_name | FXI | FLEXIBLE FOAM |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 2400 South 600 W | For BOON Purposes - DO NOT USE |
| city_name | Salt Lake City | WELLSVILLE |
| zip_code | 84115 | 84339 |
| location_name | Salt Lake Mattress Co/ Serta | NEEDS ATTENTION |


### 8226477_tms.json (Accuracy: 62.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | SOARSAUT | NOLAROGA |
| freight_charge | 0 | 700 |
| total_charge | 0 | 700 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name | San Leandro | SAN LEANDRO |
| location_name | RCCB - SAN LEANDRO CA PRODUCTION | Reyes coca cola truck Entrance |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name | Santa Maria | SANTA MARIA |
| location_name | RCCB - SANTA MARIA CA SALES | RCCB CA Sales |


### 61814758_tms.json (Accuracy: 62.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | UNKNOWN | ECCOGLIL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | GATORADE DC TACOMA WA OVERFLOW | GATORADE DC TACOMA |
| sched_arrive_early | 20250311124500-0700 | 20250311124500-0600 |
| sched_arrive_late | 20250311124500-0700 | 20250311124500-0600 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | ADMIRAL BEV/OLD FAITHFUL | ADMIRAL BEVERAGE CORP |
| sched_arrive_early | 20250313070000-0700 | 20250313070000-0600 |
| sched_arrive_late | 20250313140000-0700 | 20250313140000-0600 |


### 504819841_tms.json (Accuracy: 62.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | UNKNOWN | CHROBIIA |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 658 South 7th Street, Reading, PA 19602 | 658 S 7th St |
| city_name | Reading | READING |
| location_name | UCI Mill / DS Smith | United Corrstack / Ds Smith |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 3021 Taylor Dr, Asheboro, NC 27203 | 3021 Taylor Dr |
| city_name | Asheboro | ASHEBORO |
| location_name | SOUTHCORR PACKAGING, LLC | DS Smith Asheboro |


### 7363582_tms.json (Accuracy: 62.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | AL | ALLELACA |
| freight_charge | 875.0 | 775 |
| otherchargetotal | 0 | 100 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | ARDENT MILLS LLC | Ardent Mills Yuba City Mill |
| sched_arrive_late | 20241227150000-0700 | 20241227130000-0700 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | MIRA LOMA DRY #960 | COSTCO DISTRIBUTION 960 |
| sched_arrive_late | 20241228053000-0700 | 20241228033000-0700 |


### 1931823_tms.json (Accuracy: 62.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | CL | CIRCFOI1 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | Oakland, CA 94603 | 9999 San Leandro St |
| city_name | Oakland | OAKLAND |
| location_name | Oakland Pickup | Cold Ice Inc |


### 504102841_tms.json (Accuracy: 62.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | CR | CHROBIIA |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 658 South 7th Street, Reading, PA 19602 | 658 S 7th St |
| city_name | Reading | READING |
| location_name | UCI Mill / DS Smith | United Corrstack / Ds Smith |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 3021 Taylor Dr, Asheboro, NC 27203 | 3021 Taylor Dr |
| city_name | Asheboro | ASHEBORO |
| location_name | SOUTHCORR PACKAGING, LLC | DS Smith Asheboro |


### 61048221_tms.json (Accuracy: 62.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | MC | ECCOGLIL |
| freight_charge | 2815.0 | 2330 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 20405 EAST BUSINESS PKWY | 20405 E Walnut Dr N |
| location_name | TROPICANA DC WALNUT CA | Tropicana DC |


### 31421-79757_tms.json (Accuracy: 62.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| freight_charge | 2177.0 | 1250 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 815 Houser Way N, The Landing Renton, WA 98055 | 815 HOUSER WAY NORTH |
| city_name | Renton | RENTON |
| location_name | JAVA TRADING CO LLC | JAVA TRADING |


### 504104411_tms.json (Accuracy: 62.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | CR | CHROBIIA |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 3737 Dan Morton Dr STE 150, Dallas, TX 75236 | 3737 Dan Morton Dr |
| city_name | Dallas | DALLAS |
| location_name | GREIF DALLAS - DBA MULTI CORRCHOICE | GREIF DALLAS |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 6195 S 300 W STE 300, Salt Lake City, UT 84104-6013 | 6195 WEST 300 SOUTH SUITE 300 |
| city_name | Salt Lake City | SALT LAKE CITY |
| location_name | PREMIER PKG % INTERWEST TRANSPORTATION - IDSLC | INTERWEST TRANSPORTATION |


### 32688939_tms.json (Accuracy: 62.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | SHARPTRI | COYOALGA |
| freight_charge | 2000.0 | 1697.72 |
| otherchargetotal | 0 | 302.28 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name | Monticello | MONTICELLO |
| sched_arrive_late | 20250122150000-0700 | 20250122130000-0700 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name | Tullahoma | TULLAHOMA |
| sched_arrive_late | 20250123130000-0700 | 20250123110000-0700 |


### 607273_tms.json (Accuracy: 62.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| blnum | #607273 | 607273 |
| customer_id | SL | SPARROIL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 15750 MERIDIAN PKWY RIVERSIDE, CA 92518 | 15750 Meridian Pkwy |
| location_name | SYSCO RIVERSIDE | Sysco Riverside - Wholesale Restaurant F |


### 2001073484_tms.json (Accuracy: 62.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | WL | WERNOMNE |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 1400 W Rincon St, Corona, CA 92878 | 1400 W Rincon St |
| city_name | Corona | CORONA |
| location_name | Vegfresh | Veg-Fresh Farms |


### 60847782_tms.json (Accuracy: 62.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | EG | ECCOGLIL |
| freight_charge | 1587.5 | 1500 |
| otherchargetotal | 0 | 87.5 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | QUAKER DC TACOMA | QUAKER |


### 1183886_tms.json (Accuracy: 66.67%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| blnum | S965843 | 1183886 |
| equipment_type_id | V | R |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name | Medford | MEDFORD |
| sched_arrive_late | 20250217190000-0700 | 20250217170000-0700 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name | Brigham City | BRIGHAM CITY |
| sched_arrive_late | 20250219120000-0700 | 20250219100000-0700 |


### 3068716_tms.json (Accuracy: 66.67%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | CL | CHEESUWA |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name | Lacey | LACEY |
| location_name | DART/SOLO CONTAINER | DART CONTAINOR CORP |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 5400 W Hwy 83 | 5400 WEST HIGHWAY 83 |
| city_name | Corinne | CORINNE |
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


### 8665815_tms.json (Accuracy: 66.67%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | SHARPTRI | TRINITDE |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 200 WEST INDUSTRIAL BLV, CLEBURNE, TX 76033 | 200 W Industrial Blvd |
| sched_arrive_late | 20241211090000-0700 |  |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 3104 OAK LANE, DALLAS, TX 75226 | 3104 Oak Ln |
| location_name | PAMACO INSULATION, LLC | Pamaco Inc. |
| sched_arrive_late | 20241211133000-0700 | 20241211130000-0700 |


### 2145346_tms.json (Accuracy: 66.67%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| blnum | 4502378939 | 2145346 |
| customer_id | UNKNOWN | AXLEKNTN |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 2115 Exchange Dr., ARLINGTON TX 76011 | 2115 Exchange Dr |
| location_name | Blue Ribbon | Blue Ribbon Delivery Inc |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 3300 Century Circle, IRVING TX 75062 | 3300 Century Cir |
| location_name | McCormick | Mc Cormick & Co Inc |


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


### 8299332_tms.json (Accuracy: 70.83%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | UNKNOWN | NOLAROGA |
| freight_charge | 0 | 1500 |
| total_charge | 0 | 1500 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name | Annapolis Junction | ANNAPOLIS JCT |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name | Saltillo | SALTILLO |


### 4231282_tms.json (Accuracy: 70.83%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | SC | VISUWAIL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | Swire Coca-Cola | COCA-COLA BOTTLING CO. |
| sched_arrive_late | 20241212133000-0700 |  |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 12634 S 265 W | 12634 SOUTH 265 WEST |
| sched_arrive_late | 20241214130000-0700 |  |


### 3294690_tms.json (Accuracy: 70.83%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | KF | KNIGPHAZ |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | NOVA CONTAINER FREIGHT | Beme, Nova Container Freight Station |
| sched_arrive_late | 20241204160000-0700 |  |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| zip_code |  | 84116 |
| location_name | EXPEDITORS SALT LAKE CITY | EXPEDITORS INTERNATIONAL |


### 5001712233_tms.json (Accuracy: 70.83%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | PI | PRIMSPMO |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | SOUTHWEST CHEESE | SWC CLOVIS POWDER STORE |
| sched_arrive_late | 20241217150000-0700 |  |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 780 W 1400 S | 780 WEST 1400 SOUTH |
| sched_arrive_late | 20241219120000-0700 |  |


### 60866061_tms.json (Accuracy: 70.83%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | EG | ECCOGLIL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| sched_arrive_late | 20241226120000-0700 |  |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 5995 W 300 S | 5995 WEST  300 SOUTH |
| location_name | COSTCO | COSTCO DISTRIBUTION 584 |
| sched_arrive_late | 20241228100000-0700 |  |


### 3070085_tms.json (Accuracy: 70.83%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | SHARPTRI | CHEESUWA |
| freight_charge | 270.0 | 0 |
| otherchargetotal | 0 | 270 |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | DART/SOLO CONTAINER | DART CONTAINOR CORP |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | BWC SYSCO INTERMOUNTAIN | Sysco Intermountain - Food Distributor & |


### 2001836741_tms.json (Accuracy: 70.83%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | UNKNOWN | MOLOCHIL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name | Dallas | DALLAS |
| location_name | Absopure Waters - Absopure | Hydration Source |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name | Ennis | ENNIS |
| location_name | CVS TEXAS DIST L P | CVS Health Distribution Center |


### 14342080_tms.json (Accuracy: 70.83%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | ST | SUNTBOFL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name | Longview | LONGVIEW |
| location_name | FXI | FLEXIBLE FOAM |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name | Salt Lake City | SALT LAKE CITY |
| location_name | FXI | SERTA MATTRESS |


### 6371326_tms.json (Accuracy: 75.00%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | AL | ARRIAUTX |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name | Bellevue | BELLEVUE |
| location_name | SWIRE CCUSA BELLEVUE WA PROD CTR | COCA-COLA BOTTLING CO. |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name | Draper | DRAPER |


### 61174109_tms.json (Accuracy: 75.00%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| blnum | 1921116001444785 | 61174109 |
| customer_id | EG | ECCOGLIL |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 5995 W 300 S | 5995 WEST  300 SOUTH |
| location_name | COSTCO SALT LAKE CITY #584 | COSTCO DISTRIBUTION 584 |


### 0148909_tms.json (Accuracy: 75.00%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | CT | COASDEIL |
| equipment_type_id | C20 | V |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | Savannah Logistics Warehouse | MERCER DISTRIBUTION SERVICES |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | KIMBALL RENTALS LLC | Kimball Equipment Company |


### 0245658_tms.json (Accuracy: 75.00%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | FT | CASHWEUT |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | Americold Logistics | AMERICOLD |
| sched_arrive_late | 20241220100000-0700 |  |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| sched_arrive_late | 20241224090000-0700 |  |


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
| blnum | 1932889403140138 | 61407132 |
| customer_id | UNKNOWN | ECCOGLIL |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 5995 W 300 S | 5995 WEST  300 SOUTH |
| location_name | COSTCO | COSTCO DISTRIBUTION 584 |


### 31483-42812_tms.json (Accuracy: 75.00%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | SF | CHROBIIA |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name | Grand Prairie | GRAND PRAIRIE |
| location_name | POWER PACKAGING A DHL COMPANY | Power Packing of Texas Inc |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name | Fort Worth | FORT WORTH |


### 61578870_tms.json (Accuracy: 75.00%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | UNKNOWN | ECCOGLIL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | LGE NG2 Warehouse | LGE US DC TACOMA |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | IDC/FREEPORT CENTER BUILDING D-7 FREEPORT CENTER | Freeport Center Building D7 |
| location_name | R.C. WILLEY HOME FURNISHING | RC Willey |


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


### 70729538_tms.json (Accuracy: 75.00%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | SHARPTRI | AVENCHIL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | SMURFIT KAPPA/OCC | SMURFIT KAPPA COATING MILL |
| sched_arrive_late | 20250224173000-0700 | 20250224153000-0700 |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | SMURFIT SPANISH FORK | WestRock / Smurfit |


### 6637008_tms.json (Accuracy: 75.00%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | DT | ARRIAUTX |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name | Winlock | WINLOCK |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| city_name | Salt Lake City | SALT LAKE CITY |
| sched_arrive_late | None | 20250306080000-0700 |


### 60752192_tms.json (Accuracy: 75.00%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | EG | ECCOGLIL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | LONGVIEW FIBRE PAPER - PACKAGING INC | KAPSTONE KRAFT PAPER |
| sched_arrive_late | 20241208130000-0700 |  |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 451 N 5600 W | 451 NORTH 5600 WEST |


### 504798115_tms.json (Accuracy: 79.17%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | CR | CHROBIIA |
| total_charge | 632.6 | 526 |
| otherchargetotal | 106.6 | 0 |


### 61579102_tms.json (Accuracy: 79.17%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | MC | ECCOGLIL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | Gallo Winery | GALLO |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | CVS | CVS ANNEX WHSE #H1L3 |


### 61231181_tms.json (Accuracy: 79.17%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | EG | ECCOGLIL |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 5995 W 300 S | 5995 WEST  300 SOUTH |
| location_name | COSTCO | COSTCO DISTRIBUTION 584 |


### 61465411_tms.json (Accuracy: 79.17%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | EG | ECCOGLIL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | QUAKER DC TACOMA | QUAKER |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 531 W 600 N | 531 WEST 600 NORTH |


### 61550952_tms.json (Accuracy: 79.17%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | MC | ECCOGLIL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | QUAKER DC TACOMA | QUAKER |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 531 W 600 N | 531 WEST 600 NORTH |


### 60778077_tms.json (Accuracy: 79.17%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | EG | ECCOGLIL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | QUAKER DC TACOMA | QUAKER |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 531 W 600 N | 531 WEST 600 NORTH |


### 61375773_tms.json (Accuracy: 79.17%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | UNKNOWN | ECCOGLIL |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 5995 W 300 S | 5995 WEST  300 SOUTH |
| location_name | COSTCO SALT LAKE CITY #584 | COSTCO DISTRIBUTION 584 |


### 61217638_tms.json (Accuracy: 79.17%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | UNKNOWN | ECCOGLIL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | QUAKER DC TACOMA | QUAKER |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 531 W 600 N | 531 WEST 600 NORTH |


### 14530945_tms.json (Accuracy: 79.17%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | ST | SUNTBOFL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | FXI | FLEXIBLE FOAM |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | Salt Lake Mattress Co/ Serta | SERTA MATTRESS |


### 4233261_tms.json (Accuracy: 79.17%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | VP | VISUWAIL |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | Swire Coca-Cola | COCA-COLA BOTTLING CO. |

#### Stop 2 (SO, Sequence 2) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| address | 12634 S 265 W | 12634 SOUTH 265 WEST |


### 1353403_tms.json (Accuracy: 83.33%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | UNKNOWN | TASEMATX |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | KNAUF INSULATION | Knauf Fiberglass |


### 4006371285_tms.json (Accuracy: 83.33%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | SHARPTRI | SCHNEIKY |

#### Stop 1 (PU, Sequence 1) Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| location_name | SOLO CUP CO | DART CONTAINOR CORP |


### 3068411_tms.json (Accuracy: 87.50%)

#### Field Mismatches

| Field | Converted Value | Ground Truth Value |
|-------|----------------|--------------------|
| customer_id | CL | CHEESUWA |


