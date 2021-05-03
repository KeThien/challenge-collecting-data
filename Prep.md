# Which element and how in the item page

## Locality

We can get it in the link (cfr anatomy of the link) by URLparse in python

## Type of property (House/apartment)

We can get it in the link (cfr anatomy of the link) by URLparse in python

## Subtype of property (Bungalow, Chalet, Mansion, ...)

We can get it in the link (cfr anatomy of the link) by URLparse in python

## Price

```html
<p class="classified__price">
  <span aria-hidden="true">€295,000</span>
  <span class="sr-only">295000€</span>
</p>
```

## Type of sale (Exclusion of life sales)

if public sale:

```html
<h2 class="text-block__title">Public sale</h2>
```

Life annuity sale or Viager in french(need to be excluded):

```html
<div class="flag-list__item flag-list__item--secondary">
  <!---->
  <span class="flag-list__text">life annuity</span>
</div>
```

else it's private

## Number of rooms

need to select bedrooms and bathrooms and make a sum or just take number of bedrooms from the top

```html
<p class="classified__information--property">
  2 bedrooms
  <span aria-hidden="true">|</span>
  90
  <span class="abbreviation">
    <span aria-hidden="true">m²</span>
    <span class="sr-only">square meters</span>
  </span>
</p>
```

## Area

Same element as number of rooms or "Living area" with regex

```html
<tr class="classified-table__row">
  <th scope="row" class="classified-table__header">Living area</th>
  <td class="classified-table__data">
    90
    <span class="abbreviation"
      ><span aria-hidden="true"> m² </span>
      <span class="sr-only"> square meters </span></span
    >
  </td>
</tr>
```

## Fully equipped kitchen (Yes/No)

if the mention or html element exists

```html
<tr class="classified-table__row">
  <th scope="row" class="classified-table__header">Kitchen type</th>
  <td class="classified-table__data">Installed</td>
</tr>
```

## Furnished (Yes/No)

```html
<tr class="classified-table__row">
  <th scope="row" class="classified-table__header">Furnished</th>
  <td class="classified-table__data">No</td>
</tr>
```

## Open fire (Yes/No)

if the mention fireplaces or html element exists

```html
<tr class="classified-table__row">
  <th scope="row" class="classified-table__header">How many fireplaces?</th>
  <td class="classified-table__data">1</td>
</tr>
```

## Terrace (Yes/No) If yes: Area

```html
<tr class="classified-table__row">
  <th scope="row" class="classified-table__header">Terrace surface</th>
  <td class="classified-table__data">
    3
    <span class="abbreviation">
      <span aria-hidden="true">m²</span>
      <span class="sr-only">square meters</span>
    </span>
  </td>
  <tr class="classified-table__row">
    <th scope="row" class="classified-table__header">How many fireplaces?</th>
    <td class="classified-table__data">1</td>
  </tr>
</tr>
```

## Garden (Yes/No) If yes: Area

```html
<tr class="classified-table__row">
  <th scope="row" class="classified-table__header">Garden surface</th>
  <td class="classified-table__data">
    70
    <span class="abbreviation"
      ><span aria-hidden="true"> m² </span>
      <span class="sr-only"> square meters </span></span
    >
  </td>
</tr>
```

## Surface of the land

Sums of All surfaces ?

## Surface area of the plot of land

```html
<tr class="classified-table__row">
  <th scope="row" class="classified-table__header">Surface of the plot</th>
  <td class="classified-table__data">
    250

    <span class="abbreviation"
      ><span aria-hidden="true"> m² </span>
      <span class="sr-only"> square meters </span></span
    >
  </td>
</tr>
```

## Number of facades

```html
<tr class="classified-table__row">
  <th scope="row" class="classified-table__header">Number of frontages</th>
  <td class="classified-table__data">3</td>
</tr>
```

## Swimming pool (Yes/No)

```html
<tr>
  <th scope="row" class="classified-table__header">Swimming pool</th>
  <td class="classified-table__data">No</td>
</tr>
```

## State of the building (New, to be renovated, ...)

```html
<tr class="classified-table__row">
  <th scope="row" class="classified-table__header">Building condition</th>
  <td class="classified-table__data">As new</td>
</tr>
```

# Anatomy of the URL by search

https://www.immoweb.be/en/classified/apartment/for-sale/etterbeek/1040/9310998
https://www.immoweb.be/en/classified/house/for-sale/sint-pieters-leeuw/1600/9310259?searchId=608fb6bfd3722

Use URLparse package from python

# Be caution about multi appartement lot like

https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/opheylissem/1357/9309251?searchId=608fc35acd434

how to adress it ?
maybe by regex and exclude when range of price like "175 000 € - 249 000 €"
or exclude all
"projet-neuf-appartements" / "new-real-estate-project-apartments" subtypes

# Steps to keep in mind for having a clean DF

### Numericals

Try as much as possible to record only numerical values. Example: Instead of defining whether the kitchen is equipped with a "Yes", use binary values.
Boolean: `True` or `False` <br>

### Price

strips of his string ex:

```
€295,000 -> 295000
295000€ -> 295000
```

### If no element is provided

No empty row. If you are missing information, set the value to None.

# Additional thoughts

We can add in the dataframe the unique ID of the item provide in the URL parameters that we can parse. So that we can easily create a link for the item page.
