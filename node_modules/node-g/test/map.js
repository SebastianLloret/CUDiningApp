var g = require('../g')

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