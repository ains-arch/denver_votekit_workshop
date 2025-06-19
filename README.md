11 city council members in precincts (2 at large)

gpkg city council precincts geoms and candidate assignment. might have at large data

Working Report Link: https://docs.google.com/document/d/1VqDG7T1osMLAX2hxbx2l_WlVqGyNsUdRJpndx3jLob4/edit?usp=sharing

# data preview
## denver_city_council.gpkg
```
<class 'geopandas.geodataframe.GeoDataFrame'>
RangeIndex: 13 entries, 0 to 12
Data columns (total 6 columns):
 #   Column    Non-Null Count  Dtype   
---  ------    --------------  -----   
 0   DIST_NUM  11 non-null     float64 
 1   DIST_REP  13 non-null     object  
 2   NOTES     2 non-null      object  
 3   GLOBALID  13 non-null     object  
 4   URL_LINK  13 non-null     object  
 5   geometry  13 non-null     geometry
dtypes: float64(1), geometry(1), object(4)
memory usage: 756.0+ bytes
```

```
   DIST_NUM         DIST_REP NOTES                                GLOBALID                              URL_LINK                                           geometry
0       6.0    Paul Kashmann  None  {E32EE291-9AAF-4374-96DE-0C3CD04312FA}   https://www.denvergov.org/district6  MULTIPOLYGON (((3150429.065 1685445.781, 31504...
1       9.0   Darrell Watson  None  {8B3BC287-A3E1-4549-827C-93A9F6E12D78}   https://www.denvergov.org/district9  MULTIPOLYGON (((3149277.482 1716097.796, 31486...
2       1.0  Amanda Sandoval  None  {85225A22-4FDE-4332-9E19-7D1FE607274C}   https://www.denvergov.org/district1  MULTIPOLYGON (((3134585.633 1714580.431, 31343...
3       2.0      Kevin Flynn  None  {F6CDE34C-3B1D-4B60-9B13-0C93DE2D7C82}   https://www.denvergov.org/district2  MULTIPOLYGON (((3133659.751 1676374.036, 31335...
4      10.0      Chris Hinds  None  {7DCBE7AE-A755-4E8C-B950-5A9B4EE62C48}  https://www.denvergov.org/district10  MULTIPOLYGON (((3141333.769 1700874.412, 31412...
```

## Denver_pop.parquet
```
<class 'pandas.core.frame.DataFrame'>
Index: 346 entries, vtd:08031031241 to vtd:08031031827
Data columns (total 7 columns):
 #   Column             Non-Null Count  Dtype
---  ------             --------------  -----
 0   tot_pop_20         346 non-null    int64
 1   bpop_20            346 non-null    int64
 2   hpop_20            346 non-null    int64
 3   asian_nhpi_pop_20  346 non-null    int64
 4   amin_pop_20        346 non-null    int64
 5   other_pop_20       346 non-null    int64
 6   white_pop_20       346 non-null    int64
dtypes: int64(7)
memory usage: 21.6+ KB
```

```
                 tot_pop_20  bpop_20  hpop_20  asian_nhpi_pop_20  amin_pop_20  other_pop_20  white_pop_20
id                                                                                                       
vtd:08031031241        1348       45      126                 58           11            17          1091
vtd:08031031639        1383       12       67                 58           11            19          1216
vtd:08031031229        1099       13       84                 54           17            11           920
vtd:08031031230        1232       13       93                 90           13            12          1011
vtd:08031031237        3273      249      315                322           33            36          2318
```

## Denver_vap.parquet
```
<class 'pandas.core.frame.DataFrame'>
Index: 346 entries, vtd:08031031241 to vtd:08031031827
Data columns (total 7 columns):
 #   Column             Non-Null Count  Dtype
---  ------             --------------  -----
 0   tot_vap_20         346 non-null    int64
 1   bvap_20            346 non-null    int64
 2   hvap_20            346 non-null    int64
 3   asian_nhpi_vap_20  346 non-null    int64
 4   amin_vap_20        346 non-null    int64
 5   other_vap_20       346 non-null    int64
 6   white_vap_20       346 non-null    int64
dtypes: int64(7)
memory usage: 21.6+ KB
```

```
                 tot_vap_20  bvap_20  hvap_20  asian_nhpi_vap_20  amin_vap_20  other_vap_20  white_vap_20
id                                                                                                       
vtd:08031031241        1106       34       88                 40           10            15           919
vtd:08031031639        1074       11       47                 38            5            15           958
vtd:08031031229         853        8       61                 30           13             8           733
vtd:08031031230         865        2       69                 33            4             5           752
vtd:08031031237        3196      227      302                314           30            34          2289
```

## Denver_elections.parquet
```
<class 'pandas.core.frame.DataFrame'>
Index: 346 entries, vtd:08031031241 to vtd:08031031827
Data columns (total 16 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   pres_08_dem  346 non-null    int64
 1   pres_08_rep  346 non-null    int64
 2   pres_12_dem  346 non-null    int64
 3   pres_12_rep  346 non-null    int64
 4   pres_16_dem  346 non-null    int64
 5   pres_16_rep  346 non-null    int64
 6   sen_16_dem   346 non-null    int64
 7   sen_16_rep   346 non-null    int64
 8   gov_18_dem   346 non-null    int64
 9   gov_18_rep   346 non-null    int64
 10  ag_18_dem    346 non-null    int64
 11  ag_18_rep    346 non-null    int64
 12  pres_20_dem  346 non-null    int64
 13  pres_20_rep  346 non-null    int64
 14  sen_20_dem   346 non-null    int64
 15  sen_20_rep   346 non-null    int64
dtypes: int64(16)
memory usage: 46.0+ KB
```

```
                 pres_08_dem  pres_08_rep  pres_12_dem  pres_12_rep  pres_16_dem  pres_16_rep  ...  ag_18_dem  ag_18_rep  pres_20_dem  pres_20_rep  sen_20_dem  sen_20_rep
VTD                                                                                            ...                                                                        
vtd:08031031241          566          190          580          240          644          165  ...        621        179          751          207         740         235
vtd:08031031639          637          253          601          357          677          217  ...        642        238          814          222         777         277
vtd:08031031229          466          222          410          265          459          167  ...        466        215          605          171         582         216
vtd:08031031230          432          231          454          271          502          195  ...        499        244          627          189         591         246
vtd:08031031237          995          305         1079          421         1289          240  ...        869        153          895          138         848         166

[5 rows x 16 columns]
```

## Denver_precincts.parquet
```
<class 'pandas.core.frame.DataFrame'>
Index: 346 entries, 302 to 647
Data columns (total 15 columns):
 #   Column      Non-Null Count  Dtype 
---  ------      --------------  ----- 
 0   STATEFP20   346 non-null    object
 1   COUNTYFP20  346 non-null    object
 2   VTDST20     346 non-null    object
 3   GEOID20     346 non-null    object
 4   VTDI20      346 non-null    object
 5   NAME20      346 non-null    object
 6   NAMELSAD20  346 non-null    object
 7   LSAD20      346 non-null    object
 8   MTFCC20     346 non-null    object
 9   FUNCSTAT20  346 non-null    object
 10  ALAND20     346 non-null    int64 
 11  AWATER20    346 non-null    int64 
 12  INTPTLAT20  346 non-null    object
 13  INTPTLON20  346 non-null    object
 14  geometry    346 non-null    object
dtypes: int64(2), object(13)
memory usage: 43.2+ KB
```

```
    STATEFP20 COUNTYFP20 VTDST20      GEOID20 VTDI20      NAME20  ... FUNCSTAT20 ALAND20 AWATER20   INTPTLAT20    INTPTLON20                                           geometry
302        08        031  031241  08031031241      A  Denver 241  ...          N  531573        0  +39.6765106  -104.9809775  b'\x01\x03\x00\x00\x00\x01\x00\x00\x00Z\x00\x0...
303        08        031  031639  08031031639      A  Denver 639  ...          N  486619        0  +39.6965898  -104.9628491  b'\x01\x03\x00\x00\x00\x01\x00\x00\x00>\x00\x0...
304        08        031  031229  08031031229      A  Denver 229  ...          N  845123        0  +39.6895881  -104.9653561  b'\x01\x03\x00\x00\x00\x01\x00\x00\x00d\x00\x0...
305        08        031  031230  08031031230      A  Denver 230  ...          N  421848        0  +39.6904954  -104.9551128  b'\x01\x03\x00\x00\x00\x01\x00\x00\x00I\x00\x0...
306        08        031  031237  08031031237      A  Denver 237  ...          N  906997        0  +39.6790394  -104.9634185  b'\x01\x03\x00\x00\x00\x01\x00\x00\x00q\x00\x0...
```
