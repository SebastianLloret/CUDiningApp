/**
 * G for Aimeejs
 * Author by gavinning
 * Homepage https://github.com/Aimeejs/g
 */

class G {

    /**
     * 为一组数据生成Map
     * @param   {Array}     arr   数据数组
     * @param   {String}    key   数据子对象的key
     * @param   {Function}  fn    处理key值的回调
     * @return  {Object}          生成的Map
     * @example this.map()
     */
    map(arr, key, fn) {
        var map = {};
        arr.forEach((item) => {
            fn ?
                // 存在fn时
                map[item[key]] = fn(item):
                // 不存在fn时，返回item自身
                map[item[key]] = item;
        })
        return map;
    }

    /**
     * Map => Array
     * @param   {Object}   map Map数据
     * @param   {Function} fn  处理数据的回调
     * @return  {Array}        处理后的数组
     * @example this.toArray({a:1}, (key, value) => {return key}) ==> ['a']
     * @example this.toArray({a:1}, (key, value) => {return value}) ==> [1]
     */
    toArray(map, fn) {
        var key;
        var array = [];
        for(key in map){
            array.push(fn(key, map[key]));
        }
        return array;
    }

    /**
     * 获取一个Map的key的数组
     * @param   {Object}   map Map对象
     * @param   {Function} fn  对key的处理回调
     * @return  {Array}       包装后的数组
     * @example this.getKeyArray({a:1, b:2}) => ['a', 'b']
     */
    getKeyArray(map, fn) {
        return this.toArray(map, (key, value) => {
            return fn ? fn(key) : key;
        })
    }

    /**
     * 获取一个Map的value的数组
     * @param   {Object}   map Map对象
     * @param   {Function} fn  对value的处理回调
     * @return  {Array}       包装后的数组
     * @example this.getValueArray({a:1, b:2}) => [1, 2]
     */
    getValueArray(map, fn) {
        return this.toArray(map, (key, value) => {
            return fn ? fn(value) : value;
        })
    }
}

let g = new G;
g.G = G;
module.exports = g['default'] = g;
