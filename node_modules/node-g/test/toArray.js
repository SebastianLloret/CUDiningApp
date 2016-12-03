var g = require('../g')

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


var arr1 = g.toArray(obj, (key, value) => {
	return value
})
console.log(arr1)


var arr1 = g.toArray(obj, (key, value) => {
	return value
})
console.log(arr1)


var arr2 = g.toArray(obj, (key, value) => {
	return function() {
		`<a href="/get/${key}">${value}</a>`
	}
})
console.log(arr2)