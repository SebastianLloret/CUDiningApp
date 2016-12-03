var g = require('../g')

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

var arr1 = g.getKeyArray(obj, key => {
	return test[key]
})
console.log(arr1)