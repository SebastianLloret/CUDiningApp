g
---

### Install

For Aimeejs
```sh
aimee i g --save
```
```js
import g from 'g'
// or
var g = require('g')
```

For Nodejs
```sh
npm i node-g --save
```
```js
var g = require('node-g')
```

### Documents
`` g.map => ``
```js
var arr = [
	{
		a: 1,
		b: 1
	},
	{
		a: 2,
		b: 2
	},
	{
		a: 3,
		b: 3
	}
]
var map = g.map(arr, 'a')
console.log(map)

// result =>
// { '1': { a: 1, b: 1 }, '2': { a: 2, b: 2 }, '3': { a: 3, b: 3 } }
```

``g.toArray``
```js
var obj = {
	a: 1,
	b: 2,
	c: 3,
	d: 4
}

var arr = g.toArray(obj, (key, value) => {
	return key
})
console.log(arr)
// result =>
// [ 'a', 'b', 'c', 'd' ]


var arr1 = g.toArray(obj, (key, value) => {
	return value
})
console.log(arr1)
// result =>
// [ 1, 2, 3, 4 ]


var arr2 = g.toArray(obj, (key, value) => {
	return function() {
		`<a href="/get/${key}">${value}</a>`
	}
})
console.log(arr2)
// result =>
// [ [Function], [Function], [Function], [Function] ]
```

``g.getKeyArray``
```js
var obj = {
	a: 1,
	b: 2,
	c: 3,
	d: 4
}
var test = {
	a: 123,
	aa: 12345,
	aaa: 1234567,
	b: 456,
	bb: 45678,
	bbb: 456789,
	c: 145,
	d: 496
}

var arr = g.getKeyArray(obj)
console.log(arr)
// result =>
// [ 'a', 'b', 'c', 'd' ]

var arr1 = g.getKeyArray(obj, key => {
	return test[key]
})
console.log(arr1)
// result =>
// [ 123, 456, 145, 496 ]
```

``g.getValueArray``
```js
var obj = {
	a: 1,
	b: 2,
	c: 3,
	d: 4
}
var test = {
	a: 123,
	aa: 12345,
	aaa: 1234567,
	b: 456,
	bb: 45678,
	bbb: 456789,
	c: 145,
	d: 496
}

var arr = g.getValueArray(obj)
console.log(arr)
// result =>
// [ 1, 2, 3, 4 ]

var arr1 = g.getValueArray(obj, value => {
	return value + 10
})
console.log(arr1)
// result =>
// [ 11, 12, 13, 14 ]
```